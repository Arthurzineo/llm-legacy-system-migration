#!/usr/bin/env python3
"""Offline structural checks of synthetic examples; not legacy migration validation."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    required = ['README.md', 'GRAPHIFY.md', '.orca/PROJECT.md', 'docs/architecture/ARCHITECTURE.md',
                'schemas/evidence.schema.json', 'schemas/behavior-case.schema.json',
                'examples/evidence.example.json', 'examples/behavior-case.example.json']
    for rel in required:
        assert (root / rel).is_file(), f'Missing required file: {rel}'
    for rel in required[-4:]:
        assert isinstance(json.loads((root / rel).read_text(encoding='utf-8')), dict), rel
    evidence = json.loads((root / 'examples/evidence.example.json').read_text(encoding='utf-8'))
    case = json.loads((root / 'examples/behavior-case.example.json').read_text(encoding='utf-8'))
    assert evidence['status'] == 'unverified', 'Synthetic evidence must remain unverified'
    assert case['status'] == 'draft', 'Synthetic behavior cannot be marked observed'
    assert case['id'] in evidence['linked_tests']
    assert evidence['id'] in case['evidence_ids']
    assert not (root / 'graphify-out/graph.json').exists(), 'Do not create a fake Graphify index'
    return True

if __name__ == '__main__':
    try:
        validate()
    except (AssertionError, ValueError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
    print('OK: offline scaffolding and synthetic references are consistent; no legacy software was tested.')
