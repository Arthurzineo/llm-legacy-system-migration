"""Optional analyzers, mixed languages, submodules and setup routing."""
import configparser
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from setup_optional_quality_tools import language_inventory, TOOL_COMMITS
from quality_gate_doctor import inspect_tools
from superpower_plan import load_manifest, route


class OptionalToolsAndSetupTest(unittest.TestCase):
    def test_supported_and_unsupported_language_scopes(self):
        with tempfile.TemporaryDirectory() as workspace:
            target = Path(workspace)
            (target / "server.go").write_text("package main\n")
            (target / "analyze.py").write_text("print('ok')\n")
            (target / "legacy.php").write_text("<?php\n")
            (target / "vendor").mkdir()
            (target / "vendor" / "hidden.go").write_text("package vendored\n")
            result = language_inventory(target)
            self.assertEqual(result["supported"].get("Go"), 1)
            self.assertEqual(result["supported"].get("Python"), 1)
            self.assertEqual(result["unsupported"].get("PHP"), 1)

    def test_git_submodule_manifest(self):
        parser = configparser.ConfigParser()
        parser.read(ROOT / ".gitmodules")
        self.assertEqual(len(TOOL_COMMITS), 3)
        for name in TOOL_COMMITS:
            section = f'submodule "tools/third-party/{name}"'
            self.assertIn(section, parser)
            self.assertEqual(parser[section]["url"], f"https://github.com/unclebob/{name}.git")

    def test_diagnostics_do_not_claim_measured_results(self):
        with tempfile.TemporaryDirectory() as workspace:
            info = inspect_tools(workspace)
            self.assertEqual(set(info), set(TOOL_COMMITS))
            self.assertTrue(all(not value["measured"] for value in info.values()))

    def test_orca_setup_is_not_fifth_superpower(self):
        entries = load_manifest()
        self.assertEqual(len(entries), 4)
        orca = next(entry for entry in entries if entry["id"] == "orca")
        self.assertIn("orca-setup", orca["required"])
        self.assertIn("setup-orca", orca["aliases"])
        self.assertIn("orca-setup", route("setup-orca")["skills_to_read_in_order"])

    def test_memory_is_in_setup(self):
        content = (ROOT / "skills/core/orca-setup/SKILL.md").read_text(encoding="utf-8")
        for term in ("memory_status", "configure_ai_memory_v2.sh", "contracts", "solo"):
            self.assertIn(term, content)


if __name__ == "__main__":
    unittest.main()
