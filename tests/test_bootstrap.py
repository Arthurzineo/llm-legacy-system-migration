import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_artifacts import validate

class BootstrapTest(unittest.TestCase):
    def test_initial_documentation(self):
        self.assertTrue(validate())

if __name__ == '__main__':
    unittest.main()
