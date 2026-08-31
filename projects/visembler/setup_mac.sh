#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
VENV="$ROOT/.venv"
find_python() {
  for candidate in python3.13 python3.12 python3.11 python3; do
    if command -v "$candidate" >/dev/null 2>&1 && "$candidate" - <<'PY2' >/dev/null 2>&1
import sys
raise SystemExit(0 if (3,11) <= sys.version_info[:2] < (3,14) else 1)
PY2
    then echo "$candidate"; return 0; fi
  done
  return 1
}
PYTHON="$(find_python || true)"
[[ -n "$PYTHON" ]] || { echo "ERROR: Python 3.11, 3.12, or 3.13 is required."; exit 1; }
WHEEL="$(find "$ROOT/wheel" -maxdepth 1 -name 'company_ui-3.0.0a1-*.whl' -print -quit)"
[[ -n "$WHEEL" ]] || { echo "ERROR: Company UI v3.0.0a1 wheel not found under $ROOT/wheel"; exit 1; }

echo "Visembler macOS setup"
echo "  macOS: $(sw_vers -productVersion 2>/dev/null || true)"
echo "  architecture: $(uname -m)"
echo "  python: $($PYTHON --version 2>&1)"

if [[ -f "$ROOT/SHA256SUMS.txt" ]]; then
  echo "Verifying release checksums..."
  "$ROOT/verify_checksums.sh" >/dev/null
fi

echo "Verifying package/source contracts before installation..."
"$PYTHON" "$ROOT/tools/verify_visualizer_source_contract.py" >/dev/null
"$PYTHON" "$ROOT/tools/verify_package.py" --root "$ROOT" >/dev/null
"$PYTHON" "$ROOT/tools/verify_visualizer_asset_graph.py" --output "$ROOT/evidence/setup_asset_graph.json" >/dev/null

if [[ ! -d "$VENV" ]]; then
  "$PYTHON" -m venv "$VENV" || { echo "ERROR: Python venv creation failed."; exit 1; }
fi

echo "Installing exact production dependencies from the configured company Python package index..."
if ! "$VENV/bin/python" -m pip install -r "$ROOT/requirements.txt"; then
  echo "ERROR: dependency installation failed. Current pip configuration:"
  "$VENV/bin/python" -m pip config list || true
  exit 1
fi

echo "Installing the bundled Company UI wheel without re-resolving dependencies..."
"$VENV/bin/python" -m pip install --force-reinstall --no-deps "$WHEEL"

echo "Verifying the real NiceGUI 3.15 API against the bundled-source application..."
"$VENV/bin/python" "$ROOT/tools/verify_nicegui315_runtime.py"
echo "Verifying the real NiceGUI 3.15 API against the installed wheel..."
(cd /tmp && "$VENV/bin/python" "$ROOT/tools/verify_nicegui315_runtime.py" --installed-wheel)

echo "Running Company UI runtime contract and runtime doctor..."
"$VENV/bin/company-ui" runtime-contract
"$VENV/bin/company-ui" doctor --runtime-only --ignore-port --port 8080 --no-require-browser

echo "Launching the exact 'python app.py' path and exercising HTTP + storage-secret startup..."
"$VENV/bin/python" "$ROOT/tools/live_app_http_smoke.py" --output "$ROOT/evidence/setup_live_app_http.json"

mkdir -p "$ROOT/runtime_data"
echo
echo "SETUP COMPLETE"
echo "Run the app with: ./run_visualizer.sh"
echo "Then open: http://127.0.0.1:8080/visualizer"
echo "Optional exhaustive certification: ./test_linux.sh"
