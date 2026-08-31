#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

DIRECT={
 'SmartLayoutEngine':'inspector_configuration','TextEngine':'inline_text','MetricEngine':'inline_value','ComparisonEngine':'inspector_comparison',
 'CoreChartEngine':'inspector_data_grid','TableEngine':'spreadsheet_grid','MatrixEngine':'inspector_matrix','TimelineEngine':'visual_event_editor',
 'DiagramEngine':'direct_nodes_edges','ImageMediaEngine':'file_or_clipboard','EvidenceCompositeEngine':'inspector_statement','DecisionCompositeEngine':'inspector_statement',
 'ProjectCompositeEngine':'inspector_statement','EngineeringChartEngine':'inspector_observations','WaferFabEngine':'point_inspector',
 'InteractionLayer':'inspector_behavior','EditorInfrastructure':'inspector_configuration',
}
PASTE={
 'CoreChartEngine':'label_value_tsv_csv','TableEngine':'rectangular_tsv_csv','MatrixEngine':'matrix_tsv_csv','ImageMediaEngine':'image_clipboard',
 'EngineeringChartEngine':'label_value_tsv_csv','WaferFabEngine':'x_y_value_tsv_csv','TimelineEngine':'event_rows','DiagramEngine':'structured_nodes_edges',
}
INSPECTOR={
 'SmartLayoutEngine':'#iConfiguration','TextEngine':'#iText','MetricEngine':'#iValue','ComparisonEngine':'#iBefore','CoreChartEngine':'#iData',
 'TableEngine':'#iTable','MatrixEngine':'#iMatrix','TimelineEngine':'#iTimeline','DiagramEngine':'#iNodes','ImageMediaEngine':'#iImageFile',
 'EvidenceCompositeEngine':'#iStatement','DecisionCompositeEngine':'#iStatement','ProjectCompositeEngine':'#iStatement','EngineeringChartEngine':'#iObservations',
 'WaferFabEngine':'#iTool','InteractionLayer':'#iBehavior','EditorInfrastructure':'#iConfiguration',
}

ENGINE_FAMILY={
 'SmartLayoutEngine':'layout','TextEngine':'narrative','MetricEngine':'metric','ComparisonEngine':'comparison','CoreChartEngine':'chart',
 'TableEngine':'table','MatrixEngine':'matrix','TimelineEngine':'timeline','DiagramEngine':'diagram','ImageMediaEngine':'media',
 'EvidenceCompositeEngine':'evidence','DecisionCompositeEngine':'decision','ProjectCompositeEngine':'project','EngineeringChartEngine':'engineering-chart',
 'WaferFabEngine':'wafer-fab','InteractionLayer':'interaction','EditorInfrastructure':'editor-infrastructure',
}

def slug(s:str)->str:return re.sub(r'(^-|-$)','',re.sub(r'[^a-z0-9]+','-',s.lower()))
def renderer_source(element:str,engine:str)->str:return 'integration'

def inspector_schema(element:str,engine:str)->str:
    n=element.lower()
    if engine!='MetricEngine': return f'{ENGINE_FAMILY[engine]}.semantic'
    if 'ladder' in n:return 'metric.ladder'
    if 'ring' in n:return 'metric.ring'
    if 'confidence' in n:return 'metric.confidence'
    if 'capacity' in n:return 'metric.capacity'
    if 'rate' in n:return 'metric.rate'
    if 'threshold' in n:return 'metric.threshold'
    if 'target' in n and 'actual' in n:return 'metric.target_actual'
    if 'progress' in n:return 'metric.progress'
    if 'sparkline' in n:return 'metric.sparkline'
    return 'metric.value'

def visual_grammar(element:str,engine:str)->str:
    n=element.lower(); fam=ENGINE_FAMILY[engine]
    if engine=='MetricEngine':
        for key in ('ring','ladder','sparkline','threshold','capacity','progress','confidence','rate','target'):
            if key in n:return f'metric-{key}'
        return 'metric-value'
    if engine=='TimelineEngine':return 'timeline-vertical' if 'vertical' in n else ('schedule-grid' if 'schedule' in n or 'calendar' in n else 'timeline-horizontal')
    if engine=='DiagramEngine':return 'diagram-node' if 'node' in n else 'diagram-flow'
    if engine in {'CoreChartEngine','EngineeringChartEngine'}:return f'{fam}-{slug(element)}'
    if engine in {'TableEngine','MatrixEngine'}:return f'{fam}-grid'
    if engine=='ImageMediaEngine':return 'media-image'
    if engine=='WaferFabEngine':return 'wafer-map' if 'wafer' in n else 'fab-engineering'
    return f'{fam}-{slug(element)}'

def smart_constraints(element:str,engine:str,geom:dict)->dict:
    n=element.lower(); minw=float(geom['min']['w']); minh=float(geom['min']['h']); prefw=float(geom['preferred']['w']); prefh=float(geom['preferred']['h'])
    growth='fixed'; wrap='normal'; aspect=None
    if engine=='MetricEngine':
        minw,minh,prefw,prefh=220,135,280,155
        if 'hero' in n:minw,minh,prefw,prefh=280,145,420,170
        elif 'ring' in n:minw,minh,prefw,prefh=205,205,235,235;aspect=1.0
        elif 'ladder' in n:minw,minh,prefw,prefh=235,185,280,210
        elif 'sparkline' in n:minw,minh,prefw,prefh=255,155,315,175
        elif 'confidence' in n:minw,minh,prefw,prefh=250,165,305,190
        elif 'threshold' in n:minw,minh,prefw,prefh=250,160,310,180
        elif 'capacity' in n or 'rate' in n:minw,minh,prefw,prefh=240,150,295,170
    elif engine in {'CoreChartEngine','EngineeringChartEngine'}:minw,minh,prefw,prefh=320,220,410,270;aspect=1.45
    elif engine=='TableEngine':minw,minh,prefw,prefh=340,210,470,280;growth='vertical'
    elif engine=='MatrixEngine':minw,minh,prefw,prefh=290,220,350,280;aspect=1.2
    elif engine=='TimelineEngine':
        minw,minh,prefw,prefh=360,165,500,190;growth='horizontal'
        if 'vertical' in n:minw,minh,prefw,prefh=245,285,290,360;growth='vertical'
        elif any(k in n for k in ('gantt','schedule','swimlane')):minw,minh,prefw,prefh=420,230,560,300
    elif engine=='DiagramEngine':minw,minh,prefw,prefh=340,225,450,285
    elif engine=='ImageMediaEngine':minw,minh,prefw,prefh=280,200,390,260;aspect=1.5
    elif engine=='WaferFabEngine':minw,minh,prefw,prefh=260,250,320,300;aspect=1.0 if 'wafer' in n else 1.2
    elif engine=='TextEngine':minw,minh,prefw,prefh=260,125,360,165;growth='vertical';wrap='reading-width'
    elif engine in {'EvidenceCompositeEngine','DecisionCompositeEngine','ProjectCompositeEngine'}:minw,minh,prefw,prefh=285,165,360,205;growth='vertical'
    elif engine=='ComparisonEngine':minw,minh,prefw,prefh=280,160,360,190
    # frozen max remains the authority ceiling; semantic minimum can be stricter than legacy contract min.
    return {'min_width':int(minw),'min_height':int(minh),'preferred_width':int(prefw),'preferred_height':int(prefh),'preferred_aspect':aspect,'content_growth':growth,'text_wrap_policy':wrap,'safe_margin':14,'overflow_policy':'reflow_or_actionable_conflict'}

def empty_state(engine:str)->dict:
    actions={
      'CoreChartEngine':['paste_data','enter_data','connect_dataset'], 'TableEngine':['paste_rows','add_row','enter_data'],
      'ImageMediaEngine':['paste_image','upload'], 'DiagramEngine':['add_node','paste_structure'], 'TimelineEngine':['add_event'],
    }.get(engine,[])
    return {'required':bool(actions),'actions':actions,'must_be_functional':bool(actions)}

def default_model_ref(engine:str)->str:return f'defaults.{ENGINE_FAMILY[engine]}'

def build(root:Path)->dict:
    product=root/'source/company_ui/products/visualizer';core=product/'vendor/production_core/contracts';contracts=json.loads((core/'component_contracts.json').read_text())['contracts'];rows=[]
    for c in contracts:
        engine=c['canonical_engine'];geom=c['geometry'];ppt=c['ppt'];element=c['element'];sc=smart_constraints(element,engine,geom);schema=inspector_schema(element,engine)
        rows.append({
            'element':element,'element_id':slug(element),'engine':engine,'category':c['category'],'family':c.get('relationship','variant of canonical engine'),
            'semantic_family':ENGINE_FAMILY[engine],'visual_grammar':visual_grammar(element,engine),'default_model_ref':default_model_ref(engine),
            'renderer_variant':slug(element),'renderer_source':renderer_source(element,engine),'library_thumbnail':visual_grammar(element,engine),
            'inspector':INSPECTOR[engine],'inspector_schema':schema,'direct_edit':DIRECT[engine],'direct_edit_behavior':DIRECT[engine],
            'paste':PASTE.get(engine,'none'),'paste_behavior':PASTE.get(engine,'none'),'empty_state_required':empty_state(engine)['required'],'empty_state':empty_state(engine),
            'geometry':{'min':geom['min'],'preferred':geom['preferred'],'max':geom['max']},'smart_layout_constraints':sc,
            'geometry_behavior':{'smart':'semantic_owned','guided':'user_owned_snapped','free':'user_owned_unsnapped','minimum_enforced':True},
            'save_reload':'canonical_revision_safe','undo_redo':'editor_command_semantics','responsive_behavior':'viewport_fit_plus_scroll_containers',
            'keyboard_path_required':bool(c['accessibility']['keyboard_path_required']),'accessibility_behavior':{'keyboard_path_required':bool(c['accessibility']['keyboard_path_required']),'type_label_hidden_by_default':True},
            'ppt_mapping':ppt['mapping'],'ppt_editable_preference':bool(ppt['editable_preference']),'export_authority':'frozen_visualizer_97_1','export_eligibility':'semantic_when_supported',
            'revision_safe':bool(c['serialization']['revision_safe_mutations']),'raw_values_preserved':bool(c['data_binding']['raw_values_preserved']),
        })
    return {'schema_version':2,'capability_release':'R14','count':len(rows),'engines':len({r['engine'] for r in rows}),'rows':rows}

def validate(data:dict)->list[str]:
    errors=[];rows=data.get('rows',[])
    if data.get('count')!=248 or len(rows)!=248:errors.append(f'expected 248 rows, got manifest={data.get("count")} actual={len(rows)}')
    engines={r.get('engine') for r in rows}
    if len(engines)!=17:errors.append(f'expected 17 engines, got {len(engines)}')
    names=[r.get('element') for r in rows]
    if len(set(names))!=len(names):errors.append('duplicate element names')
    variants=[r.get('renderer_variant') for r in rows]
    if len(set(variants))!=248:errors.append('renderer variants are not 248/248 unique')
    required=('element','element_id','engine','category','semantic_family','visual_grammar','renderer_variant','renderer_source','library_thumbnail','inspector','inspector_schema','direct_edit','paste','geometry','smart_layout_constraints','geometry_behavior','save_reload','undo_redo','responsive_behavior','ppt_mapping','export_authority','export_eligibility','accessibility_behavior')
    for i,row in enumerate(rows):
        missing=[k for k in required if row.get(k) in (None,'')]
        if missing:errors.append(f'row {i} {row.get("element")}: missing {missing}')
        for k in ('min','preferred','max'):
            g=row.get('geometry',{}).get(k,{})
            if not (isinstance(g.get('w'),(int,float)) and isinstance(g.get('h'),(int,float)) and g['w']>0 and g['h']>0):errors.append(f'{row.get("element")}: invalid geometry {k}')
        sc=row.get('smart_layout_constraints',{})
        if sc.get('min_width',0)<=0 or sc.get('min_height',0)<=0:errors.append(f'{row.get("element")}: invalid semantic intrinsic minimum')
        if row.get('renderer_source')!='integration':errors.append(f'{row.get("element")}: renderer must remain integration-owned')
    return errors

def main()->int:
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=None);ap.add_argument('--check',action='store_true');args=ap.parse_args();root=Path(__file__).resolve().parents[1];target=args.output or root/'source/company_ui/products/visualizer/contracts/ELEMENT_CAPABILITY_MATRIX.json';target.parent.mkdir(parents=True,exist_ok=True)
    generated=build(root)
    if args.check and target.exists():
        existing=json.loads(target.read_text())
        if existing!=generated:print('[FAIL] capability matrix differs from generated authority mapping');return 1
    errors=validate(generated)
    if errors:
        for e in errors:print('[FAIL]',e)
        return 1
    target.write_text(json.dumps(generated,indent=2,sort_keys=True)+'\n');counts={}
    for row in generated['rows']:counts[row['renderer_source']]=counts.get(row['renderer_source'],0)+1
    schemas=len({r['inspector_schema'] for r in generated['rows']});thumbs=len({r['library_thumbnail'] for r in generated['rows']})
    print(json.dumps({'pass':True,'elements':generated['count'],'engines':generated['engines'],'inspector_schemas':schemas,'thumbnail_grammars':thumbs,'renderer_sources':counts},indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
