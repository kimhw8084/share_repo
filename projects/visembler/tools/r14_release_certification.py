#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys,time
from pathlib import Path

VIEWPORTS=[('desktop',1600,1000),('laptop',1440,900),('compact',1280,800)]
REPRESENTATIVE=[
 ('Hero KPI','MetricEngine'),('Metric Ring','MetricEngine'),('Metric Ladder','MetricEngine'),('Metric with Sparkline','MetricEngine'),
 ('Line Chart','CoreChartEngine'),('Clean Table','TableEngine'),('Milestone Rail','TimelineEngine'),('Process Flow','DiagramEngine'),('Image','ImageMediaEngine'),('Wafer Map','WaferFabEngine')]
THUMBS=[('Metric Ring','MetricEngine'),('Metric Ladder','MetricEngine'),('Metric with Sparkline','MetricEngine'),('Threshold Metric','MetricEngine'),('Milestone Rail','TimelineEngine'),('Process Flow','DiagramEngine'),('Clean Table','TableEngine'),('Image','ImageMediaEngine'),('Wafer Map','WaferFabEngine')]

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path('evidence/r14_release_certification.json'));ap.add_argument('--browser',default='/usr/bin/chromium');args=ap.parse_args()
    root=Path(__file__).resolve().parents[1]; product=root/'source/company_ui/products/visualizer'; assets=product/'assets'; core=product/'vendor/production_core/core'
    html=(assets/'integrated_editor.html').read_text();css=(assets/'tokens.css').read_text()+'\n'+(assets/'integrated_editor.css').read_text();store=(core/'editor_store.mjs').read_text();registry=(core/'runtime_registry.mjs').read_text();renderer=(core/'universal_renderer.mjs').read_text();er=(assets/'element_renderer.mjs').read_text();editor=(assets/'integrated_editor.mjs').read_text()
    result={'pass':False,'checks':{},'viewports':{},'console_errors':[],'page_errors':[],'started':time.time()}
    def check(name,ok,detail=None):
        result['checks'][name]={'pass':bool(ok),'detail':detail};print(f'[CHECK] {name}: {"PASS" if ok else "FAIL"}',flush=True)
        if not ok: raise AssertionError(f'{name}: {detail!r}')
    model={'schema_version':1,'items':[],'groups':{},'mode':'smart','layoutPreset':'editorial','crossFilter':None,'nextId':1}
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
      browser=p.chromium.launch(executable_path=args.browser,headless=True,args=['--disable-dev-shm-usage'])
      try:
       for label,w,h in VIEWPORTS:
        page=browser.new_page(viewport={'width':w,'height':h});page.set_default_timeout(7000)
        page.on('console',lambda msg,l=label: result['console_errors'].append(f'{l}: {msg.text}') if msg.type=='error' else None)
        page.on('pageerror',lambda err,l=label: result['page_errors'].append(f'{l}: {err}'))
        setup=f'''<script>window.__CUI_VISUALIZER_BOOTSTRAP__={json.dumps({'report_id':'r14-cert','revision':1,'model':model})};document.addEventListener('visualizer_bridge',e=>{{let m=e.detail;try{{m=typeof m==='string'?JSON.parse(m):m}}catch(_){{}}if(m?.type==='preset.preferences_requested')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'preset.preferences_result',payload:{{presets:[]}}}}),0);if(m?.type==='report.commit')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'report.commit_result',payload:{{report_id:m.payload.report_id,revision:m.payload.base_revision+1,commit_id:m.payload.commit_id}}}}),0);}});</script>'''
        page.set_content(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style>{setup}</head><body style="margin:0;height:100vh">{html}</body></html>',wait_until='domcontentloaded')
        page.evaluate("""async ({registry,store,renderer,er,editor})=>{const blob=s=>URL.createObjectURL(new Blob([s],{type:'text/javascript'}));const reg=blob(registry),st=blob(store),ren=blob(renderer.replace("'./runtime_registry.mjs'",JSON.stringify(reg)));const eurl=blob(er.replace("'../vendor/production_core/core/universal_renderer.mjs'",JSON.stringify(ren)));const patched=editor.replace("'../vendor/production_core/core/editor_store.mjs'",JSON.stringify(st)).replace("'../vendor/production_core/core/runtime_registry.mjs'",JSON.stringify(reg)).replace("'./element_renderer.mjs'",JSON.stringify(eurl));await import(blob(patched));}""",{'registry':registry,'store':store,'renderer':renderer,'er':er,'editor':editor})
        page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'")
        m0=page.evaluate("""()=>{const b=e=>{const r=e.getBoundingClientRect();return{x:r.x,y:r.y,w:r.width,h:r.height,right:r.right,bottom:r.bottom}};return{root:b(document.querySelector('.cui-visualizer-root')),viewport:b(document.querySelector('#viewport')),sceneW:document.querySelector('#scene').clientWidth,sceneH:document.querySelector('#scene').clientHeight};}""")
        check(f'{label}.standalone_viewport_fill',m0['root']['h']>=h-2,m0)
        check(f'{label}.scene_contract',m0['sceneW']==1300,m0)
        # representative semantic layout
        for e,g in REPRESENTATIVE: page.evaluate("([e,g])=>window.__VIZ_PROD__.addLibraryElement(e,g)",[e,g])
        page.wait_for_timeout(100);page.evaluate("()=>window.__VIZ_PROD__.fitZoom()");page.wait_for_timeout(80)
        pf=page.evaluate("()=>window.__VIZ_PROD__.preflight()")
        layout_codes=[x['code'] for x in pf['issues'] if x['kind']=='layout']
        check(f'{label}.smart_no_clipping','content-clipping' not in layout_codes,layout_codes)
        check(f'{label}.smart_intrinsic_min','intrinsic-minimum' not in layout_codes,layout_codes)
        check(f'{label}.smart_safe_hull','safe-hull' not in layout_codes,layout_codes)
        check(f'{label}.idle_cleanliness',page.evaluate("()=>({gv:getComputedStyle(document.querySelector('#guideV')).display,gh:getComputedStyle(document.querySelector('#guideH')).display,count:+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0),pointer:!!window.__VIZ_PROD__.ui.pointer})") == {'gv':'none','gh':'none','count':0,'pointer':False},None)
        # all visible one-line controls remain one line / no width overflow
        wraps=page.evaluate("""()=>[...document.querySelectorAll('.cui-visualizer-root button')].filter(e=>e.offsetParent!==null&&getComputedStyle(e).whiteSpace==='nowrap'&&(e.scrollWidth>e.clientWidth+1||e.scrollHeight>e.clientHeight+1)).map(e=>({id:e.id,text:e.innerText,sw:e.scrollWidth,cw:e.clientWidth,sh:e.scrollHeight,ch:e.clientHeight}))""")
        check(f'{label}.no_wrap_controls',not wraps,wraps[:10])
        # minimap and viewport containment
        geom=page.evaluate("""()=>{const b=s=>{const r=document.querySelector(s).getBoundingClientRect();return{x:r.x,y:r.y,right:r.right,bottom:r.bottom,w:r.width,h:r.height}};return{vp:b('#viewport'),mm:b('#minimap'),hull:b('#hull')}}""")
        check(f'{label}.minimap_contained',geom['mm']['x']>=geom['vp']['x']-1 and geom['mm']['right']<=geom['vp']['right']+1 and geom['mm']['y']>=geom['vp']['y']-1 and geom['mm']['bottom']<=geom['vp']['bottom']+1,geom)
        check(f'{label}.canvas_utilization',geom['hull']['w']/geom['vp']['w']>=.62 and geom['hull']['h']/geom['vp']['h']>=.50,geom)
        # command eligibility: one ungrouped, two ungrouped, grouped
        first=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items[0].id")
        page.locator(f'.component[data-id="{first}"]').click(force=True);page.wait_for_timeout(20)
        elig1=page.evaluate("()=>({group:!document.querySelector('#group').disabled,ungroup:!document.querySelector('#ungroup').disabled})")
        check(f'{label}.eligibility_one',elig1=={'group':False,'ungroup':False},elig1)
        second=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items[1].id")
        page.evaluate("id=>document.querySelector(`.component[data-id=\"${id}\"]`).dispatchEvent(new MouseEvent('click',{bubbles:true,shiftKey:true}))",second);page.wait_for_timeout(20)
        elig2=page.evaluate("()=>({group:!document.querySelector('#group').disabled,ungroup:!document.querySelector('#ungroup').disabled})")
        check(f'{label}.eligibility_multi',elig2['group'] and not elig2['ungroup'],elig2)
        page.locator('#group').click();page.wait_for_timeout(40)
        elig3=page.evaluate("()=>({group:!document.querySelector('#group').disabled,ungroup:!document.querySelector('#ungroup').disabled})")
        check(f'{label}.eligibility_grouped',not elig3['group'] and elig3['ungroup'],elig3)
        # guide torture in Guided: repeated drag, Escape cancellation, window blur cleanup
        page.locator('[data-mode="guided"]').click();page.wait_for_timeout(50)
        drag_id=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items[0].id")
        head=page.locator(f'.component[data-id="{drag_id}"] .c-head');box=head.bounding_box();
        for i in range(4):
          page.mouse.move(box['x']+8,box['y']+8);page.mouse.down();page.mouse.move(box['x']+34+i*3,box['y']+23+i*2,steps=5);page.mouse.up();page.wait_for_timeout(20)
          clean=page.evaluate("()=>({n:+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0),v:getComputedStyle(document.querySelector('#guideV')).display,h:getComputedStyle(document.querySelector('#guideH')).display,p:!!window.__VIZ_PROD__.ui.pointer})")
          check(f'{label}.guide_torture_up_{i}',clean=={'n':0,'v':'none','h':'none','p':False},clean)
        # escape during active drag
        box=head.bounding_box();page.mouse.move(box['x']+8,box['y']+8);page.mouse.down();page.mouse.move(box['x']+47,box['y']+36,steps=4);page.keyboard.press('Escape');page.mouse.up();page.wait_for_timeout(20)
        clean=page.evaluate("()=>({n:+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0),v:getComputedStyle(document.querySelector('#guideV')).display,h:getComputedStyle(document.querySelector('#guideH')).display,p:!!window.__VIZ_PROD__.ui.pointer})")
        check(f'{label}.guide_torture_escape',clean=={'n':0,'v':'none','h':'none','p':False},clean)
        page.evaluate("()=>window.dispatchEvent(new Event('blur'))");page.wait_for_timeout(10)
        check(f'{label}.guide_torture_blur',page.evaluate("()=>+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0)===0&&!window.__VIZ_PROD__.ui.pointer"),None)
        # Free mode must not show snap guides during drag.
        page.locator('[data-mode="free"]').click();page.wait_for_timeout(40);box=head.bounding_box();page.mouse.move(box['x']+8,box['y']+8);page.mouse.down();page.mouse.move(box['x']+40,box['y']+31,steps=4)
        free_guides=page.evaluate("()=>+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0)");page.mouse.up();check(f'{label}.free_no_snap_guides',free_guides==0,free_guides)
        # Smart switch must warn before destructive recomposition.
        page.locator('[data-mode="smart"]').click();page.wait_for_timeout(20);check(f'{label}.smart_switch_warn',page.locator('.modal.show').count()==1,None);page.locator('.modal.show button').filter(has_text='Recompose').click();page.wait_for_timeout(60)
        # editor zoom matrix and clean preflight
        for z in (.55,.8,1.0,1.25):
          page.evaluate("z=>window.__VIZ_PROD__.setZoom(z)",z);page.wait_for_timeout(20)
          check(f'{label}.editor_zoom_{int(z*100)}',abs(page.evaluate("()=>window.__VIZ_PROD__.ui.zoom")-z)<.011,None)
          check(f'{label}.zoom_idle_clean',page.evaluate("()=>+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0)===0"),None)
          page.evaluate("id=>document.querySelector(`.component[data-id=\"${id}\"]`).dispatchEvent(new MouseEvent('click',{bubbles:true}))",first);page.wait_for_timeout(8)
          ctx=page.evaluate("""id=>{const b=e=>{const r=e.getBoundingClientRect();return{x:r.x,y:r.y,right:r.right,bottom:r.bottom,w:r.width,h:r.height}};const c=b(document.querySelector('#context')),s=b(document.querySelector(`.component[data-id=\"${id}\"]`)),v=b(document.querySelector('#viewport'));const ix=Math.max(0,Math.min(c.right,s.right)-Math.max(c.x,s.x)),iy=Math.max(0,Math.min(c.bottom,s.bottom)-Math.max(c.y,s.y));return{c,s,v,overlap:ix*iy}}""",first)
          check(f'{label}.context_zoom_{int(z*100)}_contained',ctx['c']['x']>=ctx['v']['x']-1 and ctx['c']['right']<=ctx['v']['right']+1 and ctx['c']['y']>=ctx['v']['y']-1 and ctx['c']['bottom']<=ctx['v']['bottom']+1,ctx)
          check(f'{label}.context_zoom_{int(z*100)}_no_selected_overlap',ctx['overlap']<=1,ctx)
        # semantic library thumbnails are differentiated across the full 248-item catalog
        page.evaluate("()=>{window.__VIZ_PROD__.ui.libraryLimit=500;window.__VIZ_PROD__.renderLibrary()}")
        sigs=[]
        for e,g in THUMBS:
          sig=page.evaluate("([e,g])=>{const n=[...document.querySelectorAll('.library-item[data-element][data-engine]')].find(x=>x.dataset.element===e&&x.dataset.engine===g);return n?.querySelector('.library-thumb')?.innerHTML||''}",[e,g]);sigs.append(sig)
        check(f'{label}.library_semantic_thumbnails',len(set(sigs))==len(sigs) and all(sigs),[s[:60] for s in sigs])
        # specific metric inspector coverage
        page.evaluate("()=>window.__VIZ_PROD__.addLibraryElement('Metric Ladder','MetricEngine')");page.wait_for_timeout(30);ladder=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items.at(-1).id");page.locator(f'.component[data-id="{ladder}"]').click(force=True);page.wait_for_timeout(20)
        check(f'{label}.ladder_inspector',page.locator('#iLevels').count()==1 and page.locator('#iOrientation').count()==1,None)
        # actionable empty states (table/diagram/timeline)
        for engine,action,prop in [('TableEngine','add-row','customTable'),('DiagramEngine','add-node','nodes'),('TimelineEngine','add-event','milestones')]:
          eid=page.evaluate("eng=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.engine===eng)?.id",engine)
          if not eid: continue
          # force a true semantic empty state through the governed server-bootstrap path
          page.evaluate("""([id,eng])=>{const st=window.CompanyUIVisualizerBridge.state(),m=structuredClone(st.model),it=m.items.find(x=>x.id===id);if(eng==='DiagramEngine'){it.nodes=[];it.edges=[]}else if(eng==='TimelineEngine'){it.milestones=[]}else if(eng==='TableEngine'){it.customTable={headers:['Field','Value'],rows:[['',null]]};it.rows=[['',null]]}window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:st.report_id,revision:st.revision+1,model:m}})}""",[eid,engine]);page.wait_for_timeout(35)
          comp=page.locator(f'.component[data-id="{eid}"]');button=comp.locator(f'[data-empty-action="{action}"]')
          if button.count():
            button.click(force=True);page.wait_for_timeout(35)
            val=page.evaluate("([id,p])=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.id===id)?.[p]",[eid,prop])
            check(f'{label}.empty_action_{engine}',bool(val),val)
          else: check(f'{label}.empty_action_{engine}',False,'CTA missing')
        # source model correctness: zero remains numeric; timeline date remains null after semantic commits
        metric=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.engine==='MetricEngine').id");page.locator(f'.component[data-id="{metric}"]').click(force=True);page.wait_for_timeout(10)
        if page.locator('#iValue').count(): page.locator('#iValue').fill('0');page.locator('#iValue').press('Tab');page.wait_for_timeout(30)
        zval=page.evaluate("id=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.id===id).value",metric);check(f'{label}.zero_preserved',isinstance(zval,(int,float)) and not isinstance(zval,bool) and zval==0,zval)
        timeline=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.engine==='TimelineEngine')")
        if timeline and timeline.get('milestones'):
          check(f'{label}.timeline_null_date',timeline['milestones'][0].get('date') is None,timeline['milestones'][0])
        # browser zoom-style scale matrix via CDP pageScaleFactor is kept non-mutating; root remains clean.
        client=page.context.new_cdp_session(page)
        for scale in (.8,1.0,1.25,1.5):
          client.send('Emulation.setPageScaleFactor',{'pageScaleFactor':scale});page.wait_for_timeout(10)
          check(f'{label}.browser_scale_{int(scale*100)}',page.evaluate("()=>+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0)===0"),None)
        client.send('Emulation.setPageScaleFactor',{'pageScaleFactor':1})
        page.evaluate("()=>window.__VIZ_PROD__.fitZoom()");page.wait_for_timeout(25)
        shot=args.output.parent/'screenshots'/f'r14_{label}.png';shot.parent.mkdir(parents=True,exist_ok=True);page.screenshot(path=str(shot),full_page=True)
        result['viewports'][label]={'preflight':pf,'geometry':geom};page.close()
       check('final.no_console_errors',not result['console_errors'],result['console_errors']);check('final.no_page_errors',not result['page_errors'],result['page_errors'])
       result['pass']=all(v['pass'] for v in result['checks'].values())
      finally: browser.close()
    result['duration_seconds']=round(time.time()-result['started'],3);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'pass':result['pass'],'checks':len(result['checks']),'duration_seconds':result['duration_seconds'],'console_errors':result['console_errors'],'page_errors':result['page_errors']},indent=2));return 0 if result['pass'] else 1
if __name__=='__main__':raise SystemExit(main())
