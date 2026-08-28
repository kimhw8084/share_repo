# Adaptive MyGPT Builder v7.0 RC1

**Artifact class:** Verified local release-candidate package  
**Use:** Create a new private Custom GPT for Preview validation  
**Status:** `RELEASE CANDIDATE - PREVIEW VALIDATION REQUIRED`  
**Build date:** 2026-07-27  
**Runtime character count:** 6666 characters, excluding the final newline  
**Inherited editor gate:** below 8,000 characters  
**Maintenance margin:** 1334 characters

## What v7 optimizes

v7 is designed to maximize the measured performance of MyGPT creation while preventing accidental regression. It preserves the strongest v6 controls—truthful capability claims, direct-task speed, research-coverage proof, privacy, external-action boundaries, artifact honesty, and baseline testing—while reducing instruction density and adding a dedicated Integrated Agent Build route.

## What is locally verified

- All required package files were created.
- Runtime character count is below the inherited 8,000-character gate.
- Benchmark IDs and required CSV fields are structurally validated.
- The package manifest includes SHA-256 hashes.
- No file, Preview run, deployment, integration, or 95+ score is claimed unless it exists.

## What is not yet verified

- Behavior inside your actual Custom GPT Preview.
- The recommended model visible in your account.
- Capability availability in your plan or workspace.
- Comparative v6-versus-v7 performance on your real prompts.
- External Apps, Actions, APIs, accounts, or automated workflows.

## Install in this order

1. Create a **new private GPT**; keep v6 unchanged as the stable baseline.
2. Paste `01_RUNTIME_INSTRUCTIONS_v7.txt` into Instructions.
3. Upload only these six Knowledge files:
   - `02_GOVERNANCE_AND_BASELINE_v7.md`
   - `03_BUILD_ROUTER_AND_OWNER_DISCOVERY_v7.md`
   - `04_RESEARCH_AND_EVIDENCE_OS_v7.md`
   - `05_DOMAIN_AND_AGENT_PATTERNS_v7.md`
   - `06_COMPILER_AND_PACKAGE_CONTRACT_v7.md`
   - `07_EVALUATION_AND_REGRESSION_SYSTEM_v7.md`
4. Apply settings from `08_SETTINGS_AND_INSTALL_GUIDE_v7.md`.
5. Add starters from `13_CONVERSATION_STARTERS_v7.txt`.
6. Run the smoke and development cases in `10_BENCHMARK_REGISTRY_v7.csv`.
7. Keep `11_PROVISIONAL_HOLDOUT_v7.csv` outside the GPT Knowledge and do not use it while editing the prompt.
8. Record raw outputs and results in `12_EVALUATION_WORKBOOK_v7.xlsx`.
9. Promote only after the release gates in Knowledge file 07 pass.

## Package map

- `00_README_FIRST_v7.md`: start here.
- `01_RUNTIME_INSTRUCTIONS_v7.txt`: paste-ready Instructions.
- `02`–`07`: six text-forward Knowledge files.
- `08_SETTINGS_AND_INSTALL_GUIDE_v7.md`: exact editor configuration and Preview workflow.
- `09_SCIENTIFIC_RESEARCH_REPORT_v7.md`: research basis and design rationale.
- `09B_RESEARCH_SOURCE_REGISTRY_v7.csv`: source-by-source evidence map.
- `10_BENCHMARK_REGISTRY_v7.csv`: executable development benchmark.
- `11_PROVISIONAL_HOLDOUT_v7.csv`: private release-candidate tests; do not upload.
- `12_EVALUATION_WORKBOOK_v7.xlsx`: run log and scorecard.
- `13_CONVERSATION_STARTERS_v7.txt`: suggested starters.
- `14_CHANGELOG_v6_to_v7.md`: preserved, changed, and added behavior.
- `15_DELIVERY_MANIFEST_v7.csv`: asset status and verification.
- `16_VALIDATE_PACKAGE_v7.py`: structural validation script.
- `manifest.json`: hashes and package metadata.

## Promotion statement

Do not label v7 as superior, 95+, production-ready, or validation-grade until you have executed Preview tests, preserved raw outputs, compared the same prompts against v6, reviewed critical cases, and approved the release.
