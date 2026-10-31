"""Superpower router and approval-safety tests."""
import tempfile
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
from superpower_plan import load_manifest, route
from install_skills import inventory, install


class SuperpowerTest(unittest.TestCase):
    def test_exactly_four_public_superpowers(self):
        manifest = load_manifest()
        self.assertEqual({e['id'] for e in manifest}, {'orca','part1','part1.1','part2'})
        self.assertEqual({name for name,(cat,_) in inventory().items() if cat=='superpowers'},
                         {e['skill'] for e in manifest})

    def test_part1_dispatch_uses_existing_skills(self):
        result = route('start-part-1', ['architecture','language-python'])
        self.assertEqual(result['stage'], 'part1')
        self.assertIn('legacy-static-inventory', result['skills_to_read_in_order'])
        self.assertIn('c4-architecture', result['skills_to_read_in_order'])
        self.assertIn('python', result['skills_to_read_in_order'])

    def test_dynamic_phase_requires_explicit_yes(self):
        initial = route('part1.1')
        self.assertTrue(initial['approval_required'])
        self.assertNotIn('isolated-legacy-runtime', initial['skills_to_read_in_order'])
        self.assertNotIn('docker', initial['skills_to_read_in_order'])
        yes = route('part1.1', decision='YES')
        self.assertFalse(yes['approval_required'])
        self.assertIn('legacy-dynamic-characterization', yes['skills_to_read_in_order'])
        for d in ['NO','DEFER']:
            no = route('part1.1', decision=d)
            self.assertNotIn('legacy-dynamic-characterization', no['skills_to_read_in_order'])
        with self.assertRaises(ValueError):
            route('part1.1', ['decision-yes'], decision=None)

    def test_part2_has_all_quality_checkpoints(self):
        result = route('part2', ['implementation','verification','cutover'])
        for s in ('legacy-incremental-implementation', 'legacy-equivalence-validation',
                  'legacy-cutover', 'tdd', 'bdd', 'mutation-testing', 'clean-code-quality-gates'):
            self.assertIn(s,result['skills_to_read_in_order'])

    def test_plan_is_read_only_and_installer_supports_superpowers(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/'skills'
            proc=subprocess.run([sys.executable, str(ROOT/'scripts/superpower_plan.py'),
                                 '--stage', 'part1.1'], capture_output=True, text=True)
            self.assertEqual(proc.returncode,0,proc.stderr)
            self.assertFalse(target.exists())
            listed=install(inventory(), target, selected={'superpower-orca'}, apply=False)
            self.assertEqual(len(listed),1)
            self.assertFalse(target.exists())


if __name__ == '__main__':
    unittest.main()
