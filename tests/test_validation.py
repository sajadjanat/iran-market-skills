"""Regression checks for failures that would break independent skill installs."""
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.sync_resources import sync
from scripts.validate_repo import frontmatter, validate


ROOT = Path(__file__).resolve().parents[1]


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.entry = self.root / "skills/iran-market-discovery/SKILL.md"

    def tearDown(self):
        self.tmp.cleanup()

    def test_real_repository(self):
        self.assertEqual(validate(self.root), [])

    def test_outside_reference_rejected(self):
        with self.entry.open("a", encoding="utf-8") as stream:
            stream.write("\n[policy](../../DATA-POLICY.md)\n")
        self.assertTrue(any("escapes installable" in e for e in validate(self.root)))

    def test_missing_packaged_reference_rejected(self):
        (self.entry.parent / "references/public-sources.md").unlink()
        self.assertTrue(any("missing local reference" in e for e in validate(self.root)))

    def test_stale_policy_detected_and_resynced(self):
        with (self.root / "DATA-POLICY.md").open("a", encoding="utf-8") as stream:
            stream.write("\nNew evidence rule.\n")
        self.assertTrue(any("Stale bundled" in e for e in validate(self.root)))
        sync(self.root)
        self.assertEqual(validate(self.root), [])

    def test_duplicate_yaml_key_rejected(self):
        with self.assertRaises(ValueError):
            frontmatter("---\nname: one\nname: two\n---\n")

    def test_default_prompt_must_route_correctly(self):
        path = self.entry.parent / "agents/openai.yaml"
        text = path.read_text(encoding="utf-8").replace("$iran-market-discovery", "$wrong-skill")
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("Default prompt" in e for e in validate(self.root)))

    def test_invalid_ui_shape_reports_error(self):
        path = self.entry.parent / "agents/openai.yaml"
        path.write_text("interface: []\n", encoding="utf-8")
        self.assertTrue(any("interface mapping" in e for e in validate(self.root)))

    def test_individual_copy_retains_runtime_links_and_license(self):
        from scripts.validate_repo import local_target, markdown_links
        for skill in (self.root / "skills").iterdir():
            isolated = Path(self.tmp.name) / "installed" / skill.name
            shutil.copytree(skill, isolated)
            isolated = isolated.resolve()
            self.assertEqual((isolated / "LICENSE").read_text(encoding="utf-8"), (self.root / "LICENSE").read_text(encoding="utf-8"))
            for doc in isolated.rglob("*.md"):
                for link in markdown_links(doc.read_text(encoding="utf-8")):
                    target = local_target(doc, link)
                    if target is not None:
                        self.assertTrue(target.is_relative_to(isolated))
                        self.assertTrue(target.exists(), link)


if __name__ == "__main__":
    unittest.main()
