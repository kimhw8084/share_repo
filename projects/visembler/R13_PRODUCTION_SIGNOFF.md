# Company UI Visualizer R13 — Production Signoff

R13 is the complete shared UI/UX-system redesign on top of the R12.2 application-hardening runtime. It preserves Company UI runtime authority, report revision/persistence behavior, frozen Visualizer 97.1 authority, and Golden Connector v5.

## Certified R13 product gates

- 699/699 Python tests completed successfully.
- Company UI governance: 0 errors / 0 warnings.
- Retained-editor functional Chromium matrix: 38/38 PASS.
- R13 visual/layout Chromium matrix: 44/44 PASS across 1600×1000, 1440×900, and 1280×800.
- Catalog renderer audit: 248/248 elements rendered.
- Distinct normalized visual structures: 248/248; duplicate groups: 0.
- Element capability contract: 248/248 across all 17 engines.
- Browser console errors: 0. Browser page errors: 0.
- Recursive browser asset/module graph: PASS, zero missing targets.
- Wheel/source byte parity: PASS.
- Frozen Visualizer vendor authority: 123 files unchanged.
- Embedded frozen authority release evidence: 27/27 PASS.
- Latest authority execution: commands 1–26 passed sequentially; Golden Connector benchmark passed independently after the sandbox legacy orchestrator hung while launching the last Chromium benchmark after the 248-browser gate.
- Golden Connector v5 SHA-256: `d8ebd4378f01b7c52a7a4be57c578c22adf29b899cc08a370cf084881195343e`.

## R13 UI/UX redesign

R13 replaces the previous cramped fixed editor geometry with a shared authoring system: readable typography and physical control targets, wider semantic library and inspector, grouped command bars, panel-aware canvas sizing, constrained minimap/context overlays, transient snap guides, semantic empty states, direct editing entry points, and data-driven rendering. Technical release/debug labels are removed from ordinary authoring UI.

All 248 catalog entries now route through the governed integration renderer and have distinct normalized visual structures plus explicit engine/editor/paste/geometry/export capability contracts.

## Application runtime

The canonical runtime remains:

`app.py → Visualizer CLI → Company UI RuntimeConfig → NiceGUIRuntimeAdapter → ui.run(...)`

No Visualizer-specific parallel `ui.run()` configuration is introduced. Local runtime uses the existing R12.2 persistent-secret behavior; production remains fail-closed without the configured production storage secret.

## Target-runtime gate

The packaging sandbox does not contain NiceGUI. R13 therefore does not claim a fake NiceGUI runtime pass. `./setup.sh` installs the exact production dependencies and must pass the real NiceGUI 3.15 API/application smoke before declaring setup complete. `./test_linux.sh` then executes the exhaustive browser/restart/authority certification.
