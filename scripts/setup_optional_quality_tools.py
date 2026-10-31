#!/usr/bin/env python3
"""Inspect optional Uncle Bob tools and languages; opt-in submodule checkout/install."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TOOL_COMMITS = {
    "crapper": "6fd92c4c9bcc56efb64a2f8743d5a2993bcfd42d",
    "dryer": "66ff6d21a42c04afcad89c78a80066176d1294b0",
    "mutator": "a5a0cb803b66e0cdb8bf471b3b08af701d424a41",
}
SUPPORTED_SUFFIXES = {
    ".clj": "Clojure", ".cljc": "Clojure",
    ".java": "Java", ".go": "Go", ".py": "Python",
    ".js": "JavaScript", ".jsx": "JavaScript", ".mjs": "JavaScript",
    ".cjs": "JavaScript", ".ts": "TypeScript", ".tsx": "TypeScript",
    ".rs": "Rust",
}
KNOWN_OTHER_SUFFIXES = {
    ".php": "PHP", ".cob": "COBOL", ".cbl": "COBOL",
    ".c": "C", ".cc": "C++", ".cpp": "C++", ".h": "C/C++",
    ".cs": "C#", ".rb": "Ruby", ".swift": "Swift", ".kt": "Kotlin",
}
IGNORE_DIRS = {
    ".git", ".venv", "venv", "node_modules", "vendor", "target",
    "dist", "build", ".orca", "tools", "docs", "__pycache__", ".next",
}

def language_inventory(target):
    counts = {}
    for directory, dirs, files in os.walk(target, followlinks=False):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS
                   and not (Path(directory) / d).is_symlink()]
        for filename in files:
            ext = Path(filename).suffix.lower()
            language = SUPPORTED_SUFFIXES.get(ext) or KNOWN_OTHER_SUFFIXES.get(ext)
            if language:
                counts[language] = counts.get(language, 0) + 1
    return {
        "supported": {k: v for k, v in sorted(counts.items())
                      if k in SUPPORTED_SUFFIXES.values()},
        "unsupported": {k: v for k, v in sorted(counts.items())
                        if k not in SUPPORTED_SUFFIXES.values()},
        "method": "source filename extensions only; runtime compatibility not confirmed",
    }

def installed_tools():
    result = {}
    for name, expected in TOOL_COMMITS.items():
        directory = ROOT / "tools" / "third-party" / name
        proc = subprocess.run(
            ["git", "-C", str(directory), "rev-parse", "HEAD"],
            text=True, capture_output=True, check=False
        ) if (directory / "pyproject.toml").exists() else None
        actual = proc.stdout.strip() if proc and proc.returncode == 0 else None
        result[name] = {
            "path": str(directory.relative_to(ROOT)),
            "expected_sha": expected,
            "actual_sha": actual,
            "source_ready": actual == expected,
            "prepared": (directory / ".venv" / "pyvenv.cfg").exists(),
        }
    return result

def execute_checked(cmd, cwd):
    subprocess.run(cmd, cwd=cwd, check=True)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=str(ROOT), help="Source repository to inspect")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--install", action="store_true",
                        help="Explicitly initialize the pinned Git submodules")
    parser.add_argument("--prepare", action="store_true",
                        help="Explicitly create venvs and install upstream dependencies")
    ns = parser.parse_args(argv)
    target = Path(ns.target).expanduser().resolve()
    if not target.is_dir():
        parser.error("Target is not an existing directory")
    try:
        if ns.install:
            if not (ROOT / ".git").exists():
                raise RuntimeError("A Git checkout is required for submodule installation")
            paths = [f"tools/third-party/{name}" for name in TOOL_COMMITS]
            execute_checked(["git", "submodule", "update", "--init", *paths], ROOT)
        if ns.prepare:
            for name in TOOL_COMMITS:
                directory = ROOT / "tools" / "third-party" / name
                entry = installed_tools()[name]
                if not entry["source_ready"]:
                    raise RuntimeError(f"{name}: initialize and verify pinned submodule first")
                venv = directory / ".venv"
                if not (venv / "pyvenv.cfg").exists():
                    execute_checked([sys.executable, "-m", "venv", str(venv)], ROOT)
                python = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
                execute_checked([str(python), "-m", "pip", "install", "-e", "."], directory)
    except (OSError, subprocess.CalledProcessError, RuntimeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    result = {
        "target": str(target),
        "languages": language_inventory(target),
        "tools": installed_tools(),
        "tool_execution_performed": False,
        "note": "Language detection and source preparation are not quality measurements.",
    }
    if ns.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Language inventory: {result['languages']}")
        for name, status in result["tools"].items():
            print(f"{name}: {'pinned checkout ready' if status['source_ready'] else 'not ready'}")
        print(result["note"])
    return 0

if __name__ == "__main__":
    sys.exit(main())
