#!/usr/bin/env python3
"""Read-only status of optional Uncle Bob tools; never runs quality checks."""
import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = {
    "crapper": "https://github.com/unclebob/crapper",
    "dryer": "https://github.com/unclebob/dryer",
    "mutator": "https://github.com/unclebob/mutator",
}

def inspect_tools(root=None):
    base = Path(root).expanduser().resolve() if root else ROOT / "tools" / "third-party"
    result = {}
    for name, url in TOOLS.items():
        candidates = []
        executable = shutil.which(name)
        if executable:
            candidates.append(executable)
        for path in (base / name / name, base / name):
            if path.is_file():
                candidates.append(str(path))
        result[name] = {
            "installed": bool(candidates),
            "candidates": list(dict.fromkeys(candidates)),
            "upstream": url,
            "source_checkout": (base / name / "pyproject.toml").is_file(),
            "measured": False,
        }
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tools-root", help="Parent directory with crapper/, dryer/, mutator/")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    info = inspect_tools(args.tools_root)
    if args.json:
        print(json.dumps(info, indent=2))
    else:
        for name, status in info.items():
            print(f"{name}: {'candidate found' if status['installed'] else 'not found'}; no metrics measured")
            for path in status["candidates"]:
                print(f"  {path}")
