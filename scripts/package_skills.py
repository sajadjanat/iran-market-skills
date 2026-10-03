"""Build one reproducible, self-contained upload ZIP per skill (standard library)."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def package(root: Path, output: Path) -> dict:
    skills = sorted((root / "skills").iterdir())
    output.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for skill in skills:
        if not skill.is_dir() or not (skill / "SKILL.md").is_file():
            continue
        destination = output / (skill.name + ".zip")
        with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
            for source in sorted(skill.rglob("*")):
                if not source.is_file() or "__pycache__" in source.parts:
                    continue
                if source.is_symlink():
                    raise ValueError("Package must not contain symlinks: " + str(source))
                name = source.relative_to(skill.parent).as_posix()
                entry = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, source.read_bytes())
        manifest[skill.name] = {"file": destination.name,
                               "sha256": hashlib.sha256(destination.read_bytes()).hexdigest()}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()
    manifest = package(Path(__file__).resolve().parents[1], args.output.resolve())
    print(f"Built {len(manifest)} skill ZIPs in {args.output}")
