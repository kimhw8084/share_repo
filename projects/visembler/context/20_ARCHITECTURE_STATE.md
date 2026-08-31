# V3 Architecture State

Company UI v3 is an additive application platform over the hardened v2 renderer/design constitution.

Implemented pillars:

1. `ApplicationRuntime` / `WorkspaceRuntime` ownership kernel.
2. Typed namespaced state, atomic transactions, defensive reads, revision history, rollback, undo/redo.
3. Unified immutable `Dataset` + `DataSession` engine for shared table/chart/KPI/filter state and indexed large-data filtering.
4. Adaptive workspace grid with deterministic move/resize/collision/compaction/responsive derivation and snapshot restore.
5. JSON application/workspace persistence across runtime state, panel geometry and shared data filters.
6. Semantic visualization planning reusing the existing certified visualization renderer stack.
7. Governed extension registry for components, data sources, commands, visualizations and workspace panels.
8. Runtime diagnostics and performance/lifecycle ownership.
9. RC5 lifecycle/async/DataTable/overlay/chart/pathological-data hardening retained intact.
10. Phase 47 browser hardening: final mobile 44px interactive targets, cascade-safe reduced motion, and mobile-header metadata suppression.

The compatibility floor is the inherited v2 visual/interaction contract. Existing routes are not required to migrate to v3 runtime/workspace APIs.
