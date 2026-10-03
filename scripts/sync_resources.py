"""Bundle canonical resources so each skill can be installed independently."""
from __future__ import annotations

import argparse
from pathlib import Path


def exports(root: Path):
    policy = "<!-- Generated from repository DATA-POLICY.md; run scripts/sync_resources.py. -->\n\n"
    policy += (root / "DATA-POLICY.md").read_text(encoding="utf-8")
    license_text = (root / "LICENSE").read_text(encoding="utf-8")
    for skill in sorted((root / "skills").iterdir()):
        if skill.is_dir() and (skill / "SKILL.md").is_file():
            yield skill / "references/evidence-policy.md", policy
            yield skill / "LICENSE", license_text


def sync(root: Path, check: bool = False) -> list[Path]:
    stale = []
    for target, text in exports(root):
        if target.is_file() and target.read_text(encoding="utf-8") == text:
            continue
        stale.append(target)
        if not check:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8", newline="\n")
    return stale


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    stale = sync(root, args.check)
    for path in stale:
        print(("STALE " if args.check else "WROTE ") + str(path.relative_to(root)))
    return 1 if args.check and stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
