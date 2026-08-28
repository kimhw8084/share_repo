# Package Integrity Audit

- Package: `/mnt/data/PHASE10_STAGE4_UNSEEN_ROBOTICS_HOLDOUT_MIGRATION.zip`
- Package type: `zip`
- Status: `review_required`
- Inspection run ID: `inspection-64fc4d3c-c75c-492c-b645-536197123cbc`
- Package test run ID: `None`
- Validator version: `0.1.10`
- Inventory records: 346
- Hard fails: 0
- Warnings: 1
- Review-required findings: 2

## Findings
- `non_controlling_manifest_detected` — **warning** / warning [manifest]: Nested old/stale/reference manifest is outside package-level controlling scope.
- `manifest_hash_omission_applied` — **pass** / pass [manifest]: Eligible exact-role manifest hash omission was applied.
- `checksum_sidecar_verified` — **pass** / pass [checksum]: Sidecar SHA-256 matches target.
- `external_sidecar_required` — **review_required** / review_required [verification_metadata]: Final delivered package checksum remains correctly pending external sidecar verification.
- `external_sidecar_required` — **review_required** / review_required [verification_metadata]: Final delivered package checksum remains correctly pending external sidecar verification.
