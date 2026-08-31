#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

VIEWPORTS=[('desktop',1600,1000),('laptop',1440,900),('compact',1280,800)]

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('evidence/r13_visual_layout_matrix.json')); ap.add_argument('--browser',default='/usr/bin/chromium'); args=ap.parse_args()
    root=Path(__file__).resolve().parents[1]; product=root/'source/company_ui/products/visualizer'; assets=product/'assets'; core=product/'vendor/production_core/core'
    html=(assets/'integrated_editor.html').read_text(); css=(assets/'tokens.css').read_text()+'\n'+(assets/'integrated_editor.css').read_text(); store=(core/'editor_store.mjs').read_text(); registry=(core/'runtime_registry.mjs').read_text(); renderer=(core/'universal_renderer.mjs').read_text(); er=(assets/'element_renderer.mjs').read_text(); editor=(assets/'integrated_editor.mjs').read_text()
    result={'pass':False,'checks':{},'viewports':{},'console_errors':[],'page_errors':[]}
    def check(name,ok,detail=None):
        result['checks'][name]={'pass':bool(ok),'detail':detail}; print(f'[CHECK] {name}: {"PASS" if ok else "FAIL"}',flush=True)
        if not ok: raise AssertionError(f'{name}: {detail!r}')
    model={'schema_version':1,'items':[],'groups':{},'mode':'smart','layoutPreset':'editorial','crossFilter':None,'nextId':1}
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=args.browser,headless=True,args=['--disable-dev-shm-usage'])
        for label,w,h in VIEWPORTS:
            page=browser.new_page(viewport={'width':w,'height':h}); page.set_default_timeout(5000)
            page.on('console',lambda msg,l=label: result['console_errors'].append(f'{l}: {msg.text}') if msg.type=='error' else None); page.on('pageerror',lambda err,l=label: result['page_errors'].append(f'{l}: {err}'))
            setup=f'''<script>window.__CUI_VISUALIZER_BOOTSTRAP__={json.dumps({'report_id':'r13-visual','revision':1,'model':model})};document.addEventListener('visualizer_bridge',e=>{{let m=e.detail;try{{m=typeof m==='string'?JSON.parse(m):m}}catch(_){{}}if(m?.type==='preset.preferences_requested')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'preset.preferences_result',payload:{{presets:[]}}}}),0);if(m?.type==='report.commit')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'report.commit_result',payload:{{report_id:m.payload.report_id,revision:m.payload.base_revision+1,commit_id:m.payload.commit_id}}}}),0);}});</script>'''
            page.set_content(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style>{setup}</head><body style="margin:0;height:100vh">{html}</body></html>',wait_until='domcontentloaded')
            page.evaluate("""async ({registry,store,renderer,er,editor})=>{const blob=s=>URL.createObjectURL(new Blob([s],{type:'text/javascript'}));const reg=blob(registry),st=blob(store),ren=blob(renderer.replace("'./runtime_registry.mjs'",JSON.stringify(reg)));const eurl=blob(er.replace("'../vendor/production_core/core/universal_renderer.mjs'",JSON.stringify(ren)));const patched=editor.replace("'../vendor/production_core/core/editor_store.mjs'",JSON.stringify(st)).replace("'../vendor/production_core/core/runtime_registry.mjs'",JSON.stringify(reg)).replace("'./element_renderer.mjs'",JSON.stringify(eurl));await import(blob(patched));}""",{'registry':registry,'store':store,'renderer':renderer,'er':er,'editor':editor})
            page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'")
            for element,engine in [('Hero KPI','MetricEngine'),('Line Chart','CoreChartEngine'),('Key Takeaway','TextEngine'),('Clean Table','TableEngine'),('Process Flow','DiagramEngine')]: page.evaluate("([e,g])=>window.__VIZ_PROD__.addLibraryElement(e,g)",[element,engine])
            page.wait_for_timeout(40); page.evaluate("()=>window.__VIZ_PROD__.fitZoom()") if page.evaluate("()=>typeof window.__VIZ_PROD__.fitZoom==='function'") else None; page.wait_for_timeout(20)
            # Select diagram to expose context controls and inspector.
            last=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items.at(-1).id"); page.locator(f'.component[data-id="{last}"]').click(force=True); page.wait_for_timeout(20)
            page.locator('#debugBtn').click(); page.wait_for_timeout(20)
            check(f'{label}.developer_console',page.locator('#debugModal.show').count()==1 and page.locator('#debugBody .debug-state').count()==1 and page.locator('#debugBody .debug-event').count()>=1,{'events':page.locator('#debugBody .debug-event').count()})
            page.locator('#debugModal [data-close]').click(); page.wait_for_timeout(10)
            metrics=page.evaluate("""()=>{const r=s=>{const e=document.querySelector(s);if(!e)return null;const b=e.getBoundingClientRect();return{x:b.x,y:b.y,w:b.width,h:b.height,right:b.right,bottom:b.bottom}};const visible=e=>{const s=getComputedStyle(e),b=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&b.width>0&&b.height>0};const chrome=[...document.querySelectorAll('.cui-visualizer-root button,.cui-visualizer-root input,.cui-visualizer-root select,.cui-visualizer-root textarea')].filter(e=>visible(e)&&!e.closest('.component')&&e.type!=='checkbox');const text=[...document.querySelectorAll('.cui-visualizer-root button,.cui-visualizer-root label,.cui-visualizer-root input,.cui-visualizer-root select,.cui-visualizer-root .section-heading,.cui-visualizer-root .inspector-section-title,.cui-visualizer-root .statusbar')].filter(e=>visible(e)&&!e.closest('.component'));return{root:r('.cui-visualizer-root'),left:r('.left'),right:r('.right'),work:r('.work'),viewport:r('#viewport'),hull:r('#hull'),minimap:r('#minimap'),context:r('#context'),minControlH:Math.min(...chrome.map(e=>e.getBoundingClientRect().height)),controlOffenders:chrome.map(e=>({tag:e.tagName,id:e.id,cls:e.className,txt:(e.innerText||e.value||'').slice(0,30),h:e.getBoundingClientRect().height})).filter(x=>x.h<32),minFont:Math.min(...text.map(e=>parseFloat(getComputedStyle(e).fontSize)||999)),fontOffenders:text.map(e=>({tag:e.tagName,id:e.id,cls:e.className,txt:(e.innerText||e.value||'').slice(0,30),font:parseFloat(getComputedStyle(e).fontSize)||999})).filter(x=>x.font<12),workScroll:document.querySelector('.work').scrollWidth-document.querySelector('.work').clientWidth,leftScroll:document.querySelector('.left').scrollWidth-document.querySelector('.left').clientWidth,rightScroll:document.querySelector('.right').scrollWidth-document.querySelector('.right').clientWidth,guideV:getComputedStyle(document.querySelector('#guideV')).display,guideH:getComputedStyle(document.querySelector('#guideH')).display,zoom:window.__VIZ_PROD__.ui.zoom};}""")
            result['viewports'][label]=metrics
            check(f'{label}.chrome_font_floor',metrics['minFont']>=12,{'min':metrics['minFont'],'offenders':metrics.get('fontOffenders')})
            # Inputs include native file input at 34-ish; 32 is hard physical minimum, primary toolbar is 36+.
            check(f'{label}.control_target_floor',metrics['minControlH']>=31.5,{'min':metrics['minControlH'],'offenders':metrics.get('controlOffenders')})
            check(f'{label}.panel_widths',metrics['left']['w']>=230 and metrics['right']['w']>=280,{'left':metrics['left']['w'],'right':metrics['right']['w']})
            check(f'{label}.no_panel_horizontal_overflow',max(metrics['workScroll'],metrics['leftScroll'],metrics['rightScroll'])<=2,{'work':metrics['workScroll'],'left':metrics['leftScroll'],'right':metrics['rightScroll']})
            check(f'{label}.canvas_utilization',metrics['hull']['w']/metrics['viewport']['w']>=.70 and metrics['hull']['h']/metrics['viewport']['h']>=.50,{'hull':metrics['hull'],'viewport':metrics['viewport'],'zoom':metrics['zoom']})
            mm,vp=metrics['minimap'],metrics['viewport']; check(f'{label}.minimap_contained',mm['x']>=vp['x']-1 and mm['right']<=vp['right']+1 and mm['y']>=vp['y']-1 and mm['bottom']<=vp['bottom']+1,{'minimap':mm,'viewport':vp})
            ctx=metrics['context']; check(f'{label}.context_contained',ctx['x']>=vp['x']-1 and ctx['right']<=vp['right']+1 and ctx['y']>=vp['y']-1 and ctx['bottom']<=vp['bottom']+1,{'context':ctx,'viewport':vp})
            check(f'{label}.guides_idle_hidden',metrics['guideV']=='none' and metrics['guideH']=='none',{'v':metrics['guideV'],'h':metrics['guideH']})
            # Inspector collapse must reclaim a meaningful amount of workspace.
            open_w=metrics['work']['w']; page.locator('#inspectorClose').click(); page.wait_for_timeout(30); closed_w=page.locator('.work').bounding_box()['width']; check(f'{label}.inspector_reflow',closed_w>=open_w+150,{'open':open_w,'closed':closed_w})
            # Double-click direct editing: text inline and chart inspector focus.
            page.locator('#inspectorToggle').click(); text_id=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.engine==='TextEngine').id"); page.locator(f'.component[data-id="{text_id}"]').dblclick(force=True); check(f'{label}.text_direct_editor',page.locator(f'.component[data-id="{text_id}"] .direct-editor-control').count()==1,None); page.locator('.direct-editor-control').fill('Edited inline'); page.locator('.direct-editor-control').press('Control+Enter'); page.wait_for_timeout(20); txt=page.evaluate("id=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.id===id).text",text_id); check(f'{label}.text_direct_commit',txt=='Edited inline',txt)
            chart_id=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.engine==='CoreChartEngine').id"); page.locator(f'.component[data-id="{chart_id}"]').dblclick(force=True); page.wait_for_timeout(80); check(f'{label}.chart_direct_focus',page.locator('#iData').evaluate('e=>document.activeElement===e'),page.evaluate('()=>document.activeElement?.id'))
            # New elements should begin with meaningful editable examples, not blank placeholders.
            chart_marks=page.locator(f'.component[data-id="{chart_id}"] svg path, .component[data-id="{chart_id}"] svg rect'); check(f'{label}.starter_chart_data',chart_marks.count()>1,{'marks':chart_marks.count()})
            table_id=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items.find(x=>x.engine==='TableEngine').id"); table_rows=page.locator(f'.component[data-id="{table_id}"] tbody tr'); check(f'{label}.starter_table_data',table_rows.count()>=2,{'rows':table_rows.count()})
            shots=args.output.parent/'screenshots'; shots.mkdir(parents=True,exist_ok=True); page.screenshot(path=str(shots/f'r13_{label}.png'),full_page=True)
            page.close()
        check('final.no_console_errors',not result['console_errors'],result['console_errors']); check('final.no_page_errors',not result['page_errors'],result['page_errors'])
        result['pass']=all(v['pass'] for v in result['checks'].values()); browser.close()
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(result,indent=2,sort_keys=True)); print(json.dumps({'pass':result['pass'],'checks':len(result['checks']),'console_errors':result['console_errors'],'page_errors':result['page_errors']},indent=2)); return 0 if result['pass'] else 1
if __name__=='__main__': raise SystemExit(main())
