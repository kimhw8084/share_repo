#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('evidence/r12_application_browser_matrix.json')); ap.add_argument('--browser',default='/usr/bin/chromium'); args=ap.parse_args()
    root=Path(__file__).resolve().parents[1]; product=root/'source/company_ui/products/visualizer'; assets=product/'assets'; core=product/'vendor/production_core/core'
    html=(assets/'integrated_editor.html').read_text(); css=(assets/'tokens.css').read_text()+'\n'+(assets/'integrated_editor.css').read_text(); store=(core/'editor_store.mjs').read_text(); registry=(core/'runtime_registry.mjs').read_text(); renderer=(core/'universal_renderer.mjs').read_text(); element_renderer=(assets/'element_renderer.mjs').read_text(); editor=(assets/'integrated_editor.mjs').read_text()
    result={'pass':False,'checks':{},'console_errors':[],'page_errors':[]}
    def check(name, ok, detail=None):
        result['checks'][name]={'pass':bool(ok),'detail':detail}; print(f'[CHECK] {name}: {"PASS" if ok else "FAIL"}',flush=True)
        if not ok: raise AssertionError(f'{name}: {detail!r}')
    blank={'schema_version':1,'items':[],'groups':{},'mode':'smart','layoutPreset':'editorial','crossFilter':None,'nextId':1}
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=args.browser,headless=True,args=['--disable-dev-shm-usage'])
        page=browser.new_page(viewport={'width':1440,'height':1000}); page.set_default_timeout(5000)
        page.on('console',lambda msg: result['console_errors'].append(msg.text) if msg.type=='error' else None); page.on('pageerror',lambda err: result['page_errors'].append(str(err)))
        bootstrap=json.dumps({'report_id':'r12-browser','revision':1,'model':blank})
        setup=f'''<script>window.__CUI_VISUALIZER_BOOTSTRAP__={bootstrap};window.__EVENTS=[];window.__R12_FRAGMENT__={json.dumps(html)};document.addEventListener('visualizer_bridge',e=>{{let m=e.detail;try{{m=typeof m==='string'?JSON.parse(m):m}}catch(_){{}}window.__EVENTS.push(m);if(m?.type==='preset.preferences_requested')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'preset.preferences_result',payload:{{presets:[]}}}}),0);if(m?.type==='preset.preferences_save_requested')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'preset.preferences_result',payload:{{presets:m.payload.presets}}}}),0);if(m?.type==='report.commit')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'report.commit_result',payload:{{report_id:m.payload.report_id,revision:m.payload.base_revision+1,commit_id:m.payload.commit_id}}}}),0);}});</script>'''
        page.set_content(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style>{setup}</head><body style="margin:0;height:100vh">{html}</body></html>',wait_until='domcontentloaded')
        page.evaluate("""async ({registry,store,renderer,elementRenderer,editor})=>{const blob=s=>URL.createObjectURL(new Blob([s],{type:'text/javascript'}));const reg=blob(registry),st=blob(store),ren=blob(renderer.replace("'./runtime_registry.mjs'",JSON.stringify(reg)));const er=blob(elementRenderer.replace("'../vendor/production_core/core/universal_renderer.mjs'",JSON.stringify(ren)));const patched=editor.replace("'../vendor/production_core/core/editor_store.mjs'",JSON.stringify(st)).replace("'../vendor/production_core/core/runtime_registry.mjs'",JSON.stringify(reg)).replace("'./element_renderer.mjs'",JSON.stringify(er));await import(blob(patched));}""",{'registry':registry,'store':store,'renderer':renderer,'elementRenderer':element_renderer,'editor':editor})
        page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'&&window.__VIZ_PROD__")
        state=lambda:page.evaluate('()=>window.CompanyUIVisualizerBridge.state()'); model=lambda:state()['model']
        check('ready.blank',state()['editor_ready'] and len(model()['items'])==0,state())
        page.evaluate("()=>{window.__VIZ_PROD__.ui.libraryLimit=500;window.__VIZ_PROD__.renderLibrary()}")
        catalog=page.locator('#fullLibrary [data-element]').evaluate_all("els=>els.map(e=>({element:e.dataset.element,engine:e.dataset.engine}))")
        check('catalog.248',len(catalog)==248,len(catalog)); engines=sorted(set(x['engine'] for x in catalog)); check('catalog.17_engines',len(engines)==17,engines)
        reps=[('Smart Canvas','SmartLayoutEngine','#iConfiguration'),('Hero Title','TextEngine','#iText'),('Hero KPI','MetricEngine','#iValue'),('Before/After KPI','ComparisonEngine','#iBefore'),('Line Chart','CoreChartEngine','#iData'),('Clean Table','TableEngine','.table-editor-grid'),('Decision Matrix','MatrixEngine','#iMatrix'),('Event Timeline','TimelineEngine','#iTimeline'),('Process Flow','DiagramEngine','#iNodes'),('Image','ImageMediaEngine','#iImageFile'),('Evidence Card','EvidenceCompositeEngine','#iStatement'),('Decision Needed','DecisionCompositeEngine','#iStatement'),('Project Card','ProjectCompositeEngine','#iStatement'),('SPC Control Chart','EngineeringChartEngine','#iObservations'),('Wafer Map','WaferFabEngine','#iTool'),('Cross-filter','InteractionLayer','#iBehavior'),('Right Inspector','EditorInfrastructure','#iConfiguration')]
        ids={}
        for element,engine,selector in reps:
            page.evaluate("([e,g])=>window.__VIZ_PROD__.addLibraryElement(e,g)",[element,engine]); page.wait_for_timeout(10)
            entry=model()['items'][-1]; ids[engine]=entry['id']; page.locator(f'.component[data-id="{entry["id"]}"]').click(force=True); page.wait_for_timeout(5)
            check(f'inspector.{engine}',entry.get('engine')==engine and page.locator(selector).count()==1,{'element':element,'selector':selector})
        check('inspectors.17',len(ids)==17,len(ids))
        # Null-safe chart editing.
        page.locator(f'.component[data-id="{ids["CoreChartEngine"]}"]').click(force=True); page.locator('#iData').fill('A\t0\nB\t\n"C, quoted"\t12'); page.locator('#iData').dispatch_event('change'); page.wait_for_timeout(20)
        chart=next(x for x in model()['items'] if x['id']==ids['CoreChartEngine']); check('typed.zero_missing_quoted',[r[1] for r in chart['data']]==[0,None,12] and chart['data'][2][0]=='C, quoted',chart['data'])
        # Timeline null dates.
        page.locator(f'.component[data-id="{ids["TimelineEngine"]}"]').click(force=True); page.locator('#iTimeline').fill('Collect|\nAnalyze|2026-08-28\nDecide|'); page.locator('#iTimeline').dispatch_event('change'); page.wait_for_timeout(10)
        timeline=next(x for x in model()['items'] if x['id']==ids['TimelineEngine']); check('timeline.null_dates',[m['date'] for m in timeline['milestones']]==[None,'2026-08-28',None],timeline['milestones'])
        # Image paste.
        page.locator(f'.component[data-id="{ids["ImageMediaEngine"]}"]').click(force=True); page.evaluate("""()=>{const dt=new DataTransfer();dt.items.add(new File([new Uint8Array([137,80,78,71,13,10,26,10])],'paste.png',{type:'image/png'}));window.dispatchEvent(new ClipboardEvent('paste',{bubbles:true,clipboardData:dt}));}"""); page.wait_for_timeout(80)
        image=next(x for x in model()['items'] if x['id']==ids['ImageMediaEngine']); check('image.clipboard',str(image.get('src','')).startswith('data:image/png;base64,'),str(image.get('src',''))[:32])
        # Preset CRUD round-trips through semantic bridge. R14 moved naming into a save dialog.
        page.locator('#presetsTab').click(); page.locator('#presetSave').click(); page.wait_for_timeout(10); page.locator('#presetSaveName').fill('Personal A'); page.locator('#presetSaveForm').evaluate('(f)=>f.requestSubmit()'); page.wait_for_function("()=>[...document.querySelectorAll('[data-preset-rename]')].some(x=>x.value==='Personal A')"); check('preset.save',page.locator('[data-preset-rename]').filter(has=page.locator('xpath=..')).count()>=1 and page.locator('[data-preset-rename="0"]').input_value()=='Personal A',{'count':page.locator('[data-loadpreset]').count(),'text':page.locator('#presetList').inner_text()})
        rename=page.locator('[data-preset-rename="0"]'); rename.fill('Personal B'); rename.dispatch_event('change'); page.wait_for_timeout(30); check('preset.rename',page.locator('[data-preset-rename="0"]').input_value()=='Personal B',page.locator('#presetList').inner_text())
        page.locator('[data-updatepreset="0"]').click(); page.wait_for_timeout(20); check('preset.update',any(e.get('type')=='preset.preferences_save_requested' for e in page.evaluate('()=>window.__EVENTS')),None)
        page.locator('[data-deletepreset="0"]').click(); page.wait_for_timeout(30); check('preset.delete',not page.locator('[data-preset-rename]').evaluate_all("els=>els.some(x=>x.value==='Personal B')"),page.locator('#presetList').inner_text())
        check('preset.builtins',page.locator('[data-built-preset]').count()==3,page.locator('#builtinPresetList').inner_text())
        # Inspector reflow.
        width_open=page.locator('.work').bounding_box()['width']; page.locator('#inspectorClose').click(); page.wait_for_timeout(30); width_closed=page.locator('.work').bounding_box()['width']; check('inspector.collapse_reclaims_width',width_closed>width_open+150,{'open':width_open,'closed':width_closed}); page.locator('#inspectorToggle').click();
        # Preview scoped to root.
        page.locator('#previewBtn').click(); check('preview.root_scoped',page.locator('.cui-visualizer-root').evaluate("e=>e.classList.contains('preview-mode')"),None); page.locator('#previewExit').click(force=True)
        # Save/PPT semantic bridge. R14 exposes PowerPoint through the Export workflow.
        before=len(page.evaluate('()=>window.__EVENTS')); page.locator('#saveBtn').click(); page.locator('#exportBtn').click(); page.wait_for_timeout(10);
        if page.locator('#exportPptAction').is_enabled(): page.locator('#exportPptAction').click()
        else: page.keyboard.press('Escape')
        page.wait_for_timeout(10); kinds=[e.get('type') for e in page.evaluate('()=>window.__EVENTS')[before:]]; check('bridge.save_ppt','report.save_requested' in kinds and 'ppt.export_requested' in kinds,kinds); page.keyboard.press('Escape'); page.wait_for_timeout(5)
        # Controlled geometry report.
        geometry={'schema_version':1,'items':[{'id':'c1','type':'text','element':'Hero Title','engine':'TextEngine','title':'A','order':0,'weight':1,'locked':False,'z':1,'x':14,'y':14,'w':200,'h':130},{'id':'c2','type':'text','element':'Key Takeaway','engine':'TextEngine','title':'B','order':1,'weight':1,'locked':False,'z':2,'x':300,'y':14,'w':200,'h':130}],'groups':{},'mode':'guided','layoutPreset':'editorial','crossFilter':None,'nextId':3}
        page.evaluate("m=>window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'geometry',revision:1,model:m}})",geometry); page.wait_for_timeout(20)
        page.locator('.component[data-id="c2"]').click(); head=page.locator('.component[data-id="c2"] .c-head').bounding_box(); zoom=page.evaluate('()=>window.__VIZ_PROD__.ui.zoom'); page.mouse.move(head['x']+head['width']/2,head['y']+head['height']/2); page.mouse.down(); event_start=len(page.evaluate('()=>window.__EVENTS')); page.mouse.move(head['x']+head['width']/2-68*zoom,head['y']+head['height']/2,steps=8); during=page.evaluate('()=>window.__EVENTS')[event_start:]; check('pointer.no_high_frequency_bridge',not any(e.get('type')=='report.commit' for e in during),[e.get('type') for e in during]); page.mouse.up(); page.wait_for_timeout(20); moved=next(x for x in model()['items'] if x['id']=='c2'); check('guided.peer_gap',abs(moved['x']-(14+200+14))<.2,moved)
        # Free mode should keep arbitrary 5 px movement.
        page.locator('[data-mode="free"]').click(); page.wait_for_timeout(10); before=next(x for x in model()['items'] if x['id']=='c2'); head=page.locator('.component[data-id="c2"] .c-head').bounding_box(); page.mouse.move(head['x']+head['width']/2,head['y']+head['height']/2); page.mouse.down(); page.mouse.move(head['x']+head['width']/2+5*zoom,head['y']+head['height']/2+3*zoom,steps=3); page.mouse.up(); page.wait_for_timeout(10); after=next(x for x in model()['items'] if x['id']=='c2'); check('free.no_snap',abs((after['x']-before['x'])-5)<1 and abs((after['y']-before['y'])-3)<1,{'before':before,'after':after})
        # host replacement / rebind.
        page.evaluate("()=>{const old=document.querySelector('.cui-visualizer-root');const wrap=document.createElement('div');wrap.innerHTML=window.__R12_FRAGMENT__;old.replaceWith(wrap.firstElementChild);}"); page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'"); check('lifecycle.host_rebind',page.locator('#fullLibrary').count()==1 and state()['editor_ready'],state())
        check('final.no_console_errors',not result['console_errors'],result['console_errors']); check('final.no_page_errors',not result['page_errors'],result['page_errors'])
        result['pass']=all(v['pass'] for v in result['checks'].values()); browser.close()
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(result,indent=2,sort_keys=True)); print(json.dumps({'pass':result['pass'],'checks':len(result['checks']),'console_errors':result['console_errors'],'page_errors':result['page_errors']},indent=2)); return 0 if result['pass'] else 1

if __name__=='__main__': raise SystemExit(main())
