# Settings and Installation Guide v7

**Package status:** Release candidate; Preview validation required  
**Platform verification date:** 2026-07-27

## 1. Create a separate GPT

- Keep v6 unchanged as the stable comparison baseline.
- Create a new private GPT named: **Adaptive MyGPT Builder v7 - Development**.
- Build/edit on the ChatGPT web experience.
- Do not publish or replace v6 until the v7 release gates pass.

## 2. Configure fields

### Name

`Adaptive MyGPT Builder v7`

### Description

`Designs, researches, evaluates, and compiles high-performance Custom GPTs and integrated AI-agent architectures with truthful capability boundaries, evidence-coverage proof, privacy controls, and non-regression testing.`

### Instructions

Paste the complete contents of `01_RUNTIME_INSTRUCTIONS_v7.txt`.

Verified local count: **6666 characters**, excluding the final newline.

### Knowledge

Upload these six files only:

1. `02_GOVERNANCE_AND_BASELINE_v7.md`
2. `03_BUILD_ROUTER_AND_OWNER_DISCOVERY_v7.md`
3. `04_RESEARCH_AND_EVIDENCE_OS_v7.md`
4. `05_DOMAIN_AND_AGENT_PATTERNS_v7.md`
5. `06_COMPILER_AND_PACKAGE_CONTRACT_v7.md`
6. `07_EVALUATION_AND_REGRESSION_SYSTEM_v7.md`

Do not upload the benchmark, holdout, research report, workbook, manifest, or install guide as Knowledge. Keeping evaluation prompts outside Knowledge reduces test leakage.

### Recommended model

Select the strongest reasoning-oriented model available in your GPT editor that supports the required capabilities. Do not hardcode the runtime to a model name. Users may switch models, and unavailable models may be replaced automatically; rerun smoke tests after a model change.

### Capabilities

- **Web Search:** ON.
- **Code Interpreter & Data Analysis:** ON.
- **Canvas:** optional; ON if you want longer drafting or structured editing.
- **Image Generation:** optional; ON only when child-GPT packages commonly need icons or visual assets.
- **Apps:** OFF for the core Builder.
- **Actions:** OFF for the core Builder.

The Builder should design Apps/Actions architectures for child systems but should not itself carry unrelated credentials or integrations. A GPT can use Apps or Actions, not both at the same time; verify the current editor before any integrated child build.

### Sharing

- Private during development.
- Share only after validation and privacy review.
- Public publication requires a separate review of description, privacy, actions/apps, external domains, and user-facing limitations.

## 3. Conversation starters

Use the four starters in `13_CONVERSATION_STARTERS_v7.txt` or shorter variants that reflect your highest-value workflows.

## 4. First Preview checks

Run these in order and save raw outputs:

1. B01 Direct-task bypass.
2. R02 Foundation route.
3. R03 Integrated Agent route.
4. B02 Build authorization.
5. B05 Fake-asset pressure.
6. B08 Injection quarantine.
7. B09 Capability alignment.
8. B16 Employment truthfulness.
9. B17 Health boundary.
10. P04 Full-package compile.

Then run all smoke cases in `10_BENCHMARK_REGISTRY_v7.csv`.

## 5. Comparison protocol

- Use the same prompt and conversation history in v6 and v7.
- Keep enabled capabilities equivalent where possible.
- Save full raw outputs.
- Blind version labels before qualitative grading.
- Randomize answer order and repeat pairwise grading with reversed order.
- Record critical failures before weighted scores.

## 6. Installation acceptance checklist

- Instructions pasted without truncation.
- Six Knowledge files uploaded and readable.
- Web Search and Data Analysis enabled.
- Apps and Actions both off in the core Builder.
- Conversation starters added.
- GPT is private.
- Runtime count rechecked after paste.
- First ten Preview cases saved.
- No promotion claim made.

## 7. Current official platform facts used in this guide

As of the verification date, OpenAI's current GPT documentation states that:

- Instructions define behavior; Knowledge supplies reference material.
- Clear multi-step trigger/action structure, positive concrete instructions, and brief examples are recommended.
- Preview should be used with realistic prompts before sharing.
- Apps and Actions are mutually exclusive.
- GPTs do not use saved memory, account custom instructions, or previous GPT conversations; each GPT conversation starts fresh.
- Users may switch from the recommended model, and retired models may be replaced automatically.

Reverify these facts when installing after a platform update.
