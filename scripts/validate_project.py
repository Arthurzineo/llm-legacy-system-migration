#!/usr/bin/env python3
"""Offline checks for local documentation, category layout and installable skills."""
from pathlib import Path
import sys
from install_skills import inventory

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
    'README.md','AGENTS.md','GRAPHIFY.md','.orca/PROJECT.md','.orca/EXEC.md',
    '.orca/contracts/CONTRACT-TEMPLATE.md',
    'docs/architecture/ORCA-OPERATING-MODEL.md',
    'docs/methodology/METHODOLOGY.md',
    'docs/methodology/OUTPUT-CONTRACT.md',
    'docs/integrations/AI-MEMORY-V2.md',
    'docs/skills/SUPERPOWERS.md',
    'docs/skills/superpowers.json',
    'scripts/superpower_plan.py',
    'skills/superpowers/superpower-operational-assurance/SKILL.md',
    'docs/skills/SKILL-QUALITY-AUDIT.md',
    'docs/architecture/original-methodology.png',
    'scripts/install_skills.py','scripts/ai_memory_doctor.py',
    'scripts/configure_ai_memory_v2.sh','scripts/install_ai_memory_v2.sh',
]
CATEGORIES={'superpowers','core','migration','programming-languages','architecture','design',
            'system','testing','miscellaneous'}
PHASES=['000-foundation','001-discovery','002-characterization','003-planning',
        '004-migration','005-verification','006-cutover','007-release-readiness','008-controlled-deployment','009-operational-assurance']

def validate(root=ROOT):
    missing=[rel for rel in REQUIRED if not (root/rel).is_file()]
    if missing:raise ValueError(f'Missing files: {missing}')
    present={p.name for p in (root/'skills').iterdir() if p.is_dir()}
    if not CATEGORIES.issubset(present):raise ValueError(f'Missing skill categories: {CATEGORIES-present}')
    sk=inventory(root/'skills')
    if len(sk)<34:raise ValueError(f'Too few categorized skills: {len(sk)}')
    from superpower_plan import load_manifest
    load_manifest(root/'docs/skills/superpowers.json', sk)
    for p in PHASES:
        base=root/'.orca/phases'/p
        for rel in ['PHASE.md','tasks/README.md','diaries/README.md']:
            if not (base/rel).is_file():raise ValueError(f'Missing phase artifact: {base/rel}')
    docs=(root/'README.md').read_text(encoding='utf-8')
    if 'English' not in docs or 'single' not in docs.lower():
        raise ValueError('Repository language and single-Chief policy missing')
    if (root/'scripts/publish-private.sh').exists():
        raise ValueError('Publication script must not be bundled at this stage')
    return sk

if __name__=='__main__':
    try:
        skills=validate()
    except (OSError,ValueError) as e:
        print(f'ERROR: {e}',file=sys.stderr);sys.exit(1)
    print(f'OK: {len(skills)} categorized skills and ORCA phase documentation validated. No migration runtime was tested.')
