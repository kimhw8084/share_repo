#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from urllib.parse import urljoin

IMPORT_RE=re.compile(r'''(?:from\s+|import\s*\(\s*)["']([^"']+)["']''')

def main() -> int:
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--output',type=Path);args=ap.parse_args()
    root=args.root.resolve(); product=root/'source/company_ui/products/visualizer'; assets=product/'assets'; vendor=product/'vendor/production_core'
    entry=assets/'integrated_editor.mjs'; queue=[entry]; seen=set(); missing=[]; edges=[]
    def url_for(path: Path) -> str:
        rel=path.relative_to(product).as_posix()
        if rel.startswith('assets/'): return '/_cui_visualizer/'+rel
        if rel.startswith('vendor/production_core/'): return '/_cui_visualizer/'+rel
        raise ValueError(rel)
    while queue:
        path=queue.pop(0).resolve()
        if path in seen: continue
        seen.add(path)
        text=path.read_text(encoding='utf-8')
        for spec in IMPORT_RE.findall(text):
            if not spec.startswith('.'): continue
            target=(path.parent/spec).resolve()
            edges.append({'from':url_for(path),'spec':spec,'to':url_for(target) if target.is_relative_to(product) else str(target)})
            if not target.is_file(): missing.append({'from':str(path),'spec':spec,'target':str(target)})
            elif target.suffix=='.mjs': queue.append(target)
    required=[assets/'integrated_editor.css',assets/'tokens.css',assets/'integrated_editor.html',assets/'element_renderer.mjs',entry,vendor/'core/editor_store.mjs',vendor/'core/runtime_registry.mjs',vendor/'core/universal_renderer.mjs']
    missing_files=[str(p) for p in required if not p.is_file()]
    result={'pass':not missing and not missing_files,'modules':[url_for(p) for p in sorted(seen)],'edges':edges,'missing':missing,'missing_files':missing_files,'http_urls':sorted({url_for(p) for p in seen}|{url_for(p) for p in required if p.is_file()})}
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(result,indent=2,sort_keys=True))
    print(json.dumps(result,indent=2,sort_keys=True));return 0 if result['pass'] else 1
if __name__=='__main__':raise SystemExit(main())
