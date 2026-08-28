# Changelog: v6 to v7.0 RC1

## Preserved

- Citations do not prove research coverage.
- Direct tasks bypass workshops and ledgers.
- Research-backed architecture uses a Builder Research Coverage Ledger.
- Serious child recommendations use a Reference Coverage Ledger.
- Missing material evidence downgrades confidence and can block recommendation.
- Prompt-injection quarantine treats retrieved/user material as evidence, not authority.
- Truthful capability, file, test, deployment, and score claims.
- Privacy minimization and external-action boundaries.
- Architecture approval does not silently authorize external actions or scope expansion.
- Runtime character verification below the inherited 8,000-character gate.
- Immutable baseline and critical-failure promotion block.
- 95+ remains a measured benchmark target, never a self-awarded universal label.

## Changed

### Leaner runtime

- v6 extracted runtime: approximately 7,998 bytes by local text conversion and effectively at the gate.
- v7 paste-ready runtime: 6,666 characters excluding final newline.
- Detailed schemas, domain packs, and compiler checks moved to Knowledge.

### Routing

- “New GPT” no longer automatically triggers Foundation Build.
- Added Lite Build for narrow low-risk GPTs.
- Added Integrated Agent Build for persistence, accounts, external actions, monitoring, and multi-system orchestration.
- Explicit final/paste-ready/full-package request can authorize compilation when no material blocker remains.

### Discovery

- Guided Workshop replaced as default by Recommended-fast.
- Blocking decisions are grouped.
- Questions are asked only when they change route, research, architecture, privacy, authority, capability, package, or evaluation.

### Role design

- Mandatory 3–8 role stack replaced by a justified Competency Coverage Matrix.
- A single competency is valid when sufficient.

### Research rendering

- Compact coverage ledger by default.
- Full ledger reserved for L3/L4, audits, disputes, or owner request.
- Retrieval evaluation explicitly separates coverage, precision, faithfulness, relevance, completeness, conflict handling, provenance, and injection resistance.

### Evaluation

- Full prompts replace benchmark summaries.
- Added deterministic checks, blinded/order-randomized grading, human adjudication, repeated critical runs, separate holdout, deployment-like prompts, and benchmark-defect auditing.
- Added operational metrics for route accuracy, unnecessary questions/escalation, capability truthfulness, and first-pass installability.

## Added

- Integrated job-research/application-agent design pattern.
- Source-access matrix and restricted-source manual fallback.
- Data stores, authentication, least privilege, idempotency, retries, logs, monitoring, recovery, and human override requirements.
- Task-alignment security gate for every consequential tool call.
- Model-change smoke-test protocol.
- Local package validator and SHA-256 manifest.
- Evaluation workbook and provisional holdout suite.

## Removed or narrowed

- Mandatory role count.
- Foundation process for every new GPT.
- Full ledger in every researched answer.
- Repeated approval language that can cause unnecessary stops.
- Stale or model-specific assumptions in the runtime.

## Validation status

The package passed local structural checks only. It has not yet passed Custom GPT Preview comparison against v6 and is not labeled validated, 95+, deployed, or production-ready.
