# Company UI 3.0.0a1 — Read Me First

This is the complete portable Company UI v3 alpha checkpoint built from the authoritative v2.0.0rc5 lineage.

## Evidence frozen into this package

- Framework identity: `3.0.0a1` / ALPHA; stable promotion target remains `3.0.0`.
- Full inherited + v3 source suite: **672/672 PASS**.
- Governance: **0 errors / 0 warnings**.
- Source certification: **12 PASS / 1 expected sandbox warning / 0 FAIL**.
- Visual integration mapping: **183/183**.
- Browser-native UI/UX constitution: **43/43 PASS** across desktop light, desktop dark + compact sidebar, tablet, and mobile dark + reduced-motion.
- Final wheel RECORD integrity: **391/391 verified, 0 mismatches**.
- Final wheel SHA-256: `f20c525d4771b9bd1d7855332a1a4232eb0e8503dd8d578b711bd67f82da9513`.

The build sandbox could not install NiceGUI because DNS/package-index access is disabled and no local NiceGUI 3.15.0 wheel/cache exists. This package therefore **does not claim** the installed NiceGUI/WebSocket/live-browser matrix or human visual-baseline gates have passed. `TARGET_RUNTIME_GATE_ATTEMPT.json` records the attempt explicitly.

## Target-machine workflow

From the extracted package directory:

```bash
chmod +x *.sh
./setup.sh
./run_lab.sh
```

`./setup.sh` installs exact `nicegui==3.15.0` through the configured company Python index, installs this wheel, verifies the installed runtime contract, and smoke-tests all 22 live routes. Keep the lab open for manual review.

For automated browser certification:

```bash
./install_certification_deps.sh
./certify.sh
```

After reviewing the generated screenshots and live application, approve the baseline only when it is visually correct:

```bash
./approve_visual_baseline.sh
```

Do not promote to stable `3.0.0` until the target runtime, 22-route live smoke, supported Chrome/Edge matrix, and human visual baseline are all PASS.

## Development continuation

The tested source tree is under `source/`. The installable wheel is under `wheel/`. Browser-rendered evidence is under `evidence/browser_uiux/`.

For a new ChatGPT development session, open this file first and then follow `context/10_RESUME_PROMPT.md`.
