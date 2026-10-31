#!/usr/bin/env python3
"""Read-only inventory of optional Uncle Bob quality tools; does not run code analysis."""
import argparse
import json
import shutil
from pathlib import Path

TOOLS={
    'crapper':'https://github.com/unclebob/crapper',
    'dryer':'https://github.com/unclebob/dryer',
    'mutator':'https://github.com/unclebob/mutator',
}

def inspect_tools(root=None):
    base=Path(root).expanduser().resolve() if root else None
    rows={}
    for name,url in TOOLS.items():
        choices=[]
        in_path=shutil.which(name)
        if in_path:choices.append(in_path)
        if base:
            for p in (base/name/name,base/name):
                if p.is_file() and p!=base:choices.append(str(p))
        rows[name]={'installed':bool(choices),'candidates':list(dict.fromkeys(choices)),
                    'upstream':url,'measured':False}
    return rows

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--tools-root',help='Directory with separate crapper/, dryer/, mutator/ checkouts')
    ap.add_argument('--json',action='store_true')
    ns=ap.parse_args()
    data=inspect_tools(ns.tools_root)
    if ns.json:print(json.dumps(data,indent=2))
    else:
        for name,info in data.items():
            print(f'{name}: '+('candidate found' if info['installed'] else 'not found')+'; no metrics measured')
            for p in info['candidates']:print(f'  {p}')
