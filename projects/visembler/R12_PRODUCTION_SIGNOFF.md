# Company UI Visualizer R12.2 — Production Signoff

R12.2 is an application-level hardening release. It does not infer or modify company Kubernetes topology, ingress, Redis, replica count, storage class, or network policy.

## Confirmed runtime defect fixed

R11 used NiceGUI user storage for personal presets but bypassed Company UI's governed runtime adapter, allowing `ui.run()` to start without the required `storage_secret`.

R12.2 has one runtime path:

```text
app.py
→ company_ui.products.visualizer.cli.main()
→ build_application()
→ Visualizer runtime resolver
→ Company UI RuntimeConfig
→ NiceGUIRuntimeAdapter.run(environ=resolved_env)
→ ui.run(... storage_secret=resolved_secret ...)
```

Production fails closed if `COMPANY_UI_STORAGE_SECRET` is absent. Non-production creates one strong local secret atomically and reuses it across restarts. A 24-way concurrent-start test confirms all local resolvers converge on the same persisted secret.

## Application hardening included

- atomic report write (`fsync` + replace)
- process-level repository transaction lock
- revision/CAS enforcement across repository instances
- idempotent semantic commit IDs
- stale/out-of-order conflict responses
- corrupt-report quarantine
- revision-safe rename/delete/blank cleanup
- strict bridge version/event/size validation
- high-frequency pointer traffic prohibited from the Python bridge
- canonical report-model size limit
- embedded-image validation and model preflight
- PNG/JPEG/WebP content validation
- image byte/dimension/pixel-bomb protection
- invalid/SVG active-image rejection
- PPTX traversal rejection
- duplicate ZIP-entry rejection
- suspicious compression-ratio/expanded-size rejection
- editable PPTX export round-trip coverage
- server-backed personal preset normalization/limits/corruption isolation
- 248-element library / 17 engines
- semantic inspectors for all 17 engines
- typed spreadsheet paste preserving null vs numeric zero
- sequence-only timeline null-date preservation
- Ctrl/Cmd+V image workflow
- Smart/Guided/Free geometry with governed 14 px spacing law
- browser-local high-frequency pointer/resize/hover behavior
- inspector reflow and host replacement/rebind lifecycle
- content-hashed editor assets and recursive module-graph verification
- Company UI mobile drawer open/close uses supported browser-side NiceGUI `js_handler`

## Release evidence produced in this build environment

- Python regression estate: 695 collected tests, 100% completed successfully
- Company UI governance: 0 errors / 0 warnings
- R12.2 Chromium application matrix: 38/38 PASS
- Chromium console errors: 0
- Chromium page errors: 0
- recursive Visualizer browser module graph: PASS, no missing targets
- source contract: PASS
- wheel/source byte parity: PASS
- frozen Visualizer vendor: 123/123 files unchanged
- Visualizer 97.1 frozen authority suite: 27/27 PASS on a temporary copy
- frozen vendor unchanged by authority execution: PASS
- Golden Connector Engine v5 SHA-256: `d8ebd4378f01b7c52a7a4be57c578c22adf29b899cc08a370cf084881195343e`

## Real NiceGUI target gate

NiceGUI is intentionally not installed in this packaging sandbox. R12.2 does not substitute a fake runtime and claim success. `setup_linux.sh` is therefore fail-closed and, after installing `nicegui==3.15.0`, requires:

1. real NiceGUI API verification,
2. real application construction from bundled source,
3. real application construction from the installed wheel,
4. Company UI runtime contract/doctor,
5. exact `python app.py` HTTP startup,
6. generation/persistence of the local storage secret.

`test_linux.sh` additionally performs a real browser restart test which writes both a report edit and an `app.storage.user` personal preset, terminates the app, restarts it with the same data/browser context, and requires both to survive with the same storage secret.

## R12.2 real-runtime hotfix

A real NiceGUI 3.15 runtime traceback showed that the Visualizer page builder accessed `app.storage.tab` before the WebSocket client connection existed. R12.2 removes tab-storage access from page construction. The last-open report preference is now stored in request-safe `app.storage.user`, which is already the authority used for personal presets. Report data and revision state remain repository-scoped; changing this preference scope does not merge report editor state across tabs. `verify_visualizer_source_contract.py` now fails any release that reintroduces `NiceGUIStateServices.tab_store()` in the Visualizer page builder.

## R12.2 setup-dispatch/runtime-smoke hotfix

A real macOS setup run showed that root `setup.sh` still dispatched to the legacy Company UI framework-lab `setup_mac.sh`. That installer ran `company-ui runtime-smoke`; all live-lab routes returned HTTP 200, but the harness intentionally stopped NiceGUI with SIGINT. Python 3.13 + uvloop surfaced the controlled stop as `CancelledError` followed by `KeyboardInterrupt`, and `set -e` aborted setup.

R12.2 replaces the root macOS installer with the Visualizer product installer used by the hardened release. Both product installers now execute `tools/live_app_http_smoke.py` against the exact root `app.py`. The framework runtime-smoke helper also uses SIGTERM for intentional shutdown. Five regression tests lock the dispatcher, macOS product setup, Linux product setup, shutdown signal, and canonical run/setup instruction.
