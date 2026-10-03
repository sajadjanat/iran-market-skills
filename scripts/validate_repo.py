"""Validate skill packaging, metadata, links, docs and evaluation coverage offline."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

try:
    from .sync_resources import sync
except ImportError:
    from sync_resources import sync


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def load_yaml(text):
    return yaml.load(text, Loader=UniqueLoader)


def frontmatter(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("Missing YAML frontmatter")
    data = load_yaml(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("Frontmatter must be a mapping")
    return data


def markdown_links(text):
    # Code examples are not navigational links. HTML/complex reference-style
    # links are deliberately outside this small repository checker's scope.
    text = re.sub(r"(?ms)^\s*```.*?^\s*```\s*$", "", text)
    return re.findall(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text)


def local_target(origin: Path, link: str):
    parts = urlsplit(link)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    return (origin.parent / unquote(parts.path)).resolve()


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    skills = sorted(p for p in (root / "skills").glob("*") if p.is_dir())
    names = set()
    for skill in skills:
        entry = skill / "SKILL.md"
        try:
            text = entry.read_text(encoding="utf-8")
            meta = frontmatter(text)
            supported = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
            if set(meta) - supported:
                raise ValueError("Unsupported frontmatter fields: " + ", ".join(sorted(set(meta) - supported)))
            metadata = meta.get("metadata", {})
            if not isinstance(metadata, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in metadata.items()):
                raise ValueError("Metadata must map strings to strings")
            name = meta.get("name")
            if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                raise ValueError("Invalid name")
            if name != skill.name or name in names:
                raise ValueError("Name must match its folder and be unique")
            names.add(name)
            description = meta.get("description")
            if not isinstance(description, str) or not 1 <= len(description) <= 1024:
                raise ValueError("Description must have 1–1024 characters")
            compatibility = meta.get("compatibility")
            if compatibility is not None and (not isinstance(compatibility, str) or not 1 <= len(compatibility) <= 500):
                raise ValueError("Invalid compatibility")
            if meta.get("license") != "MIT":
                raise ValueError("Missing MIT metadata")
            if len(text.splitlines()) > 500:
                raise ValueError("Entrypoint exceeds repository 500-line limit")
            if re.search(r"\b(?:TODO|TBD|FIXME)\b", text):
                raise ValueError("Unfinished entrypoint scaffold")
            interface = load_yaml((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
            if not isinstance(interface, dict) or not isinstance(interface.get("interface"), dict):
                raise ValueError("UI metadata must contain an interface mapping")
            ui = interface["interface"]
            if not isinstance(ui.get("display_name"), str) or not ui["display_name"].strip():
                raise ValueError("Missing display name")
            summary = ui.get("short_description")
            if not isinstance(summary, str) or not 25 <= len(summary) <= 64:
                raise ValueError("UI description must have 25–64 characters")
            prompt = ui.get("default_prompt")
            if not isinstance(prompt, str) or "$" + name not in prompt:
                raise ValueError("Default prompt must mention $" + name)
            if interface.get("policy", {}).get("allow_implicit_invocation", True) is not True:
                raise ValueError("Preserve automatic discovery for these skills")
        except (OSError, ValueError, yaml.YAMLError, KeyError, TypeError) as exc:
            errors.append(f"{skill.name}: {exc}")
        for doc in skill.rglob("*.md"):
            try:
                for link in markdown_links(doc.read_text(encoding="utf-8")):
                    target = local_target(doc, link)
                    if target is None:
                        continue
                    if not target.is_relative_to(skill.resolve()):
                        errors.append(f"{doc.relative_to(root)}: reference escapes installable skill: {link}")
                    elif not target.exists():
                        errors.append(f"{doc.relative_to(root)}: missing local reference: {link}")
            except (OSError, ValueError) as exc:
                errors.append(f"{doc.relative_to(root)}: {exc}")

    if len(skills) != 5:
        errors.append("This release must contain exactly the five existing skills")
    try:
        stale = sync(root, check=True)
        errors.extend(f"Stale bundled resource: {p.relative_to(root)}" for p in stale)
        manifest = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        if manifest.get("skills") != "./skills/" or manifest.get("name") != "iran-market-skills":
            errors.append("Plugin manifest does not match the skill directory")
        version = manifest.get("version", "")
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append("Plugin version must use semantic versioning")
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        if f"## [{version}]" not in changelog:
            errors.append("Changelog is missing the manifest version")
        cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
        ids = set()
        covered = set()
        for case in cases:
            if case["id"] in ids:
                errors.append("Duplicate evaluation ID: " + case["id"])
            ids.add(case["id"])
            covered.add(case["skill"])
            if case["skill"] not in names or not case["request"].strip() or not case["criteria"]:
                errors.append("Invalid evaluation case: " + case["id"])
            for fixture in case.get("fixtures", []):
                target = (root / fixture).resolve()
                if not target.is_relative_to(root) or not target.is_file():
                    errors.append("Missing or unsafe evaluation fixture: " + fixture)
        if covered != names:
            errors.append("Every skill needs behavioral evaluation scenarios")
        for name in names:
            if not (root / "docs" / (name + ".md")).is_file():
                errors.append("Missing human guide: " + name)
            for readme in ("README.md", "README.fa.md"):
                if name not in (root / readme).read_text(encoding="utf-8"):
                    errors.append(readme + " omits " + name)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Repository metadata/resources: {exc}")

    for doc in root.rglob("*.md"):
        if ".git" in doc.parts or "skills" in doc.relative_to(root).parts:
            continue
        try:
            for link in markdown_links(doc.read_text(encoding="utf-8")):
                target = local_target(doc, link)
                if target is not None and (not target.is_relative_to(root) or not target.exists()):
                    errors.append(f"{doc.relative_to(root)}: broken repository link: {link}")
        except (OSError, ValueError) as exc:
            errors.append(f"{doc.relative_to(root)}: {exc}")
    for path in list(root.rglob("*.yaml")) + list(root.rglob("*.yml")):
        if ".git" in path.parts:
            continue
        try:
            load_yaml(path.read_text(encoding="utf-8"))
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: invalid YAML: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print("ERROR " + error)
    if not errors:
        print("PASS: five skill packages, metadata, local links, resources, docs and eval coverage")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
