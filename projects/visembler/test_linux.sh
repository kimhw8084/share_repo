#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="$ROOT/.venv/bin/python"
[[ -x "$PY" ]] || { echo "ERROR: Run ./setup_linux.sh first."; exit 1; }

"$ROOT/verify_checksums.sh" >/dev/null
"$PY" "$ROOT/tools/verify_package.py" --root "$ROOT"
"$PY" "$ROOT/tools/verify_visualizer_source_contract.py"
"$PY" "$ROOT/tools/verify_visualizer_asset_graph.py" --output "$ROOT/evidence/test_asset_graph.json"
"$PY" "$ROOT/tools/verify_nicegui315_runtime.py"
(cd /tmp && "$PY" "$ROOT/tools/verify_nicegui315_runtime.py" --installed-wheel)
"$PY" "$ROOT/tools/live_app_http_smoke.py" --output "$ROOT/evidence/test_live_app_http.json"

echo "Installing certification-only dependencies from the configured company package index..."
"$PY" -m pip install -r "$ROOT/requirements-test.txt" -r "$ROOT/requirements-certification.txt"

if ! "$PY" -c 'import playwright' >/dev/null 2>&1; then
  echo "ERROR: Playwright certification package is unavailable."
  exit 1
fi

echo "Running complete Python regression estate..."
(cd "$ROOT/source" && "$PY" -m pytest -q)
echo "Running Company UI governance..."
(cd "$ROOT/source" && "$PY" -m company_ui.governance.cli --root . --json)
echo "Running retained-editor Chromium application matrix..."
"$PY" "$ROOT/tools/r12_application_browser_matrix.py" --output "$ROOT/evidence/test_application_browser_matrix.json"
echo "Running retained-editor visual compatibility matrix..."
"$PY" "$ROOT/tools/r13_visual_layout_matrix.py" --output "$ROOT/evidence/test_r13_visual_layout_matrix.json"
echo "Running 248-element catalog render audit..."
"$PY" "$ROOT/tools/r13_catalog_render_audit.py" --output "$ROOT/evidence/test_r13_catalog_render_audit.json"
echo "Verifying R14 element capability contract..."
"$PY" "$ROOT/tools/r13_element_capabilities.py" --check
echo "Running R14 hard browser release gate..."
"$PY" "$ROOT/tools/r14_release_certification.py" --output "$ROOT/evidence/test_r14_release_certification.json"
echo "Running R14 all-248 content torture..."
"$PY" "$ROOT/tools/r14_content_torture.py" --output "$ROOT/evidence/test_r14_content_torture.json"
echo "Running R14 performance certification..."
"$PY" "$ROOT/tools/r14_performance_certification.py" --output "$ROOT/evidence/test_r14_performance.json"
echo "Running exact app.py restart + real app.storage.user persistence smoke..."
"$PY" "$ROOT/tools/live_app_restart_smoke.py" --output "$ROOT/evidence/test_live_app_restart.json"
echo "Running frozen Visualizer 97.1 authority suite in isolated partitions..."
"$PY" "$ROOT/tools/r14_frozen_authority_certification.py" --root "$ROOT" --start 1 --end 25 --output "$ROOT/evidence/test_visualizer_authority_01_25.json"
"$PY" "$ROOT/tools/r14_frozen_authority_certification.py" --root "$ROOT" --start 26 --end 26 --output "$ROOT/evidence/test_visualizer_authority_26.json"
"$PY" "$ROOT/tools/r14_frozen_authority_certification.py" --root "$ROOT" --start 27 --end 27 --output "$ROOT/evidence/test_visualizer_authority_27.json"
echo "Rechecking package parity after certification..."
"$PY" "$ROOT/tools/verify_package.py" --root "$ROOT"
echo
 echo "R14 FULL CERTIFICATION COMPLETE"
