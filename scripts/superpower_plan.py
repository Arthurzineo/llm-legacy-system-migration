#!/usr/bin/env python3
"""Validate and preview five user-facing ORCA superpower routes (read-only).

This program does not execute agent skills, call a model, start an agent,
install tools, or authorize a phase. Agents must read the selected SKILL.md
and use their real runtime's capabilities under the relevant ORCA contract.
"""
import argparse
import json
from pathlib import Path
import sys
from install_skills import inventory

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/skills/superpowers.json'
EXPECTED = {'orca', 'part1', 'part1.1', 'part2', 'part3'}


def load_manifest(path=MANIFEST, catalog=None):
    path = Path(path)
    obj = json.loads(path.read_text(encoding='utf-8'))
    if obj.get('schema_version') not in (1, 2):
        raise ValueError('Unsupported routing schema')
    entries = obj.get('entrypoints')
    if not isinstance(entries, list) or len(entries) != 5:
        raise ValueError('Exactly five superpowers are required')
    ids = [e['id'] for e in entries]
    if set(ids) != EXPECTED or len(set(ids)) != len(ids):
        raise ValueError(f'Superpower IDs mismatch: {ids}')
    catalog = inventory(ROOT/'skills') if catalog is None else catalog
    aliases = set()
    for entry in entries:
        if entry.get('skill') not in catalog:
            raise ValueError(f'Superpower entry file is missing: {entry["id"]}')
        if entry['skill'] not in [name for name, (cat, _) in catalog.items() if cat == 'superpowers']:
            raise ValueError(f'Entrypoint must be in skills/superpowers/: {entry["skill"]}')
        for alias in [entry['id'], *entry.get('aliases', [])]:
            if alias in aliases:
                raise ValueError(f'Duplicate alias: {alias}')
            aliases.add(alias)
        if not isinstance(entry.get('required'), list) or not entry['required']:
            raise ValueError(f'No required skills: {entry["id"]}')
        if 'orca-project-entry' not in entry['required']:
            raise ValueError(f'Missing ORCA project entry: {entry["id"]}')
        all_skills = entry['required'] + [s for seq in entry.get('conditional', {}).values() for s in seq]
        for skill in all_skills:
            if skill not in catalog:
                raise ValueError(f'Unknown routed skill: {skill} in {entry["id"]}')
            if skill.startswith('superpower-'):
                raise ValueError('Superpowers cannot be silently dispatched as ordinary child skills')
        for next_phase in entry.get('next', []):
            if next_phase not in EXPECTED:
                raise ValueError(f'Unknown handoff: {next_phase}')
    return entries


def route(stage, conditions=(), decision=None, manifest=MANIFEST):
    entries = load_manifest(manifest)
    selected = next((e for e in entries if stage in [e['id'], *e.get('aliases', [])]), None)
    if selected is None:
        raise ValueError(f'Unknown stage: {stage}')
    options = selected.get('conditional', {})
    bad = set(conditions)-set(options)
    if bad:
        raise ValueError(f'Unknown conditions for {selected["id"]}: {sorted(bad)}')
    if selected['id'] != 'part1.1' and decision is not None:
        raise ValueError('--decision is only applicable to part1.1')
    if selected['id'] == 'part1.1':
        if decision not in (None, 'YES', 'NO', 'DEFER'):
            raise ValueError('Decision must be YES, NO or DEFER')
        if 'decision-yes' in conditions and decision != 'YES':
            raise ValueError('decision-yes requires --decision YES')
        if decision in ('NO', 'DEFER'):
            conditions = []
        if decision == 'YES' and 'decision-yes' not in conditions:
            conditions = [*conditions, 'decision-yes']
    effective = list(dict.fromkeys([*selected['required'], *(skill for key in conditions for skill in options[key])]))
    return {
        'stage': selected['id'],
        'name': selected['name'],
        'superpower': selected['skill'],
        'decision': decision if selected['id'] == 'part1.1' else None,
        'approval_required': selected['id'] == 'part1.1' and decision is None,
        'skills_to_read_in_order': effective,
        'available_conditions': list(options),
        'next': selected['next'],
        'notice': 'Read-only plan. No agent dispatch, tool execution, or consent is implied.'
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--list', action='store_true', help='List the five user-facing superpowers')
    ap.add_argument('--stage', help='Superpower ID or alias, e.g. part1.1')
    ap.add_argument('--condition', action='append', default=[], help='Opt in to a contextual skill group')
    ap.add_argument('--decision', choices=['YES', 'NO', 'DEFER'], help='Part 1.1 user decision (not authorization to run software)')
    ap.add_argument('--json', action='store_true', help='Machine-readable preview')
    ns = ap.parse_args(argv)
    try:
        entries = load_manifest()
        if ns.list:
            for e in entries:
                print(f'{e["id"]:8s} {e["skill"]:38s} {e["name"]}')
            return 0
        if not ns.stage:
            ap.error('Specify --list or --stage')
        result = route(ns.stage, ns.condition, ns.decision)
        if ns.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f'{result["name"]} -> {result["superpower"]}')
            if result['approval_required']:
                print('CHIEF MUST ASK: YES / NO / DEFER before dynamic characterization.')
            if result['decision'] in ('NO', 'DEFER'):
                print(f'Decision: {result["decision"]}; record only. Do not execute dynamic characterization.')
            for n, skill in enumerate(result['skills_to_read_in_order'], 1):
                print(f'  {n:02d}. Read skill: {skill}')
            print(f'Next potential superpower(s): {", ".join(result["next"]) or "none"}')
            print(result['notice'])
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
