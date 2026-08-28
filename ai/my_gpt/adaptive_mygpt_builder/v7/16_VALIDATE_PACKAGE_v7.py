from pathlib import Path
import csv, hashlib, json, sys, zipfile
ROOT=Path(__file__).resolve().parent
required=[
'00_README_FIRST_v7.md','01_RUNTIME_INSTRUCTIONS_v7.txt','02_GOVERNANCE_AND_BASELINE_v7.md',
'03_BUILD_ROUTER_AND_OWNER_DISCOVERY_v7.md','04_RESEARCH_AND_EVIDENCE_OS_v7.md',
'05_DOMAIN_AND_AGENT_PATTERNS_v7.md','06_COMPILER_AND_PACKAGE_CONTRACT_v7.md',
'07_EVALUATION_AND_REGRESSION_SYSTEM_v7.md','08_SETTINGS_AND_INSTALL_GUIDE_v7.md',
'09_SCIENTIFIC_RESEARCH_REPORT_v7.md','09B_RESEARCH_SOURCE_REGISTRY_v7.csv',
'10_BENCHMARK_REGISTRY_v7.csv','11_PROVISIONAL_HOLDOUT_v7.csv','11_HOLDOUT_PROTOCOL_v7.md',
'12_EVALUATION_WORKBOOK_v7.xlsx','13_CONVERSATION_STARTERS_v7.txt','14_CHANGELOG_v6_to_v7.md','15_DELIVERY_MANIFEST_v7.csv','manifest.json']
errors=[]
for f in required:
    if not (ROOT/f).exists(): errors.append(f'MISSING {f}')
runtime=(ROOT/'01_RUNTIME_INSTRUCTIONS_v7.txt').read_text(encoding='utf-8').rstrip('\n')
if len(runtime)>=8000: errors.append(f'RUNTIME_OVER_LIMIT {len(runtime)}')
if 8000-len(runtime)<1000: errors.append(f'RUNTIME_MARGIN_LT_1000 {8000-len(runtime)}')
for csvname in ['10_BENCHMARK_REGISTRY_v7.csv','11_PROVISIONAL_HOLDOUT_v7.csv']:
    with (ROOT/csvname).open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    ids=[r['case_id'] for r in rows]
    if len(ids)!=len(set(ids)): errors.append(f'DUPLICATE_IDS {csvname}')
    for i,r in enumerate(rows,2):
        for k in ['case_id','full_user_prompt','expected_route','required_behaviors','severity']:
            if not r.get(k): errors.append(f'MISSING_FIELD {csvname}:{i}:{k}')

try:
    with zipfile.ZipFile(ROOT/'12_EVALUATION_WORKBOOK_v7.xlsx') as z:
        bad=z.testzip()
        if bad: errors.append(f'XLSX_CORRUPT {bad}')
except Exception as e:
    errors.append(f'XLSX_INVALID {type(e).__name__}: {e}')

manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    p=ROOT/item['path']
    if not p.exists(): errors.append(f'MANIFEST_MISSING {item["path"]}'); continue
    actual=hashlib.sha256(p.read_bytes()).hexdigest()
    if actual!=item['sha256']: errors.append(f'HASH_MISMATCH {item["path"]}')
print(json.dumps({'status':'PASS' if not errors else 'FAIL','runtime_characters':len(runtime),'maintenance_margin':8000-len(runtime),'errors':errors},indent=2))
sys.exit(1 if errors else 0)
