# Package Integrity Audit

- Package: `/mnt/data/PHASE10_STAGE4_INDUSTRIAL_ROBOTICS_FACTORY_AUTOMATION_HOLDOUT.zip`
- Package type: `zip`
- Status: `review_required`
- Inspection run ID: `inspection-b5c2e1d0-e849-4463-9569-4f0ffe118eac`
- Package test run ID: `None`
- Validator version: `0.1.10`
- Inventory records: 181
- Hard fails: 0
- Warnings: 1
- Review-required findings: 3

## Findings
- `non_controlling_manifest_detected` — **warning** / warning [manifest]: Nested old/stale/reference manifest is outside package-level controlling scope.
- `unused_manifest_candidate` — **review_required** / review_required [manifest]: Additional root manifest candidate was not controlling.
- `manifest_hash_omission_applied` — **pass** / pass [manifest]: Eligible exact-role manifest hash omission was applied.
- `checksum_sidecar_verified` — **pass** / pass [checksum]: Sidecar SHA-256 matches target.
- `external_sidecar_required` — **review_required** / review_required [verification_metadata]: Final delivered package checksum remains correctly pending external sidecar verification.
- `external_sidecar_required` — **review_required** / review_required [verification_metadata]: Final delivered package checksum remains correctly pending external sidecar verification.
