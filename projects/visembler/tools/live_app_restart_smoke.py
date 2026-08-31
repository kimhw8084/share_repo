#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, signal, socket, subprocess, sys, tempfile, time, urllib.error, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def free_port():
    with socket.socket() as s: s.bind(('127.0.0.1',0)); return s.getsockname()[1]

def browser_path():
    configured=os.getenv('COMPANY_UI_BROWSER')
    candidates=[configured,'/usr/bin/chromium','/usr/bin/google-chrome','/usr/bin/google-chrome-stable','/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']
    for p in candidates:
        if p and Path(p).is_file() and os.access(p,os.X_OK): return p
    import shutil
    for name in ('chromium','chromium-browser','google-chrome','google-chrome-stable'):
        found=shutil.which(name)
        if found:return found
    return None

def wait_http(url, timeout=20):
    deadline=time.monotonic()+timeout; last=None
    while time.monotonic()<deadline:
        try:
            with urllib.request.urlopen(url,timeout=1) as response:
                if response.status<500:return response.status
        except Exception as exc: last=exc
        time.sleep(.1)
    raise RuntimeError(f'server did not become ready at {url}: {last}')

def start_server(work:Path, data:Path, port:int, log:Path):
    env=os.environ.copy(); env.update({'COMPANY_UI_ENVIRONMENT':'dev','COMPANY_UI_HOST':'127.0.0.1','COMPANY_UI_PORT':str(port),'COMPANY_UI_VISUALIZER_DATA_DIR':str(data),'PYTHONUNBUFFERED':'1'})
    env.pop('COMPANY_UI_STORAGE_SECRET',None)
    handle=log.open('w',encoding='utf-8')
    proc=subprocess.Popen([sys.executable,str(ROOT/'app.py')],cwd=work,env=env,stdout=handle,stderr=subprocess.STDOUT,start_new_session=True)
    return proc,handle,env

def stop_server(proc,handle,timeout=12):
    if proc.poll() is None:
        proc.send_signal(signal.SIGTERM)
        try: proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill(); proc.wait(timeout=5)
    handle.flush(); handle.close(); return proc.returncode

def report_snapshot(data:Path):
    files=sorted((data/'reports').glob('*.json'))
    if not files:return None
    values=[]
    for p in files:
        try: values.append(json.loads(p.read_text()))
        except Exception: continue
    if not values:return None
    return max(values,key=lambda x:int(x.get('revision',0)))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=ROOT/'evidence/r12_live_restart_smoke.json'); a=ap.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(json.dumps({'pass':False,'failures':[f'Playwright import failed: {exc}']},indent=2)); return 1
    browser=browser_path()
    if not browser:
        print(json.dumps({'pass':False,'failures':['Chrome/Chromium executable not found']},indent=2)); return 1
    port=free_port(); failures=[]; http_errors=[]; console_errors=[]; page_errors=[]; evidence={}
    with tempfile.TemporaryDirectory(prefix='cui-r12-live-') as td:
        base_dir=Path(td); work=base_dir/'cwd'; work.mkdir(); data=base_dir/'data'; data.mkdir(); base=f'http://127.0.0.1:{port}'
        proc,h,env=start_server(work,data,port,base_dir/'server1.log')
        try:
            wait_http(base+'/healthz')
            secret=(data/'.storage_secret').read_text().strip(); evidence['generated_secret_length']=len(secret)
            if len(secret)<32: failures.append('generated local storage secret is too short')
            with sync_playwright() as pw:
                b=pw.chromium.launch(executable_path=browser,headless=True,args=['--disable-dev-shm-usage'])
                context=b.new_context(); page=context.new_page(); page.set_default_timeout(8000)
                page.on('console',lambda m: console_errors.append(m.text) if m.type=='error' else None)
                page.on('pageerror',lambda e: page_errors.append(str(e)))
                page.on('response',lambda r: http_errors.append({'url':r.url,'status':r.status}) if r.url.startswith(base) and r.status>=400 else None)
                page.goto(base+'/visualizer',wait_until='domcontentloaded'); page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'")
                initial=page.evaluate('()=>window.CompanyUIVisualizerBridge.state()'); evidence['initial_revision']=initial['revision']
                page.evaluate("()=>window.__VIZ_PROD__.addLibraryElement('Hero KPI','MetricEngine')")
                page.wait_for_function("()=>window.CompanyUIVisualizerBridge.state().pending===0")
                deadline=time.monotonic()+5; first=None
                while time.monotonic()<deadline:
                    first=report_snapshot(data)
                    if first and len(first.get('model',{}).get('items',[]))>=1 and int(first.get('revision',0))>int(initial['revision']): break
                    time.sleep(.05)
                if not first or not first.get('model',{}).get('items'): failures.append('semantic report edit did not persist to repository')
                else: evidence['persisted_revision_before_restart']=first['revision']
                page.locator('#presetName').fill('Restart Persistence Preset'); page.locator('#presetSave').click()
                page.wait_for_function("()=>[...document.querySelectorAll('#presetList [data-preset-rename]')].some(e=>e.value==='Restart Persistence Preset')")
                # ensure server round trip happened, not merely local cache
                page.wait_for_timeout(250)
                rc1=stop_server(proc,h); evidence['first_shutdown_returncode']=rc1
                if rc1 not in (0,None): failures.append(f'first server shutdown was not clean: rc={rc1}')
                # Same working directory + data directory + browser context; app must reuse the local secret.
                proc,h,env=start_server(work,data,port,base_dir/'server2.log'); wait_http(base+'/healthz')
                secret2=(data/'.storage_secret').read_text().strip(); evidence['secret_reused']=secret2==secret
                if secret2!=secret: failures.append('local storage secret changed across restart')
                page.goto(base+'/visualizer',wait_until='domcontentloaded'); page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'")
                page.wait_for_function("()=>window.CompanyUIVisualizerBridge.state().model.items.length>=1")
                page.wait_for_function("()=>[...document.querySelectorAll('#presetList [data-preset-rename]')].some(e=>e.value==='Restart Persistence Preset')")
                after=page.evaluate('()=>window.CompanyUIVisualizerBridge.state()'); evidence['revision_after_restart']=after['revision']; evidence['items_after_restart']=len(after['model']['items'])
                evidence['preset_after_restart']=page.locator('#presetList [data-preset-rename="0"]').input_value()
                context.close(); b.close()
        except Exception as exc:
            failures.append(f'{type(exc).__name__}: {exc}')
        finally:
            if proc.poll() is None:
                rc2=stop_server(proc,h); evidence['second_shutdown_returncode']=rc2
                if rc2 not in (0,None): failures.append(f'second server shutdown was not clean: rc={rc2}')
            elif not h.closed: h.close()
        for name in ('server1.log','server2.log'):
            p=base_dir/name
            if p.is_file():
                text=p.read_text(errors='replace'); evidence[name+'_tail']=text.splitlines()[-80:]
                if 'Traceback (most recent call last)' in text: failures.append(f'unexpected traceback in {name}')
    if http_errors: failures.append(f'same-origin HTTP errors: {http_errors[:20]}')
    if console_errors: failures.append(f'browser console errors: {console_errors[:20]}')
    if page_errors: failures.append(f'browser page errors: {page_errors[:20]}')
    result={'pass':not failures,'failures':failures,'http_errors':http_errors,'console_errors':console_errors,'page_errors':page_errors,'evidence':evidence}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({'pass':result['pass'],'failures':failures,'evidence':{k:v for k,v in evidence.items() if not k.endswith('_tail')}},indent=2)); return 0 if result['pass'] else 1
if __name__=='__main__': raise SystemExit(main())
