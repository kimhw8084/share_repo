#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path

SIZES=(25,50,100,200)
LIMIT_MS={25:1000,50:1500,100:2500,200:5000}

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path('evidence/r14_performance_certification.json'));ap.add_argument('--browser',default='/usr/bin/chromium');args=ap.parse_args();start=time.time()
    root=Path(__file__).resolve().parents[1];product=root/'source/company_ui/products/visualizer';assets=product/'assets';core=product/'vendor/production_core/core';catalog=json.loads((product/'contracts/ELEMENT_CAPABILITY_MATRIX.json').read_text())['rows']
    html=(assets/'integrated_editor.html').read_text();css=(assets/'tokens.css').read_text()+'\n'+(assets/'integrated_editor.css').read_text();store=(core/'editor_store.mjs').read_text();registry=(core/'runtime_registry.mjs').read_text();renderer=(core/'universal_renderer.mjs').read_text();er=(assets/'element_renderer.mjs').read_text();editor=(assets/'integrated_editor.mjs').read_text();blank={'schema_version':1,'items':[],'groups':{},'mode':'smart','layoutPreset':'editorial','crossFilter':None,'nextId':1}
    result={'pass':False,'checks':{},'sizes':{},'console_errors':[],'page_errors':[]}
    def check(name,ok,detail=None):result['checks'][name]={'pass':bool(ok),'detail':detail};print(f'[PERF] {name}: {"PASS" if ok else "FAIL"} {detail if detail is not None else ""}',flush=True)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
      browser=p.chromium.launch(executable_path=args.browser,headless=True,args=['--disable-dev-shm-usage','--js-flags=--expose-gc']);page=browser.new_page(viewport={'width':1440,'height':900});page.set_default_timeout(8000)
      page.on('console',lambda m: result['console_errors'].append(m.text) if m.type=='error' else None);page.on('pageerror',lambda e:result['page_errors'].append(str(e)))
      setup=f'''<script>window.__bridgeCounts={{commit:0,total:0}};window.__CUI_VISUALIZER_BOOTSTRAP__={json.dumps({'report_id':'perf','revision':1,'model':blank})};document.addEventListener('visualizer_bridge',e=>{{window.__bridgeCounts.total++;let m=e.detail;try{{m=typeof m==='string'?JSON.parse(m):m}}catch(_){{}}if(m?.type==='report.commit'){{window.__bridgeCounts.commit++;setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'report.commit_result',payload:{{report_id:m.payload.report_id,revision:m.payload.base_revision+1,commit_id:m.payload.commit_id}}}}),0)}}if(m?.type==='preset.preferences_requested')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'preset.preferences_result',payload:{{presets:[]}}}}),0);}});</script>'''
      page.set_content(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style>{setup}</head><body style="margin:0;height:100vh">{html}</body></html>',wait_until='domcontentloaded')
      page.evaluate("""async ({registry,store,renderer,er,editor})=>{const blob=s=>URL.createObjectURL(new Blob([s],{type:'text/javascript'}));const reg=blob(registry),st=blob(store),ren=blob(renderer.replace("'./runtime_registry.mjs'",JSON.stringify(reg)));const eurl=blob(er.replace("'../vendor/production_core/core/universal_renderer.mjs'",JSON.stringify(ren)));const patched=editor.replace("'../vendor/production_core/core/editor_store.mjs'",JSON.stringify(st)).replace("'../vendor/production_core/core/runtime_registry.mjs'",JSON.stringify(reg)).replace("'./element_renderer.mjs'",JSON.stringify(eurl));await import(blob(patched));}""",{'registry':registry,'store':store,'renderer':renderer,'er':er,'editor':editor});page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'")
      # Capture representative defaults from every engine through the real insertion path.
      representatives=[]
      seen=set()
      for row in catalog:
        if row['engine'] in seen:continue
        seen.add(row['engine']);page.evaluate("m=>window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'perf',revision:1,model:m}})",blank);page.evaluate("([e,g])=>window.__VIZ_PROD__.addLibraryElement(e,g)",[row['element'],row['engine']]);page.wait_for_timeout(2);representatives.append(page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items[0]"))
      def model_for(n:int):
        items=[]
        for i in range(n):
          e=json.loads(json.dumps(representatives[i%len(representatives)]));e['id']=f'p{i+1}';e['order']=i;e['z']=i+1;e['groupId']=None;e['locked']=False;e['x']=(i%6)*195;e['y']=((i//6)%5)*125;e['w']=185;e['h']=115;items.append(e)
        return {'schema_version':1,'items':items,'groups':{},'mode':'free','layoutPreset':'editorial','crossFilter':None,'nextId':n+1}
      revision=100
      models={n:model_for(n) for n in SIZES}
      for n in SIZES:
        revision+=1;m=models[n]
        elapsed=page.evaluate("""async ([m,r])=>{const t=performance.now();window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'perf',revision:r,model:m}});await new Promise(requestAnimationFrame);await new Promise(requestAnimationFrame);return performance.now()-t}""",[m,revision])
        metrics=page.evaluate("""()=>({components:document.querySelectorAll('.component').length,dom:document.querySelectorAll('.cui-visualizer-root *').length,listenersPointer:!!window.__VIZ_PROD__.ui.pointer,bridge:window.__bridgeCounts.commit})""")
        result['sizes'][str(n)]={'render_ms':round(elapsed,2),**metrics};check(f'render_{n}',elapsed<LIMIT_MS[n],result['sizes'][str(n)]);check(f'dom_count_{n}',metrics['components']==n and metrics['dom']<60000,metrics)
      # Report switching / node reuse should not grow component count or heap without bound.
      cdp=page.context.new_cdp_session(page);cdp.send('Performance.enable');cdp.send('HeapProfiler.collectGarbage');before={x['name']:x['value'] for x in cdp.send('Performance.getMetrics')['metrics']}.get('JSHeapUsedSize',0)
      t0=time.perf_counter()
      for i in range(20):
        revision+=1;m=models[100 if i%2==0 else 200];page.evaluate("([m,r])=>window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'perf',revision:r,model:m}})",[m,revision])
      page.wait_for_timeout(80);switch_ms=(time.perf_counter()-t0)*1000;cdp.send('HeapProfiler.collectGarbage');after={x['name']:x['value'] for x in cdp.send('Performance.getMetrics')['metrics']}.get('JSHeapUsedSize',0);heap_growth=max(0,after-before)
      switch_detail={'ms':round(switch_ms,1),'components':page.locator('.component').count(),'heap_growth_mb':round(heap_growth/1024/1024,2)}
      check('report_switch_20',switch_ms<8000 and switch_detail['components']==200,switch_detail);check('heap_growth',heap_growth<64*1024*1024,switch_detail)
      # Inspector open/close loop.
      t0=time.perf_counter()
      for i in range(50):page.evaluate("open=>window.__VIZ_PROD__.setInspector(open)",bool(i%2))
      page.wait_for_timeout(80);inspector_ms=(time.perf_counter()-t0)*1000;check('inspector_toggle_50',inspector_ms<5000,round(inspector_ms,1))
      # High-frequency drag frames must not bridge to Python; only release may commit once.
      revision+=1;page.evaluate("([m,r])=>window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'perf',revision:r,model:m}})",[models[25],revision]);page.locator('[data-mode="guided"]').click();page.wait_for_timeout(30)
      first=page.locator('.component').first;first.click(force=True);head=first.locator('.c-head');box=head.bounding_box();base=page.evaluate('()=>window.__bridgeCounts.commit');page.mouse.move(box['x']+8,box['y']+8);page.mouse.down()
      for i in range(25):page.mouse.move(box['x']+10+i*2,box['y']+10+i,steps=1)
      during=page.evaluate('()=>window.__bridgeCounts.commit')-base;page.mouse.up();page.wait_for_timeout(30);released=page.evaluate('()=>window.__bridgeCounts.commit')-base
      check('drag_frames_browser_only',during==0,{'during':during,'after_release':released});check('drag_semantic_commit_max_one',released<=1,{'during':during,'after_release':released})
      # 100 undo + 100 redo operations on a small report.
      revision+=1;one=model_for(1);page.evaluate("([m,r])=>window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'perf',revision:r,model:m}})",[one,revision]);page.locator('.component').click(force=True);page.locator('[data-mode="free"]').click();page.wait_for_timeout(20)
      for _ in range(100):page.keyboard.press('ArrowRight')
      page.wait_for_timeout(40);t0=time.perf_counter()
      for _ in range(100):page.keyboard.press('Control+z')
      for _ in range(100):page.keyboard.press('Control+Shift+z')
      page.wait_for_timeout(80);undo_ms=(time.perf_counter()-t0)*1000;clean=page.evaluate("()=>({guides:+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0),pointer:!!window.__VIZ_PROD__.ui.pointer})")
      check('undo_redo_100',undo_ms<12000 and clean=={'guides':0,'pointer':False},{'ms':round(undo_ms,1),**clean})
      browser.close()
    check('no_console_errors',not result['console_errors'],result['console_errors'][:5]);check('no_page_errors',not result['page_errors'],result['page_errors'][:5]);result['pass']=all(v['pass'] for v in result['checks'].values());result['duration_seconds']=round(time.time()-start,3);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'pass':result['pass'],'checks':len(result['checks']),'duration_seconds':result['duration_seconds'],'console_errors':result['console_errors'][:5],'page_errors':result['page_errors'][:5]},indent=2));return 0 if result['pass'] else 1
if __name__=='__main__':raise SystemExit(main())
