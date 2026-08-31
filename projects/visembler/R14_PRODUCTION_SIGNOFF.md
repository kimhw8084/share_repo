# Company UI Visualizer R14 — Production Signoff

R14 is the semantic-layout and authoring-correctness release on top of the R13 retained-editor integration and R12.2 runtime hardening. It preserves Company UI runtime authority, frozen Visualizer 97.1 authority, and Golden Connector v5.

## Certified source/browser gates

- Python regression estate: **710/710 PASS**.
- Company UI governance: **0 errors / 0 warnings**.
- Functional retained-editor Chromium matrix: **38/38 PASS**.
- Legacy visual/layout compatibility matrix: **44/44 PASS**.
- R14 hard browser gate: **134/134 PASS** across 1600×1000, 1440×900, and 1280×800, with editor zoom and browser-scale matrices.
- Catalog render audit: **248/248**, with **248 unique normalized structures** and zero duplicate groups.
- Content torture: **248/248 elements, 992/992 cases PASS**, including normal/long/zero/empty states.
- Performance certification: **16/16 PASS**.
- Browser console errors: **0**. Browser page errors: **0**.
- Capability matrix: **248 elements / 17 engines / 26 semantic inspector schemas / 166 thumbnail grammars**.
- Wheel/source byte parity: **PASS**.
- Frozen Visualizer authority: **123/123 files byte-identical**, **27/27 authority commands PASS**.
- Golden Connector v5 SHA-256: `d8ebd4378f01b7c52a7a4be57c578c22adf29b899cc08a370cf084881195343e`.

## R14 product corrections

R14 fixes transient alignment-guide lifecycle, semantic Smart intrinsic sizing and safe-hull containment, stale direct-edit focus mappings, viewport/scene geometry, command eligibility, and preflight containment. Smart/Guided/Free now have distinct contracts. The library separates Elements and Presets, adds semantic thumbnails plus Recent/Favorites/Recommended organization, and moves shortcuts into Help/Commands. The inspector adds per-variant metric semantics and spreadsheet-like table editing; timeline/diagram/image workflows expose actionable authoring controls and functional empty states.

PowerPoint integration preserves editable semantic objects where supported and embeds the exact canonical element payload in shape metadata. Numeric zero, string `"0"`, blank, and `null` remain distinct; sequence-only timelines keep null dates. Dense single-slide export fails closed rather than silently truncating.

## Frozen authority

The complete frozen Visualizer vendor tree was compared to the attached R13 source authority and is byte-identical across all 123 files. The 27 frozen commands were rerun. The host exhibited a Chromium cleanup hang only when the frozen 248-browser test followed the previous browser tests in one wrapper process, so certification was partitioned as commands 1–25, 26, and 27. All 27 actual commands passed independently and the vendor tree remained unchanged.

## Runtime gate

This packaging sandbox does not contain NiceGUI 3.15.0. No fake runtime pass is claimed. `./setup.sh` installs the exact dependencies and fails closed unless the real NiceGUI API, bundled-source application construction, installed-wheel application construction, storage-secret flow, runtime contract, and `python app.py` HTTP smoke all pass. `./test_linux.sh` then runs the exhaustive browser/restart/authority estate.
