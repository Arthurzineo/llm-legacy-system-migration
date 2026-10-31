"""Offline skill metadata and no-overwrite installer behavior tests."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from install_skills import inventory, install
from validate_project import validate
from scaffold_migration_outputs import FOLDERS, scaffold

class RegistryTest(unittest.TestCase):
    def test_all_catalog_skills_have_unique_names(self):
        items=inventory()
        self.assertGreaterEqual(len(items),30)
        self.assertIn('orca-coordination',items)
        self.assertIn('ai-memory-v2',items)
        self.assertIn('clean-code-quality-gates',items)

    def test_project_tree(self):
        self.assertGreaterEqual(len(validate()),30)

    def test_installer_dry_run_does_not_create_target(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'flat'
            result=install(inventory(),target,selected={'golang'},apply=False)
            self.assertEqual(len(result),1)
            self.assertFalse(target.exists())

    def test_installer_rejects_conflicting_skill(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'flat'
            install(inventory(),target,selected={'python'},apply=True)
            p=target/'python'/'SKILL.md'
            p.write_text('different existing skill')
            with self.assertRaises(ValueError):
                install(inventory(),target,selected={'python'},apply=True)
            self.assertEqual(p.read_text(),'different existing skill')

    def test_scaffold_is_opt_in_and_folder_only(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)
            result=scaffold(target,apply=False)
            self.assertEqual(len(result),len(FOLDERS))
            self.assertFalse((target/'docs').exists())
            scaffold(target,apply=True)
            self.assertTrue((target/'docs/legacy/diagrams').is_dir())
            self.assertFalse((target/'.orca').exists())

if __name__=='__main__':unittest.main()
