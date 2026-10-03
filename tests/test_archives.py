"""Check portable ZIPs preserve the complete skill and reproduce identical bytes."""
import tempfile
import unittest
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

from scripts.package_skills import package

ROOT = Path(__file__).resolve().parents[1]


class ArchiveTests(unittest.TestCase):
    def test_complete_safe_reproducible_packages(self):
        with tempfile.TemporaryDirectory() as tmp:
            first, second = Path(tmp) / "first", Path(tmp) / "second"
            manifest = package(ROOT, first)
            self.assertEqual(manifest, package(ROOT, second))
            self.assertEqual(len(manifest), 5)
            for name, item in manifest.items():
                source = ROOT / "skills" / name
                with ZipFile(first / item["file"]) as archive:
                    files = archive.namelist()
                    self.assertIn(name + "/SKILL.md", files)
                    self.assertIn(name + "/LICENSE", files)
                    self.assertIn(name + "/references/evidence-policy.md", files)
                    expected = {p.relative_to(source.parent).as_posix(): p.read_bytes()
                                for p in source.rglob("*") if p.is_file()}
                    self.assertEqual(set(files), set(expected))
                    for entry in files:
                        path = PurePosixPath(entry)
                        self.assertFalse(path.is_absolute())
                        self.assertNotIn("..", path.parts)
                        self.assertEqual(path.parts[0], name)
                        self.assertEqual(archive.read(entry), expected[entry])


if __name__ == "__main__":
    unittest.main()
