#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from zipfile import ZipFile

EXPECTED_CONNECTOR="d8ebd4378f01b7c52a7a4be57c578c22adf29b899cc08a370cf084881195343e"
EXPECTED_REQ=["nicegui==3.15.0","python-pptx==1.0.2","Pillow==12.3.0"]
REQUIRED_TOOLS={"verify_package.py","verify_visualizer_asset_graph.py","verify_visualizer_source_contract.py","verify_nicegui315_runtime.py","live_app_restart_smoke.py","live_app_http_smoke.py","r12_application_browser_matrix.py","r13_visual_layout_matrix.py","r13_catalog_render_audit.py","r13_element_capabilities.py","r14_release_certification.py","r14_content_torture.py","r14_performance_certification.py","r14_frozen_authority_certification.py","run_visualizer_authority_suite.py"}

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1]); a=ap.parse_args(); root=a.root.resolve(); source=root/"source"; fail=[]
    root_py=sorted(p.name for p in root.glob("*.py"));
    required_shell={'setup_linux.sh','run_visualizer.sh','test_linux.sh','verify_checksums.sh'}
    missing_shell=sorted(name for name in required_shell if not (root/name).is_file())
    if missing_shell: fail.append(f'missing runtime shell scripts: {missing_shell}')
    if root_py!=["app.py"]: fail.append(f"root Python files must be exactly app.py: {root_py}")
    req=(root/"requirements.txt").read_text().splitlines() if (root/"requirements.txt").is_file() else []
    if req!=EXPECTED_REQ: fail.append(f"requirements must be exactly {EXPECTED_REQ!r}; found {req!r}")
    tools={p.name for p in (root/"tools").glob("*.py")}
    missing_tools=sorted(REQUIRED_TOOLS-tools)
    if missing_tools: fail.append(f"missing certification tools: {missing_tools}")
    wheels=list((root/"wheel").glob("company_ui-3.0.0a1-*.whl")); wheel=wheels[0] if len(wheels)==1 else None
    if wheel is None: fail.append(f"exactly one Company UI wheel required, found {len(wheels)}")
    vendor=source/"company_ui/products/visualizer/vendor/production_core"
    vendor_files=[p for p in vendor.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix!=".pyc"]
    if len(vendor_files)!=123: fail.append(f"frozen vendor file count changed: {len(vendor_files)} != 123")
    contract=json.loads((vendor/"contracts/runtime_registry.json").read_text()); elements=sum(len(v) for v in contract["byEngine"].values()); engines=len(contract["byEngine"])
    capability_path=source/"company_ui/products/visualizer/contracts/ELEMENT_CAPABILITY_MATRIX.json"
    if not capability_path.is_file(): fail.append("element capability matrix missing")
    else:
        capability=json.loads(capability_path.read_text())
        if capability.get("count")!=248 or capability.get("engines")!=17 or len(capability.get("rows",[]))!=248: fail.append("element capability matrix is not 248/17 complete")
        if any(row.get("renderer_source")!="integration" for row in capability.get("rows",[])): fail.append("capability matrix contains non-integration renderer fallbacks")
    if (elements,engines)!=(248,17): fail.append(f"authority catalog is {elements}/{engines}, expected 248/17")
    connector=vendor/"core/GOLDEN_CONNECTOR_ENGINE_V5_FROZEN.js"; connector_hash=hashlib.sha256(connector.read_bytes()).hexdigest()
    if connector_hash!=EXPECTED_CONNECTOR: fail.append(f"Golden Connector v5 hash changed: {connector_hash}")
    suite_path=vendor/"qa/release_suite.json"
    try: suite=json.loads(suite_path.read_text())
    except Exception as exc: suite={}; fail.append(f"frozen release suite evidence unreadable: {exc}")
    if not (suite.get("pass") is True and suite.get("commands_planned")==27 and suite.get("commands_ran")==27 and len(suite.get("results",[]))==27):
        fail.append("frozen Visualizer release-suite evidence is not 27/27 PASS")
    identity_path=root/"evidence/r12_frozen_authority_identity.json"
    if identity_path.is_file():
        identity=json.loads(identity_path.read_text())
        if not (identity.get("pass") and identity.get("authority_files")==123 and identity.get("vendor_files")==123 and identity.get("golden_connector_sha256")==EXPECTED_CONNECTOR): fail.append("master authority identity evidence is invalid")
    parity=True; parity_errors=[]
    if wheel:
        with ZipFile(wheel) as z:
            names=set(z.namelist()); source_names=set()
            for path in (source/"company_ui").rglob("*"):
                if not path.is_file() or "__pycache__" in path.parts or path.suffix==".pyc": continue
                rel=path.relative_to(source).as_posix(); source_names.add(rel)
                if rel not in names: parity=False; parity_errors.append("missing:"+rel); continue
                if z.read(rel)!=path.read_bytes(): parity=False; parity_errors.append("different:"+rel)
            wheel_company={n for n in names if n.startswith("company_ui/") and not n.endswith("/")}
            for extra in sorted(wheel_company-source_names): parity=False; parity_errors.append("extra:"+extra)
        if not parity: fail.extend(parity_errors[:30])
    result={"pass":not fail,"failures":fail,"elements":elements,"engines":engines,"frozen_vendor_files":len(vendor_files),"frozen_authority_suite":"27/27 PASS" if not fail or suite.get("pass") else "invalid","golden_connector_sha256":connector_hash,"wheel_source_parity":parity}
    print(json.dumps(result,indent=2,sort_keys=True)); return 0 if result["pass"] else 1
if __name__=="__main__": raise SystemExit(main())
