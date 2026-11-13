"""Regression checks for Part 3 route and mandatory approvals (no external effects)."""
import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import superpower_plan


class Part3RouteTests(unittest.TestCase):
    def test_manifest_contains_five_unique_entries(self):
        routes = superpower_plan.load_manifest()
        self.assertEqual([x["id"] for x in routes], ["orca", "part1", "part1.1", "part2", "part3"])

    def test_part2_handoff(self):
        self.assertEqual(superpower_plan.route("part2")["next"], ["part3"])

    def test_part3_required_and_conditional(self):
        result = superpower_plan.route("part3", ["deployment", "parity", "operations"])
        self.assertEqual(result["superpower"], "superpower-operational-assurance")
        selected = set(result["skills_to_read_in_order"])
        for name in ("release-readiness", "controlled-rollout", "cross-client-parity",
                     "operational-observability", "operational-recovery"):
            self.assertIn(name, selected)
        self.assertFalse(result["approval_required"])

    def test_optional_characterization_cannot_be_bypassed(self):
        result = superpower_plan.route("part1.1")
        self.assertTrue(result["approval_required"])
        result = superpower_plan.route("part1.1", decision="NO")
        self.assertNotIn("legacy-dynamic-characterization", result["skills_to_read_in_order"])

    def test_unknown_condition_is_rejected(self):
        with self.assertRaises(ValueError):
            superpower_plan.route("part3", ["unapproved-change"])


if __name__ == "__main__":
    unittest.main()
