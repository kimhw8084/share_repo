# Resume Prompt — Company UI v3

Open `00_READ_ME_FIRST.md`, then treat this package's `source/` directory as the authoritative Company UI `3.0.0a1` baseline.

Continue actual Company UI development with a strict zero-regression policy. Do not replace the inherited v2 renderer or globally migrate existing routes merely to use v3 architecture. V3 runtime, data-session, adaptive-workspace, semantic-visualization, extension and persistence capabilities are additive/opt-in unless a tested migration is materially better.

Before modifying anything, read `RELEASE_MANIFEST.json`, `PHASE_46_V300A1_APPLICATION_PLATFORM_REPORT.json`, `PHASE_47_V300A1_BROWSER_UIUX_GATE_REPORT.json`, `BROWSER_UIUX_GATE.json`, `TARGET_RUNTIME_GATE_ATTEMPT.json`, and `context/20_ARCHITECTURE_STATE.md`.

Current hard gates: 672/672 source tests, governance 0/0, source certification 12/1 expected warning/0, visual coverage 183/183, browser-native UI/UX 43/43. Any development must keep those gates green or improve them. Installed NiceGUI 3.15.0 runtime, real 22-route server smoke, supported Chrome/Edge live browser matrix and human visual-baseline approval remain mandatory target-only gates before stable 3.0.0.
