#!/usr/bin/env python3
"""Safe, category-aware Agent Skills copier; dry-run unless --apply."""
import argparse
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
SKILL_NAME = re.compile(r'^[a-z0-9][a-z0-9-]*$')

def inventory(skills_root=SKILLS):
    found = {}
    for file in sorted(skills_root.glob('*/*/SKILL.md')):
        category, folder = file.relative_to(skills_root).parts[:2]
        raw = file.read_text(encoding='utf-8')
        header = re.search(r'^name:\s*(\S+)\s*$', raw, flags=re.M)
        desc = re.search(r'^description:\s*(.+)$', raw, flags=re.M)
        if not raw.startswith('---\n') or not header or not desc:
            raise ValueError(f'Invalid skill metadata: {file}')
        name = header.group(1)
        if name != folder or not SKILL_NAME.fullmatch(name):
            raise ValueError(f'Name mismatch or unsafe skill name: {file} ({name})')
        if name in found:
            raise ValueError(f'Duplicate installable skill name: {name}')
        found[name] = (category, file)
    return found

def install(skills, target, selected=None, category=None, apply=False, force=False):
    target = Path(target).expanduser()
    actions = []
    for name, (cat, source) in sorted(skills.items()):
        if selected and name not in selected:
            continue
        if category and cat not in category:
            continue
        dest = target / name / 'SKILL.md'
        if dest.is_symlink() or (dest.parent.exists() and dest.parent.is_symlink()):
            raise ValueError(f'Symlink destination refused: {dest}')
        if dest.exists():
            if dest.read_bytes() == source.read_bytes():
                action = 'unchanged'
            elif force:
                action = 'replace'
            else:
                action = 'conflict'
        else:
            action = 'create'
        actions.append((name, cat, str(dest), action))
    for name, cat, dest, action in actions:
        print(f'{action.upper():9} {cat:23} {name:35} -> {dest}')
    if apply:
        if any(a == 'conflict' for *_, a in actions):
            raise ValueError('Existing differing skills detected; installation aborted (use --force deliberately)')
        for name, cat, dest, action in actions:
            if action in {'create', 'replace'}:
                path = Path(dest)
                path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(skills[name][1], path)
    return actions

def main(argv=None):
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--target', help='Flat skill directory; e.g. ~/.agents/skills')
    a.add_argument('--category', action='append', default=[])
    a.add_argument('--skill', action='append', default=[])
    a.add_argument('--list', action='store_true')
    a.add_argument('--apply', action='store_true')
    a.add_argument('--force', action='store_true', help='Allow explicitly replacing existing differing skills')
    ns=a.parse_args(argv)
    catalog=inventory()
    unknown=set(ns.skill)-set(catalog)
    if unknown: a.error(f'Unknown skills: {sorted(unknown)}')
    cats={c for c, _ in catalog.values()}
    if set(ns.category)-cats: a.error(f'Unknown categories: {sorted(set(ns.category)-cats)}')
    if ns.list:
        for name,(cat,file) in sorted(catalog.items()):
            print(f'{cat:23} {name}')
        return 0
    if not ns.target: a.error('--target required unless --list is used')
    try:
        result=install(catalog,ns.target,set(ns.skill),set(ns.category),ns.apply,ns.force)
    except ValueError as exc:
        print(f'ERROR: {exc}',file=sys.stderr); return 1
    print(f'{len(result)} item(s) inspected; '+('changes applied' if ns.apply else 'DRY RUN: no files changed'))
    return 0
if __name__ == '__main__':
    sys.exit(main())
