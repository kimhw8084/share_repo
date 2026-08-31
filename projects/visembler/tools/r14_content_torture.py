#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path

LONG='A production-ready descriptive label with meaningful operational context and enough content to exercise wrapping without becoming pathological'

def mutate(entry:dict,variant:str)->dict:
    e=json.loads(json.dumps(entry)); eng=e.get('engine',''); e['title']=e.get('element','Element') if variant!='long' else f"{e.get('element','Element')} — {LONG}"
    if variant=='long':
        if eng=='MetricEngine': e.update(value=123456.789,unit='hours per production year',delta=12.34,target=150000,detail=True,context=LONG,interpretation='High confidence with review context',levels=[['Maximum expected band',100],['Operational median band',62],['Lower observation band',25]],series=[10,18,13,27,24,39,31,47])
        elif eng=='ComparisonEngine': e.update(before=123456.78,after=98765.43,unit='units per reporting period')
        elif eng=='TextEngine': e.update(text=(LONG+'. ')*3,body=(LONG+'. ')*3)
        elif eng=='CoreChartEngine':
            rows=[{'label':f'Long category label {i} for operational evidence', 'value':i*13.5} for i in range(1,13)]; e.update(rows=rows,data=[[r['label'],r['value']] for r in rows],brush=[0,len(rows)-1])
        elif eng=='TableEngine': e.update(customTable={'headers':['Operational evidence dimension','Current observed measurement','Governed target threshold','Interpretation'], 'rows':[[f'Long evidence row {i}',i*10.25,i*11.5,LONG[:70]] for i in range(1,9)]},rows=[])
        elif eng=='MatrixEngine': e['matrix']=[[r*10+c for c in range(6)] for r in range(6)]
        elif eng=='TimelineEngine': e.update(milestones=[{'label':f'Long milestone {i} — governed sequence context','date':None} for i in range(1,7)],tm=0)
        elif eng=='DiagramEngine':
            nodes=[f'Long process node {i} context' for i in range(1,7)]; e.update(nodes=nodes,edges=[[nodes[i],nodes[i+1]] for i in range(len(nodes)-1)])
        elif eng=='ImageMediaEngine': e.update(src='',alt=LONG,caption=LONG,focal='50% 50%')
        elif eng in {'EvidenceCompositeEngine','DecisionCompositeEngine','ProjectCompositeEngine'}: e.update(statement=LONG,detail=(LONG+'. ')*2,status='Requires cross-functional review')
        elif eng=='EngineeringChartEngine': e.update(observations=[{'label':f'Observation {i}', 'value':50+(i%7)*2.5} for i in range(1,17)],role='measurement',lower_limit=40,upper_limit=70,lcl=44,ucl=68)
        elif eng=='WaferFabEngine': e.update(observations=[{'x':i%5,'y':i//5,'value':(i*7)%100} for i in range(25)],tool='ETCH-TOOL-LONG-NAME',chamber='CHAMBER-04',lot='LOT-2026-LONG',route='ROUTE-OPERATIONAL-CONTEXT')
        elif eng=='SmartLayoutEngine': e['configuration']=LONG
        elif eng=='InteractionLayer': e['behavior']=LONG
        elif eng=='EditorInfrastructure': e['configuration']=LONG
    elif variant=='zero':
        if eng=='MetricEngine': e.update(value=0,delta=0,target=0,max=0,current=0,capacity=0,numerator=0,denominator=0,warning=0,critical=0,actual=0,variance=0,confidence=0,series=[0,0,0])
        elif eng=='ComparisonEngine': e.update(before=0,after=0)
        elif eng=='CoreChartEngine': e.update(rows=[{'label':'Zero','value':0}],data=[['Zero',0]],brush=[0,0])
        elif eng=='TableEngine': e.update(customTable={'headers':['Field','Value'],'rows':[['Zero',0]]},rows=[['Zero',0]])
        elif eng=='MatrixEngine': e['matrix']=[[0,0],[0,0]]
        elif eng=='TimelineEngine': e.update(milestones=[{'label':'Sequence zero','date':None}],tm=0)
        elif eng=='EngineeringChartEngine': e['observations']=[{'label':'0','value':0}]
        elif eng=='WaferFabEngine': e['observations']=[{'x':0,'y':0,'value':0}]
    elif variant=='empty':
        if eng=='MetricEngine': e.update(value=None,delta=None,target=None,unit='')
        elif eng=='ComparisonEngine': e.update(before=None,after=None,unit='')
        elif eng=='TextEngine': e.update(text='',body='')
        elif eng=='CoreChartEngine': e.update(rows=[],data=[],brush=[0,0])
        elif eng=='TableEngine': e.update(customTable={'headers':['Field','Value'],'rows':[['',None]]},rows=[['',None]])
        elif eng=='MatrixEngine': e['matrix']=[[None,None],[None,None]]
        elif eng=='TimelineEngine': e.update(milestones=[],tm=0)
        elif eng=='DiagramEngine': e.update(nodes=[],edges=[])
        elif eng=='ImageMediaEngine': e.update(src='',alt='',caption='')
        elif eng in {'EvidenceCompositeEngine','DecisionCompositeEngine','ProjectCompositeEngine'}: e.update(statement='',detail='',status='')
        elif eng in {'EngineeringChartEngine','WaferFabEngine'}: e['observations']=[]
    return e

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path('evidence/r14_content_torture.json'));ap.add_argument('--browser',default='/usr/bin/chromium');args=ap.parse_args();start=time.time()
    root=Path(__file__).resolve().parents[1];product=root/'source/company_ui/products/visualizer';assets=product/'assets';core=product/'vendor/production_core/core';catalog=json.loads((product/'contracts/ELEMENT_CAPABILITY_MATRIX.json').read_text())['rows']
    html=(assets/'integrated_editor.html').read_text();css=(assets/'tokens.css').read_text()+'\n'+(assets/'integrated_editor.css').read_text();store=(core/'editor_store.mjs').read_text();registry=(core/'runtime_registry.mjs').read_text();renderer=(core/'universal_renderer.mjs').read_text();er=(assets/'element_renderer.mjs').read_text();editor=(assets/'integrated_editor.mjs').read_text();blank={'schema_version':1,'items':[],'groups':{},'mode':'smart','layoutPreset':'editorial','crossFilter':None,'nextId':1}
    result={'pass':False,'variants':['normal','long','zero','empty'],'elements':{},'failures':[],'console_errors':[],'page_errors':[]}
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
      browser=p.chromium.launch(executable_path=args.browser,headless=True,args=['--disable-dev-shm-usage']);page=browser.new_page(viewport={'width':1440,'height':900});page.set_default_timeout(6000)
      page.on('console',lambda m: result['console_errors'].append(m.text) if m.type=='error' else None);page.on('pageerror',lambda e:result['page_errors'].append(str(e)))
      setup=f'''<script>window.__CUI_VISUALIZER_BOOTSTRAP__={json.dumps({'report_id':'torture','revision':1,'model':blank})};document.addEventListener('visualizer_bridge',e=>{{let m=e.detail;try{{m=typeof m==='string'?JSON.parse(m):m}}catch(_){{}}if(m?.type==='preset.preferences_requested')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'preset.preferences_result',payload:{{presets:[]}}}}),0);if(m?.type==='report.commit')setTimeout(()=>window.CompanyUIVisualizerBridge?.receive({{bridge_version:1,type:'report.commit_result',payload:{{report_id:m.payload.report_id,revision:m.payload.base_revision+1,commit_id:m.payload.commit_id}}}}),0);}});</script>'''
      page.set_content(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style>{setup}</head><body style="margin:0;height:100vh">{html}</body></html>',wait_until='domcontentloaded')
      page.evaluate("""async ({registry,store,renderer,er,editor})=>{const blob=s=>URL.createObjectURL(new Blob([s],{type:'text/javascript'}));const reg=blob(registry),st=blob(store),ren=blob(renderer.replace("'./runtime_registry.mjs'",JSON.stringify(reg)));const eurl=blob(er.replace("'../vendor/production_core/core/universal_renderer.mjs'",JSON.stringify(ren)));const patched=editor.replace("'../vendor/production_core/core/editor_store.mjs'",JSON.stringify(st)).replace("'../vendor/production_core/core/runtime_registry.mjs'",JSON.stringify(reg)).replace("'./element_renderer.mjs'",JSON.stringify(eurl));await import(blob(patched));}""",{'registry':registry,'store':store,'renderer':renderer,'er':er,'editor':editor});page.wait_for_function("()=>document.querySelector('.cui-visualizer-root')?.dataset.editorReady==='true'")
      revision=10
      for idx,row in enumerate(catalog,1):
        page.evaluate("m=>window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'torture',revision:1,model:m}})",blank);page.evaluate("([e,g])=>window.__VIZ_PROD__.addLibraryElement(e,g)",[row['element'],row['engine']]);page.wait_for_timeout(3)
        default=page.evaluate("()=>window.CompanyUIVisualizerBridge.state().model.items[0]")
        per={}
        for variant in ('normal','long','zero','empty'):
          entry=default if variant=='normal' else mutate(default,variant);m={'schema_version':1,'items':[entry],'groups':{},'mode':'smart','layoutPreset':'editorial','crossFilter':None,'nextId':2};revision+=1
          page.evaluate("([m,r])=>window.CompanyUIVisualizerBridge.receive({bridge_version:1,type:'report.bootstrap',payload:{report_id:'torture',revision:r,model:m}})",[m,revision]);page.wait_for_timeout(5)
          info=page.evaluate("""()=>{const p=window.__VIZ_PROD__.preflight(),e=window.CompanyUIVisualizerBridge.state().model.items[0],n=document.querySelector(`.component[data-id="${e.id}"]`),c=n?.querySelector('.c-content');const codes=p.issues.filter(x=>x.kind==='layout').map(x=>x.code);return{codes,exists:!!n,overflow:c?{x:Math.max(0,c.scrollWidth-c.clientWidth),y:Math.max(0,c.scrollHeight-c.clientHeight)}:null,guide:+(document.querySelector('.cui-visualizer-root').dataset.snapGuideCount||0),pointer:!!window.__VIZ_PROD__.ui.pointer,serialized:window.__VIZ_PROD__.serialize()};}""")
          banned={'content-clipping','intrinsic-minimum','safe-hull'};bad=sorted(set(info['codes'])&banned);ok=info['exists'] and not bad and info['guide']==0 and not info['pointer']
          # absolute data invariants in zero/missing variants
          if variant=='zero' and row['engine']=='MetricEngine':
            parsed=json.loads(info['serialized']);ok=ok and parsed['items'][0].get('value')==0
          if row['engine']=='TimelineEngine' and variant in {'zero','long'}:
            parsed=json.loads(info['serialized']);ok=ok and all(x.get('date') is None for x in parsed['items'][0].get('milestones',[]))
          per[variant]={'pass':ok,'layout_codes':info['codes'],'overflow':info['overflow']}
          if not ok:result['failures'].append({'element':row['element'],'engine':row['engine'],'variant':variant,'detail':per[variant]})
        result['elements'][row['element']]={'engine':row['engine'],'pass':all(v['pass'] for v in per.values()),'variants':per}
        if idx%25==0 or idx==248: print(f'[TORTURE] {idx}/248 failures={len(result["failures"])}',flush=True)
      browser.close()
    result['summary']={'elements_passed':sum(1 for v in result['elements'].values() if v['pass']),'elements_total':248,'variant_cases':248*4,'variant_failures':len(result['failures']),'duration_seconds':round(time.time()-start,3)};result['pass']=not result['failures'] and not result['console_errors'] and not result['page_errors']
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'pass':result['pass'],**result['summary'],'console_errors':result['console_errors'][:5],'page_errors':result['page_errors'][:5]},indent=2));return 0 if result['pass'] else 1
if __name__=='__main__':raise SystemExit(main())
