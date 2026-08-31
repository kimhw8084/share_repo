#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, hashlib
from pathlib import Path

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('evidence/r13_catalog_render_audit.json')); ap.add_argument('--browser',default='/usr/bin/chromium'); args=ap.parse_args()
    root=Path(__file__).resolve().parents[1]; product=root/'source/company_ui/products/visualizer'; assets=product/'assets'; core=product/'vendor/production_core/core'
    catalog=json.loads((product/'contracts/ELEMENT_CAPABILITY_MATRIX.json').read_text())['rows']
    html=(assets/'integrated_editor.html').read_text(); css=(assets/'tokens.css').read_text()+'\n'+(assets/'integrated_editor.css').read_text(); store=(core/'editor_store.mjs').read_text(); registry=(core/'runtime_registry.mjs').read_text(); renderer=(core/'universal_renderer.mjs').read_text(); er=(assets/'element_renderer.mjs').read_text(); editor=(assets/'integrated_editor.mjs').read_text()
    result={'pass':False,'elements':{},'duplicate_shapes':[],'console_errors':[],'page_errors':[]}
    blank={'schema_version':1,'items':[],'groups':{},'mode':'smart','layoutPreset':'editorial','crossFilter':None,'nextId':1}
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=args.browser,headless=True,args=['--disable-dev-shm-usage']); page=browser.new_page(viewport={'width':1440,'height':900}); page.set_default_timeout(5000)
        page.on('console',lambda m: result['console_errors'].append(m.text) if m.type=='error' else None); page.on('pageerror',lambda e: result['page_errors'].append(str(e)))
        setup=f'''<script>window.__CUI_VISUALIZER_BOOTSTRAP__={json.dumps({'report_id':'catalog','revision':1,'model':blank})};document.addEventListener('visualizer_bridge',e=>{{let m=e.detail;try{{m=typeof m==='string'?JSON.parse(m):m}}catch(_){{}}if(m?.type==='preset.preferences_requested')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'preset.preferences_result',payload:{{presets:[]}}}}),0);if(m?.type==='report.commit')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'report.commit_result',payload:{{report_id:m.payload.report_id,revision:m.payload.base_revision+1,commit_id:m.payload.commit_id}}}}),0);}});</script>'''
        page.set_content(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style>{setup}</head><body>{html}</body></html>',wait_until='domcontentloaded')
        page.evaluate("""async ({registry,store,renderer,er,editor})=>{const blob=s=>URL.createObjectURL(new Blob([s],{type:'text/javascript'}));const reg=blob(registry),st=blob(store),ren=blob(renderer.replace("'./runtime_registry.mjs'",JSON.stringify(reg)));const eurl=blob(er.replace("'../vendor/production_core/core/universal_renderer.mjs'",JSON.stringify(ren)));const patched=editor.replace("'../vendor/production_core/core/editor_store.mjs'",JSON.stringify(st)).replace("'../vendor/production_core/core/runtime_registry.mjs'",JSON.stringify(reg)).replace("'./element_renderer.mjs'",JSON.stringify(eurl));await import(blob(patched));}""",{'registry':registry,'store':store,'renderer':renderer,'er':er,'editor':editor})
        page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'")
        shapes={}
        for i,row in enumerate(catalog):
            page.evaluate("m=>window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'catalog',revision:1,model:m}})",blank)
            page.evaluate("([e,g])=>window.__VIZ_PROD__.addLibraryElement(e,g)",[row['element'],row['engine']]); page.wait_for_timeout(2)
            info=page.evaluate("""()=>{const m=window.CompanyUIVisualizerBridge.state().model,entry=m.items.at(-1),node=document.querySelector(`.component[data-id="${entry.id}"] .gallery-card`);if(!node)return{missing:true,entry};const clone=node.cloneNode(true);clone.removeAttribute('data-element');clone.removeAttribute('data-variant');clone.className=[...clone.classList].filter(c=>!c.startsWith('variant-')).join(' ');const walker=document.createTreeWalker(clone,NodeFilter.SHOW_TEXT);const texts=[];while(walker.nextNode())texts.push(walker.currentNode);for(const t of texts)if(t.nodeValue.trim())t.nodeValue='#';for(const el of clone.querySelectorAll('[style]')){const style=el.getAttribute('style')||'';el.setAttribute('style',style.replace(/[0-9.]+%/g,'N%').replace(/[0-9.]+px/g,'Npx'));}return{missing:false,element:entry.element,engine:entry.engine,variant:node.dataset.variant,text:(node.innerText||'').trim(),quality:!!node.querySelector('.quality-badge'),title_visible:!!node.querySelector('h3'),shape:clone.outerHTML};}""")
            # Visual grammars such as charts, wafer maps, layout structures and editor affordances
            # are intentionally graphic-only. A title is an author-controlled option, not required
            # content, so evaluate the rendered grammar rather than requiring incidental text.
            ok=not info.get('missing') and info.get('element')==row['element'] and info.get('engine')==row['engine'] and len(info.get('shape',''))>100 and not info.get('quality') and not info.get('title_visible')
            fp=hashlib.sha256(info.get('shape','').encode()).hexdigest()[:16] if not info.get('missing') else ''
            result['elements'][row['element']]={'pass':ok,'engine':row['engine'],'variant':info.get('variant'),'shape':fp,'text_length':len(info.get('text',''))}
            shapes.setdefault((row['engine'],fp),[]).append(row['element'])
            if (i+1)%40==0: print(f'[AUDIT] {i+1}/248',flush=True)
        result['duplicate_shapes']=[{'engine':e,'shape':fp,'elements':names} for (e,fp),names in shapes.items() if fp and len(names)>1]
        passed=sum(1 for x in result['elements'].values() if x['pass']); unique=len({x['shape'] for x in result['elements'].values() if x['shape']})
        result['summary']={'passed':passed,'total':248,'unique_normalized_shapes':unique,'duplicate_groups':len(result['duplicate_shapes'])}
        result['pass']=passed==248 and not result['console_errors'] and not result['page_errors']
        browser.close()
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,sort_keys=True));print(json.dumps({'pass':result['pass'],**result['summary'],'console_errors':result['console_errors'],'page_errors':result['page_errors']},indent=2));return 0 if result['pass'] else 1
if __name__=='__main__':raise SystemExit(main())
