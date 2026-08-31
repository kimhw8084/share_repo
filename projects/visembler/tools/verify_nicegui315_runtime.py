#!/usr/bin/env python3
from __future__ import annotations
import argparse, inspect, json, os, tempfile
from importlib.metadata import version
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(); ap.add_argument('--installed-wheel',action='store_true'); args=ap.parse_args()
fail=[]
def need(ok,msg):
    if not ok: fail.append(msg)
try:
    import nicegui
    from nicegui import app, ui
    from nicegui.element import Element
except Exception as exc:
    print(json.dumps({'pass':False,'failures':[f'NiceGUI import failed: {exc}']},indent=2)); raise SystemExit(1)

actual=version('nicegui')
need(actual=='3.15.0',f'NiceGUI must be exactly 3.15.0; installed={actual}')
run_sig=inspect.signature(ui.run)
for name in ('host','port','storage_secret','session_middleware_kwargs','root_path','workers'):
    need(name in run_sig.parameters,f'ui.run missing required parameter {name}')
static_sig=inspect.signature(app.add_static_files)
for name in ('url_path','local_directory','follow_symlink','max_cache_age'):
    need(name in static_sig.parameters,f'app.add_static_files missing required parameter {name}')
need('follow_symlinks' not in static_sig.parameters,'unexpected plural follow_symlinks API assumption')
on_sig=inspect.signature(Element.on)
need('js_handler' in on_sig.parameters,'Element.on missing js_handler')

# Construct the exact application once. This executes static route registration and
# page factory wiring against real NiceGUI instead of a fake harness.
if not fail:
    import sys
    if not args.installed_wheel: sys.path.insert(0,str(ROOT/'source'))
    from company_ui.products.visualizer.cli import build_application
    import company_ui
    imported_from=str(Path(company_ui.__file__).resolve())
    if args.installed_wheel and str((ROOT/'source').resolve()) in imported_from:
        fail.append(f'installed-wheel mode imported source tree: {imported_from}')
    with tempfile.TemporaryDirectory(prefix='cui-r12-api-') as td:
        env={'COMPANY_UI_ENVIRONMENT':'dev','COMPANY_UI_HOST':'127.0.0.1','COMPANY_UI_PORT':'18080','COMPANY_UI_VISUALIZER_DATA_DIR':td}
        try:
            adapter,resolved,repo=build_application(env)
            kwargs=adapter.run_kwargs(resolved)
            need(bool(kwargs.get('storage_secret')),'resolved storage_secret did not reach NiceGUI run kwargs')
            need(kwargs.get('workers')==1,'NiceGUI application must use one worker per process')
            need(len(repo.list())==1,'application bootstrap should create exactly one initial report in an empty repository')
            secret_file=Path(td)/'.storage_secret'
            need(secret_file.is_file(),'non-production storage secret was not persisted')
        except Exception as exc:
            fail.append(f'real NiceGUI application construction failed: {type(exc).__name__}: {exc}')

result={'pass':not fail,'mode':'installed-wheel' if args.installed_wheel else 'bundled-source','company_ui_import':locals().get('imported_from'),'nicegui':actual,'ui_run_parameters':list(run_sig.parameters),'static_parameters':list(static_sig.parameters),'element_on_parameters':list(on_sig.parameters),'failures':fail}
print(json.dumps(result,indent=2,sort_keys=True))
raise SystemExit(0 if result['pass'] else 1)
