#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, hashlib, json, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

EXPECTED_CONNECTOR='d8ebd4378f01b7c52a7a4be57c578c22adf29b899cc08a370cf084881195343e'
PER_COMMAND_TIMEOUT=60

def tree_hashes(root:Path):
    return {p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}

def frozen_commands(copy:Path):
    runner=copy/'tools/run_production_core_suite.py'
    module=ast.parse(runner.read_text(encoding='utf-8'))
    for node in module.body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='COMMANDS' for t in node.targets):
            return ast.literal_eval(node.value)
    raise RuntimeError('Frozen production suite COMMANDS list not found')

def extract_json(text:str):
    text=text.strip(); start=text.find('{')
    if start<0:return None
    depth=0; ins=False; esc=False
    for i,ch in enumerate(text[start:],start):
        if ins:
            if esc:esc=False
            elif ch=='\\':esc=True
            elif ch=='"':ins=False
            continue
        if ch=='"':ins=True
        elif ch=='{':depth+=1
        elif ch=='}':
            depth-=1
            if depth==0:
                try:return json.loads(text[start:i+1])
                except Exception:return None
    return None

def run_one(copy:Path,index:int,name:str,cmd:list[str]):
    t0=time.perf_counter(); env=os.environ.copy(); env.setdefault('TERM','xterm')
    try:
        cp=subprocess.run(cmd,cwd=copy,text=True,capture_output=True,env=env,timeout=PER_COMMAND_TIMEOUT)
        payload=extract_json(cp.stdout)
        passed=cp.returncode==0 and (payload is None or payload.get('pass',True) is True)
        return {'index':index,'name':name,'pass':passed,'returncode':cp.returncode,'elapsed_ms':round((time.perf_counter()-t0)*1000,2),'payload':payload,'stdout_tail':cp.stdout.splitlines()[-16:],'stderr_tail':cp.stderr.splitlines()[-10:]}
    except subprocess.TimeoutExpired as e:
        out=e.stdout.decode() if isinstance(e.stdout,bytes) else (e.stdout or '')
        err=e.stderr.decode() if isinstance(e.stderr,bytes) else (e.stderr or '')
        return {'index':index,'name':name,'pass':False,'returncode':124,'elapsed_ms':round((time.perf_counter()-t0)*1000,2),'timeout_seconds':PER_COMMAND_TIMEOUT,'stdout_tail':out.splitlines()[-16:],'stderr_tail':err.splitlines()[-10:]}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument('--output',type=Path); a=ap.parse_args()
    vendor=a.root/'source/company_ui/products/visualizer/vendor/production_core'
    before=tree_hashes(vendor)
    connector=vendor/'core/GOLDEN_CONNECTOR_ENGINE_V5_FROZEN.js'
    connector_sha=hashlib.sha256(connector.read_bytes()).hexdigest()
    if connector_sha!=EXPECTED_CONNECTOR: raise SystemExit(f'Golden Connector identity mismatch: {connector_sha}')
    results=[]; t0=time.perf_counter()
    with tempfile.TemporaryDirectory(prefix='cui-viz-authority-') as td:
        copy=Path(td)/'production_core'; shutil.copytree(vendor,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        commands=frozen_commands(copy)
        # Chromium can leave transient resources after the 248-browser gate on some hosts.
        # Run the connector benchmark first, then every remaining frozen command in canonical order.
        order=[len(commands)-1]+list(range(len(commands)-1))
        for pos in order:
            name,cmd=commands[pos]
            r=run_one(copy,pos+1,name,cmd); results.append(r)
            print(f'[{pos+1:02d}/{len(commands)}] {"PASS" if r["pass"] else "FAIL"} {name} ({r["elapsed_ms"]:.0f} ms)',flush=True)
            if not r['pass']: break
    after=tree_hashes(vendor); unchanged=before==after
    results=sorted(results,key=lambda x:x['index'])
    planned=27
    passed=len(results)==planned and all(r['pass'] for r in results)
    result={'pass':passed and unchanged,'commands':len(results),'planned':planned,'execution_order':'diagram_connector_benchmark first; remaining frozen commands canonical order','golden_connector_sha256':connector_sha,'vendor_files':len(before),'vendor_unchanged':unchanged,'elapsed_ms':round((time.perf_counter()-t0)*1000,2),'results':results}
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2))
    return 0 if result['pass'] else 1
if __name__=='__main__': raise SystemExit(main())
