#!/usr/bin/env python3
"""Preview or create empty migration output directories in a selected target project."""
import argparse
from pathlib import Path
import sys

FOLDERS = [
    'docs/legacy/static','docs/legacy/diagrams','docs/legacy/evidence','docs/legacy/rules',
    'docs/legacy/reviews','docs/legacy/characterization/environment',
    'docs/legacy/characterization/fixtures','docs/legacy/characterization/observations',
    'docs/legacy/characterization/golden-master','docs/target/adrs',
    'docs/verification/equivalence','docs/verification/quality',
    'docs/verification/security','docs/verification/release',
]

def scaffold(target:Path,apply=False):
    target=target.expanduser().resolve()
    if not target.is_dir():raise ValueError(f'Target project directory does not exist: {target}')
    result=[]
    for folder in FOLDERS:
        p=target/folder
        if p.is_symlink():raise ValueError(f'Symlink target refused: {p}')
        result.append((str(p),'exists' if p.exists() else 'create'))
    if apply:
        for p,action in result:
            if action=='create':Path(p).mkdir(parents=True,exist_ok=False)
    return result

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--target',type=Path,required=True)
    ap.add_argument('--apply',action='store_true')
    ns=ap.parse_args(argv)
    try:
        for path,status in scaffold(ns.target,ns.apply):print(f'{status.upper():6} {path}')
    except (OSError,ValueError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr);return 1
    print('Changes applied' if ns.apply else 'DRY RUN — nothing created')
    return 0
if __name__=='__main__':sys.exit(main())
