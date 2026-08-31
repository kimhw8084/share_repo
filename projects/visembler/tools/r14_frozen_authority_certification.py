#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, hashlib, json, os, shutil, subprocess, tempfile, time
from pathlib import Path

EXPECTED_CONNECTOR='d8ebd4378f01b7c52a7a4be57c578c22adf29b899cc08a370cf084881195343e'
PER_COMMAND_TIMEOUT=120

def hashes(root: Path):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}

def commands(vendor: Path):
    module=ast.parse((vendor/'tools/run_production_core_suite.py').read_text(encoding='utf-8'))
    for node in module.body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='COMMANDS' for t in node.targets):
            return ast.literal_eval(node.value)
    raise RuntimeError('COMMANDS not found')

def extract_json(text: str):
    text=text.strip(); start=text.find('{')
    if start < 0: return None
    depth=0; quoted=False; esc=False
    for i,ch in enumerate(text[start:],start):
        if quoted:
            if esc: esc=False
            elif ch=='\\': esc=True
            elif ch=='"': quoted=False
            continue
        if ch=='"': quoted=True
        elif ch=='{': depth += 1
        elif ch=='}':
            depth -= 1
            if depth == 0:
                try: return json.loads(text[start:i+1])
                except Exception: return None
    return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--start',type=int,default=1); ap.add_argument('--end',type=int,default=27); a=ap.parse_args()
    root=a.root.resolve(); vendor=root/'source/company_ui/products/visualizer/vendor/production_core'
    before=hashes(vendor); connector=vendor/'core/GOLDEN_CONNECTOR_ENGINE_V5_FROZEN.js'; connector_sha=hashlib.sha256(connector.read_bytes()).hexdigest()
    if connector_sha != EXPECTED_CONNECTOR: raise SystemExit(f'Golden Connector mismatch: {connector_sha}')
    results=[]; started=time.perf_counter()
    all_commands=commands(vendor)
    selected=[(idx,name,cmd) for idx,(name,cmd) in enumerate(all_commands,1) if a.start<=idx<=a.end]
    for idx,name,cmd in selected:
        with tempfile.TemporaryDirectory(prefix=f'cui-auth-{idx:02d}-') as td:
            copy=Path(td)/'production_core'; shutil.copytree(vendor,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
            env=os.environ.copy(); env.setdefault('TERM','xterm'); t0=time.perf_counter()
            try:
                cp=subprocess.run(cmd,cwd=copy,text=True,capture_output=True,env=env,timeout=PER_COMMAND_TIMEOUT)
                payload=extract_json(cp.stdout); ok=cp.returncode==0 and (payload is None or payload.get('pass',True) is True)
                row={'index':idx,'name':name,'pass':ok,'returncode':cp.returncode,'elapsed_ms':round((time.perf_counter()-t0)*1000,2),'payload':payload,'stdout_tail':cp.stdout.splitlines()[-12:],'stderr_tail':cp.stderr.splitlines()[-8:]}
            except subprocess.TimeoutExpired as exc:
                out=exc.stdout.decode() if isinstance(exc.stdout,bytes) else (exc.stdout or ''); err=exc.stderr.decode() if isinstance(exc.stderr,bytes) else (exc.stderr or '')
                row={'index':idx,'name':name,'pass':False,'returncode':124,'elapsed_ms':round((time.perf_counter()-t0)*1000,2),'timeout_seconds':PER_COMMAND_TIMEOUT,'stdout_tail':out.splitlines()[-12:],'stderr_tail':err.splitlines()[-8:]}
            results.append(row); print(f'[{idx:02d}/27] {"PASS" if row["pass"] else "FAIL"} {name} ({row["elapsed_ms"]:.0f} ms)',flush=True)
            if not row['pass']: break
    after=hashes(vendor); result={'pass':len(results)==len(selected) and all(x['pass'] for x in results) and before==after,'commands':len(results),'planned':len(selected),'range':[a.start,a.end],'isolated_per_command':True,'golden_connector_sha256':connector_sha,'vendor_files':len(before),'vendor_unchanged':before==after,'elapsed_ms':round((time.perf_counter()-started)*1000,2),'results':results}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2)); return 0 if result['pass'] else 1

if __name__=='__main__': raise SystemExit(main())
