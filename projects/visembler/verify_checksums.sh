#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
[[ -f SHA256SUMS.txt ]] || { echo "ERROR: SHA256SUMS.txt missing"; exit 1; }
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum -c SHA256SUMS.txt
elif command -v shasum >/dev/null 2>&1; then
  shasum -a 256 -c SHA256SUMS.txt
else
  echo "ERROR: need sha256sum or shasum for release checksum verification."
  exit 1
fi
