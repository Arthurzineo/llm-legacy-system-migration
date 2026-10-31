#!/usr/bin/env python3
"""Read-only AI Memory v2.0.1 diagnostic. Never alters host or MCP client configuration."""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

PIN='2.0.1'

def diagnose(server_url='http://127.0.0.1:49374',binary='ai-memory',timeout=3):
    result={'target_version': PIN,'binary': 'missing','version': None,
            'server': 'unreachable','mcp_endpoint': 'unverified',
            'client_mcp': 'requires_in_client_memory_status_call',
            'hooks': 'requires_per_client_verification',
            'ready': False}
    path=shutil.which(binary)
    if path:
        result['binary']='available'
        try:
            proc=subprocess.run([path,'--version'],capture_output=True,text=True,timeout=timeout,check=False)
            value=(proc.stdout+' '+proc.stderr).strip()
            result['version']=value[:200]
            m=re.search(r'(?<!\d)(\d+\.\d+\.\d+)(?!\d)',value)
            result['binary']='compatible' if m and m.group(1)==PIN else 'incompatible_or_unknown'
        except (OSError, subprocess.TimeoutExpired) as e:
            result['version_error']=type(e).__name__
    parsed=urllib.parse.urlparse(server_url)
    if parsed.scheme not in ('http','https') or not parsed.netloc or parsed.username or parsed.password:
        raise ValueError('Expected an http(s) server origin without embedded credentials')
    origin=f'{parsed.scheme}://{parsed.netloc}'
    for suffix,field in [('/healthz','server'),('/mcp','mcp_endpoint')]:
        req=urllib.request.Request(origin+suffix,headers={'Accept':'application/json'})
        if os.environ.get('AI_MEMORY_AUTH_TOKEN'):
            req.add_header('Authorization','Bearer '+os.environ['AI_MEMORY_AUTH_TOKEN'])
        try:
            with urllib.request.urlopen(req,timeout=timeout) as resp:
                status=resp.status
                body=resp.read(1024).decode('utf-8','replace')
            result[field]='reachable_http_'+str(status)
            if field=='server':
                try:
                    data=json.loads(body)
                    if data.get('status')=='ok': result[field]='healthy'
                except (ValueError,AttributeError): pass
        except urllib.error.HTTPError as exc:
            result[field]='http_'+str(exc.code) # MCP GET errors often expected; not tool readiness
        except (urllib.error.URLError,TimeoutError,OSError) as exc:
            result[field]='unreachable'
    result['notes']='MCP status must be verified using memory_status inside each real agent; HTTP reachability alone is insufficient.'
    return result

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--server-url',default=os.environ.get('AI_MEMORY_SERVER_URL','http://127.0.0.1:49374'))
    ap.add_argument('--json',action='store_true')
    ap.add_argument('--timeout',type=float,default=3)
    ns=ap.parse_args(argv)
    try: data=diagnose(ns.server_url, timeout=ns.timeout)
    except ValueError as exc:
        print(f'ERROR: {exc}',file=sys.stderr);return 2
    if ns.json: print(json.dumps(data,indent=2))
    else:
        for k,v in data.items():print(f'{k}: {v}')
    return 0
if __name__=='__main__': sys.exit(main())
