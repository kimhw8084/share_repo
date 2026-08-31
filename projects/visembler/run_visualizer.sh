#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PY="$ROOT/.venv/bin/python"
if [[ ! -x "$PY" ]]; then
  echo "ERROR: runtime environment is not installed. Run ./setup.sh first."
  exit 1
fi
export COMPANY_UI_ENVIRONMENT="${COMPANY_UI_ENVIRONMENT:-dev}"
export COMPANY_UI_HOST="${COMPANY_UI_HOST:-0.0.0.0}"
export COMPANY_UI_PORT="${COMPANY_UI_PORT:-${PORT:-8080}}"
export COMPANY_UI_VISUALIZER_DATA_DIR="${COMPANY_UI_VISUALIZER_DATA_DIR:-$ROOT/runtime_data}"
mkdir -p "$COMPANY_UI_VISUALIZER_DATA_DIR"
echo "Starting Visembler"
echo "  URL: http://127.0.0.1:${COMPANY_UI_PORT}/visualizer"
echo "  data: $COMPANY_UI_VISUALIZER_DATA_DIR"
exec "$PY" "$ROOT/app.py"
