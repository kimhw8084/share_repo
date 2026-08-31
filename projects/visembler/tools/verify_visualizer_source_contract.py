#!/usr/bin/env python3
from __future__ import annotations
import ast, json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'source'
PRODUCT=SRC/'company_ui/products/visualizer'
fail=[]

def require(ok: bool, msg: str):
    if not ok: fail.append(msg)

root_py=sorted(p.name for p in ROOT.glob('*.py'))
require(root_py==['app.py'],f'root Python files must be exactly app.py; found {root_py}')
app=(ROOT/'app.py').read_text(encoding='utf-8')
cli=(PRODUCT/'cli.py').read_text(encoding='utf-8')
runtime=(PRODUCT/'runtime.py').read_text(encoding='utf-8')
page=(PRODUCT/'page.py').read_text(encoding='utf-8')
editor=(PRODUCT/'assets/integrated_editor.mjs').read_text(encoding='utf-8')
layout=(SRC/'company_ui/integrations/nicegui_layout.py').read_text(encoding='utf-8')

# Startup authority: Visualizer never calls ui.run directly; Company UI adapter owns it.
for p in PRODUCT.rglob('*.py'):
    text=p.read_text(encoding='utf-8')
    try: tree=ast.parse(text,filename=str(p))
    except SyntaxError: continue
    for node in ast.walk(tree):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and node.func.attr=='run' and isinstance(node.func.value,ast.Name) and node.func.value.id=='ui':
            fail.append(f'parallel ui.run detected in {p.relative_to(SRC)}')
require('adapter.run(environ=env)' in cli,'Visualizer CLI must pass resolved environment into Company UI runtime adapter')
require('COMPANY_UI_STORAGE_SECRET' in runtime,'runtime secret handling missing')
require("raw == 'prod'" in runtime and 'required in production' in runtime,'production storage secret fail-closed contract missing')
require('storage_secret' not in app,'root app.py must not own NiceGUI storage configuration')

# Previously confirmed runtime API failures must stay impossible.
require('follow_symlinks' not in page,'unsupported plural follow_symlinks present')
require('follow_symlink=False' in page,'static mounts must use NiceGUI 3.15 follow_symlink')
require('.set_text(' not in page,'generic Element.set_text regression present')
require('NiceGUIStateServices.tab_store()' not in page,'Visualizer page builder must not access app.storage.tab before WebSocket connection')
require('NiceGUIStateServices.user_store()' in page,'Visualizer last-open report state must use request-safe user storage')
require("'chart-line'" in page,'canonical governed Visualizer navigation icon missing')
require("'chart'" not in page,'non-governed chart icon alias present')
require('js_handler=' in layout,'mobile drawer browser-local NiceGUI js_handler contract missing')

# Browser/runtime safety laws.
for forbidden in ('crypto.randomUUID','crypto.subtle'):
    require(forbidden not in editor,f'unsupported secure-context browser API present: {forbidden}')
require("document.body.classList.toggle('preview-mode'" not in editor,'preview must be root-scoped, not body-scoped')
require('data-editor-ready' in (PRODUCT/'assets/integrated_editor.html').read_text(encoding='utf-8'),'editor readiness contract missing')
require('MutationObserver' in editor and 'AbortController' in editor,'editor rebind/teardown lifecycle missing')
require('report.commit' in editor and 'MAX_BRIDGE_BYTES' in editor,'semantic bridge/size law missing')

# Parse all Python modules to catch syntax damage.
for p in [ROOT/'app.py',*PRODUCT.rglob('*.py')]:
    try: ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
    except SyntaxError as exc: fail.append(f'syntax:{p}:{exc}')

# Exact requirements and package data.
req=(ROOT/'requirements.txt').read_text().splitlines()
require(req==['nicegui==3.15.0','python-pptx==1.0.2','Pillow==12.3.0'],f'unexpected requirements: {req}')
pyproject=(SRC/'pyproject.toml').read_text(encoding='utf-8')
require('"company_ui.products.visualizer"' in pyproject and 'vendor/production_core/**/*' in pyproject,'Visualizer package data contract missing')

result={'pass':not fail,'failures':fail,'root_python_files':root_py,'requirements':req}
print(json.dumps(result,indent=2,sort_keys=True))
raise SystemExit(0 if result['pass'] else 1)
