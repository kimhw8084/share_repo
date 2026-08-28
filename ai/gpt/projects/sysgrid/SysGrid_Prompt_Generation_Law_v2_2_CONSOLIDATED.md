# SysGrid Prompt Generation Law v2.2 — CONSOLIDATED

Status: **ACTIVE CONSOLIDATED LAW**

This file consolidates and supersedes the active Prompt Generation Law set:

```text
SysGrid_Prompt_Generation_Law_v2_0.md
SysGrid_Prompt_Generation_Law_v2_1_Workflow_Amendment.md
SysGrid_Prompt_Generation_Law_v2_2_Zero_Divergence_Token_Economy.md
```

Keep this consolidated file plus:

```text
SysGrid Linear SOP — Zero-Deviation Operating Law.md
```

Archive/remove the separate v2.0, v2.1, and v2.2 amendment files from active project context after adoption.

Authority priority:

```text
1. SysGrid Linear SOP — Zero-Deviation Operating Law
2. This consolidated Prompt Generation Law v2.2
```

If this law conflicts with the SysGrid Linear SOP, the SOP wins.

Core correction in this consolidation:

```text
The user runs the commit/push/zip utility script.
Copyable worker prompts must not include git, commit, push, zip, commit-push-zip, or upload-zip instructions unless the user explicitly asks for those lines.
```

---

## 0. Supreme Rule

A prompt is not trusted because it is long, forceful, or detailed.

A prompt is trusted only when:

```text
1. The objective is measurable.
2. The source of truth is explicit.
3. The failure class is known.
4. The scope is narrow.
5. The proof artifacts are mandatory.
6. The next-action rule is conditional.
7. The prompt family has not already failed twice.
8. The result can be independently reviewed from the returned artifact.
```

If any condition is missing, the next action is not implementation. The next action must be discovery, verification, command-only proof, recovery, or stop.

---

## 1. Purpose and Authority

This law governs the SysGrid AI implementation loop:

```text
User / Linear goal
→ ChatGPT prompt generation
→ Coding AI implementation
→ Zip/result return
→ ChatGPT review
→ Score
→ Lesson learned
→ Conditional next action
→ Retry / pass / stop
```

This law exists to prevent:

```text
same-style prompt retry after repeated failure
normal continuation after regression
PASS without proof
Done without zip review
Done without lesson
artifact failure handled by prose prompt
scope bloat
score confusion
model blame before process diagnosis
```

This law does not replace the SysGrid Linear SOP. If this law conflicts with the SysGrid Linear SOP, the SOP wins.

---

## 2. Workflow Control Loop

Every SysGrid implementation cycle must follow:

```text
Goal
→ Prompt
→ Code/result
→ Zip/artifact
→ Review
→ Score
→ Lesson
→ Conditional next action
→ Retry / pass / stop
```

No skipping:

```text
No zip = no final review.
No review = no Done.
No lesson = no next prompt.
No next-action rule = no retry.
No proof = no PASS.
```

Every cycle must record:

```text
Active issue:
Run:
Iteration number:
Prompt type:
Prompt summary:
Returned artifact:
Verdict:
Official cumulative run score:
Iteration execution score:
What worked:
What failed:
Lesson learned:
Next allowed action:
Forbidden next action:
```

Every prompt → result → review cycle must have an iteration number. If the iteration number is unknown, stop and classify the state before generating any prompt.

---

## 3. Prompt Readiness Gates

Before generating any prompt, answer every gate.

### 3.1 Objective Gate

Required:

```text
Objective:
One-sentence measurable end state:
```

Illegal unless converted into measurable acceptance criteria:

```text
fix it
make it better
continue
do the next thing
make it similar
```

### 3.2 Task-Type Gate

Allowed task types:

```text
Discovery-only
Implementation
Targeted bug fix
Recovery-only
Report-only
Command-only shell
Verification-only
Audit-only
Refactor
Scope-splitting
Test-generation
Manual-validation request
Law-rewrite
Stop / no prompt
```

If task type is unclear, use discovery-only.

### 3.3 Source-of-Truth Gate

A prompt may not proceed to implementation unless source of truth is known.

Valid source of truth examples:

```text
MonitoringGrid.tsx
verified baseline zip
known working implementation
accepted issue description
specific commit/diff
golden UI standard
specific failing test
specific user-confirmed behavior
```

Illegal unless the exact source is named:

```text
make it like before
make it like Monitoring
fix based on vibes
probably should work
```

### 3.4 Facts Gate

Facts must be separated:

```text
Works:
Fails:
Unknown:
```

Rules:

```text
Never mix unknown with facts.
Never let the worker solve guessed problems.
Never convert suspicion into source of truth.
```

### 3.5 Scope Gate

A prompt must target one coherent objective.

Allowed:

```text
Fix shift-selection range logic only.
Restore saved-view localStorage behavior only.
Create missing report file only.
```

Forbidden:

```text
Fix saved views, shift selection, row menu, and finish shared runtime.
```

### 3.6 Risk Gate

If the task can damage behavior, shared contracts, routes, Git state, artifact discipline, or user data, the prompt must include:

```text
Inspect first.
Allowed files.
Forbidden files.
Source of truth.
Root-cause explanation before patching.
Verification commands.
Stop conditions.
```

### 3.7 Proof Gate

Every prompt must define what proof is required before the worker can return.

Proof may include:

```text
grep proof
no-match grep proof
test output
exit code
git status
git diff --check
zipinfo
test -s report file
manual UI validation status
baseline diff
```

If no proof is specified, no PASS is possible.

---

## 4. Failure Taxonomy

Before generating the next prompt, classify the prior result.

| Failure class | Definition | Required next action |
|---|---|---|
| Code logic failure | Implementation logic is wrong, but no known-good behavior regressed outside scope | Targeted bug fix |
| Regression / WORSE | A known working behavior got worse, disappeared, or changed incorrectly | Recovery-only |
| Artifact failure | Required report, zip, proof file, or generated artifact is missing | First time: report/verification-only. Repeated: command-only shell |
| Zip packaging failure | Zip exists but has wrong root/content/path or unsafe included files | Command-only shell with zipinfo proof |
| Verification failure | Claims made without exact command output, exit codes, blocker details, or manual validation status | Verification-only |
| Environment blocker | Verification command cannot run due missing deps, permissions, or tools | Record exact blocker, no false pass |
| Source-of-truth failure | Expected behavior or baseline is unclear | Discovery-only |
| Scope failure | Prompt/result spans too many unrelated surfaces | Scope-splitting / one-surface prompt |
| Context-loss failure | Active issue, iteration, verdict, lesson, source, or scope is unknown | Context rebuild / discovery-only |
| Prompt-family failure | Same objective fails twice without improvement, or same pattern repeats after targeted prompt | Discard or replace prompt family |
| Scoring failure | Cumulative score and iteration score are confused | Correct scoring before next prompt |
| False-success failure | Worker claims done but artifact, code, command, or zip proof contradicts claim | FAIL review and lesson extraction |

---

## 5. Conditional Routing Engine

### 5.1 Verdict Routing

```text
IF verdict = PASS
THEN record lock, lesson, and next goal.
FORBIDDEN: reopen same work without new evidence.
```

```text
IF verdict = PARTIAL and improved
THEN one narrower correction is allowed.
FORBIDDEN: broad rewrite.
```

```text
IF verdict = PARTIAL and not improved
THEN change prompt type or split scope.
FORBIDDEN: same-style retry.
```

```text
IF verdict = FAIL
THEN classify failure before next prompt.
FORBIDDEN: automatic retry.
```

```text
IF verdict = WORSE
THEN recovery-only.
FORBIDDEN: normal correction, feature continuation, new abstraction.
```

### 5.2 Two-Try Escalation

```text
IF same objective fails twice
THEN prompt family is invalid.
THEN replace prompt type or discard.
FORBIDDEN: third same-style retry.
```

```text
IF iteration execution score drops
THEN stop and classify failure.
THEN recover if regression.
FORBIDDEN: continue normal implementation.
```

```text
IF score stays flat twice on same objective
THEN prompt/process is defective.
THEN redesign prompt type.
FORBIDDEN: rewording only.
```

### 5.3 Artifact Routing

```text
IF required report is missing once
THEN report-only or verification-only is allowed.
```

```text
IF required report is missing twice
THEN command-only shell.
FORBIDDEN: another prose coding prompt.
```

```text
IF zipinfo does not show required report
THEN do not upload.
THEN fix artifact packaging with command-only shell.
```

```text
IF git ls-files '*.zip' shows a zip
THEN fail Git discipline.
THEN remove/untrack/fix packaging.
FORBIDDEN: continue implementation.
```

### 5.4 Verification Routing

```text
IF command output is missing
THEN verification-only.
FORBIDDEN: PASS.
```

```text
IF manual UI validation is required but missing
THEN no PASS.
THEN record “manual UI not run” or run manual validation.
```

```text
IF typecheck/build is blocked
THEN record exact command, blocker, exit code, and “CLI proof limited.”
FORBIDDEN: claim passed.
```

### 5.5 Scope Routing

```text
IF prompt includes multiple runtime surfaces
THEN split.
FORBIDDEN: broad mixed prompt.
```

```text
IF broad refactor fails
THEN one-surface prompt.
FORBIDDEN: bigger refactor prompt.
```

### 5.6 Source-of-Truth Routing

```text
IF source of truth is unclear
THEN discovery-only.
FORBIDDEN: implementation.
```

### 5.7 Known Bug Routing

```text
IF bug is discovered outside current scope
THEN record it.
THEN decide whether severity elevates it.
FORBIDDEN: silently fix unrelated bug inside current prompt.
```

```text
IF bug affects multiple workspaces
THEN classify as shared interaction or shared runtime bug.
FORBIDDEN: treat as one local view bug.
```

---

## 6. Prompt-Type Templates

### 6.1 Discovery-Only Prompt

Use when source, scope, or failure class is unknown.

Must include:

```text
Inspect only.
Do not edit.
Identify source of truth.
List working facts.
List failing facts.
List unknowns.
Recommend next prompt type.
```

### 6.2 Implementation Prompt

Use only when all readiness gates pass.

Must include:

```text
Session/reset line.
Active issue.
Iteration number.
Objective.
Source of truth.
Allowed files.
Forbidden files.
Required workflow.
Verification commands.
Artifact requirements.
PASS/PARTIAL/FAIL/WORSE criteria.
Final response format.
```

### 6.3 Targeted Bug Fix Prompt

Use for isolated behavior defect.

Must include:

```text
Broken behavior.
Expected behavior.
Exact source file or search target.
Regression tests or grep proof.
No unrelated refactor.
```

### 6.4 Recovery-Only Prompt

Use after WORSE.

Must include:

```text
Previous known-good baseline.
Exact regression.
Files allowed for recovery.
No new feature work.
No revised abstraction.
Proof regression is gone.
Proof unrelated areas unchanged.
```

### 6.5 Report-Only Prompt

Use only for first missing-report correction.

Must include:

```text
Do not edit source.
Create exact report filename.
Record exact checks.
Prove report exists with test -s.
Prove archive contains report.
```

If report-only fails twice, switch to command-only.

### 6.6 Command-Only Shell Prompt

Use for repeated artifact or packaging failure.

Must include only shell commands or a shell-scriptable block.

Must include:

```text
cd correct directory
cat > REPORT.md
test -s REPORT.md
zip from outside repo
zipinfo grep report
git ls-files '*.zip'
stop if proof fails
```

### 6.7 Verification-Only Prompt

Use when code may be correct but proof is insufficient.

Must include:

```text
Do not edit source.
Run exact verification commands.
Capture output and exit codes.
Record blocked commands exactly.
Return report.
```

### 6.8 Audit-Only Prompt

Use when review or diagnosis is required before change.

Must include:

```text
Inspect files.
Map behavior.
Find root cause candidates.
No edits.
Recommend next prompt type.
```

### 6.9 Scope-Splitting Prompt

Use when objective is too broad.

Must include:

```text
Break objective into smallest coherent slices.
Rank by dependency and risk.
Select only next slice.
Do not implement.
```

### 6.10 Stop / No-Prompt

Use when:

```text
active issue unclear
source unclear and discovery forbidden
same prompt family failed and no new strategy exists
Linear gate unclear
user approval required
```

---

## 7. Artifact and Zip Law — Consolidated v2.2

The uploaded zip remains the review source of truth.

```text
No zip = no final code review.
No review = no Done.
```

However, prompt bodies must not instruct the worker to run the user's packaging utility.

The user runs the commit/push/zip utility script.

Prompts may require artifact placement and review evidence, but must not waste tokens telling the worker to:

```text
run git
commit
push
zip
run commit-push-zip
use the standard commit-push-zip workflow
upload the zip
```

Allowed in prompts:

```text
Required artifact: frontend/<file>.md
Required source change: <file path>
Uploaded zip is review source of truth.
```

For non-code artifact tasks:

```text
Create the smallest useful artifact inside frontend/.
Keep it minimal.
Do not rely on terminal output as proof.
```

For code tasks:

```text
Do not create non-code report artifacts unless blocked or explicitly required.
Required proof must be reviewable from the uploaded zip or source files.
```

ChatGPT review must verify from the uploaded zip:

```text
1. Required artifact exists, if applicable.
2. Required source change exists, if applicable.
3. No unrelated files changed.
4. Archive is clean.
5. Scope matches the prompt.
6. PASS/PARTIAL/FAIL/WORSE can be assigned from artifact evidence.
```

If the zip cannot prove the result, the review cannot PASS.

## 8. Verification Law

Every verification report must include:

```text
Command:
Exit code:
Output summary:
PASS/FAIL/BLOCKED:
```

If command is blocked:

```text
Command:
Blocker:
Exit code:
CLI proof limited.
No dependency mutation performed.
```

If behavior is visual or interaction-based, manual UI status is required.

Allowed statuses:

```text
Ran and passed.
Ran and failed.
Not run.
Blocked with reason.
```

Forbidden:

```text
looks fine
should work
not applicable without reason
```

PASS is forbidden if:

```text
zip not reviewed
required report missing
manual UI required but absent
known regression not checked
source-of-truth comparison missing
verification output missing
lesson missing
```

---

## 9. Scoring Law

Every review must show:

```text
Official cumulative run score:
Iteration execution score:
```

Official cumulative run score measures progress against fixed run acceptance criteria. It changes only when actual run acceptance state changes.

Iteration execution score measures how well the current prompt was executed. It may drop sharply for:

```text
missing report
wrong zip
ignored proof
scope drift
verification gap
```

even if cumulative source state stays stable.

Forbidden:

```text
Compare iteration score to cumulative score as if same thing.
Claim project quality fell from one score to another without score-type distinction.
```

Score triggers:

```text
IF iteration score drops
THEN classify failure before next prompt.
```

```text
IF same-objective iteration score fails to improve twice
THEN prompt family invalid.
```

```text
IF cumulative score drops due regression
THEN recovery-only.
```

---

## 10. Lesson-Learning Law

Every review must produce:

```text
What worked:
What failed:
Root cause:
Lesson learned:
Next prompt rule:
```

If no lesson is recorded, no next prompt is allowed.

Bad lesson:

```text
Be more careful next time.
```

Valid lesson:

```text
IF required report is missing twice
THEN switch to command-only shell creation
NOT prose report prompt.
```

A lesson is invalid unless it changes at least one of:

```text
prompt type
scope
proof requirement
forbidden action
routing rule
discard condition
```

Repeated lesson rule:

```text
IF same lesson appears twice
THEN prompt/process was not changed enough.
THEN discard or replace prompt family.
```

---

## 11. Known SysGrid Regression Guard Library

Known SysGrid regression patterns must be guarded explicitly.

Every relevant prompt must include exact proof that the known regression did not recur.

Guard format:

```text
Guard name:
Why it exists:
Command/proof:
Expected result:
Failure action:
```

### 11.1 Saved-View Active localStorage Cleanup Guard

Why:

```text
A prior iteration regressed active saved-view deletion by removing direct localStorage cleanup.
```

Proof:

```bash
rg -n "removeItem\(MONITORING_ACTIVE_VIEW_KEY\)" src/components/MonitoringGrid.tsx
```

Expected:

```text
At least one active-delete cleanup path must be present.
```

Failure action:

```text
Classify as WORSE if this behavior was previously present and now missing.
Route to recovery-only.
```

### 11.2 Removed Saved-View Abstraction Guard

Why:

```text
A prior saved-view abstraction introduced useOperationalSavedViews and persistedActiveViewId/persistedViews, then recovery removed them.
```

Proof:

```bash
rg -n "useOperationalSavedViews|persistedViews|persistedActiveViewId" src
```

Expected:

```text
No output unless a future approved prompt explicitly reintroduces this abstraction.
```

Failure action:

```text
If unintentionally reintroduced, classify as regression risk and stop before continuation.
```

### 11.3 Row-Menu Opener/Setter Guard

Why:

```text
A previous row-menu regression risk confused a state setter with a semantic open action.
The law must prevent aliasing openRowActionMenu directly to setRowActionMenu or equivalent setter-only wiring.
```

Required-absent proof:

```bash
rg -n "openRowActionMenu:\s*setRowActionMenu|openRowActionMenu\s*=\s*setRowActionMenu|openRowActionMenu:\s*\w*Set\w*|openRowActionMenu\s*=\s*\w*Set\w*" src
```

Expected:

```text
No output.
```

Required semantic proof:

```bash
rg -n "openRowActionMenu" src/components src
```

Expected:

```text
Open action should be semantic and preserve row/action context, not be a raw setter alias.
```

Failure action:

```text
If raw setter alias appears, classify as runtime interaction regression.
If it affects active behavior, route to recovery-only or targeted bug fix depending on whether known-good behavior was broken.
```

### 11.4 Shift-Selection Predicate Guard

Why:

```text
User confirmed shift selection is buggy across Monitoring, Services, and External.
Known suspicious predicate: rowIndex >= start && rowIndex >= end.
```

Required-absent proof:

```bash
rg -n "rowIndex\s*>=\s*start\s*&&\s*rowIndex\s*>=\s*end" src
```

Expected after fix:

```text
No output.
```

Required behavior rule:

```text
Shift range must include only displayed/sorted/filtered rows with rowIndex between min(anchor,current) and max(anchor,current), inclusive.
```

Required code invariant:

```text
lower = Math.min(anchorIndex, currentIndex)
upper = Math.max(anchorIndex, currentIndex)
include row only if rowIndex >= lower && rowIndex <= upper
```

or equivalent displayed-row traversal that proves the same invariant.

Failure action:

```text
If bad predicate remains after a prompt claiming to fix selection, classify as FAIL.
If a known working selection behavior regresses, classify as WORSE.
```

### 11.5 Cross-Workspace Shift-Selection Guard

Why:

```text
The bug is not local if Monitoring, Services, and External are affected.
```

Required proof:

```text
Prompt/review must inspect shared interaction layer first.
Prompt/review must identify all consuming workspaces.
Prompt/review must state whether Monitoring, Services, and External share the same selection/range path.
```

Expected:

```text
One shared fix or shared helper path preferred.
No copy-paste local patch unless evidence proves shared path is impossible.
```

Failure action:

```text
If the prompt fixes only one workspace while bug is shared, classify as PARTIAL or FAIL depending on remaining impact.
```

---

## 12. Cross-Workspace Severity Escalation Rule

```text
IF user confirms a bug affects Monitoring + Services + External
THEN classify as cross-workspace shared-interaction defect.
THEN pause lower-priority refactor continuation.
THEN next allowed prompt must be targeted bug fix, discovery-only root-cause prompt, or explicit scheduling decision.
FORBIDDEN: continue saved-view/runtime refactor as if bug is local or deferred silently.
```

Severity classes:

| Class | Definition | Required action |
|---|---|---|
| Local bug | One workspace only | targeted local fix allowed |
| Shared interaction bug | Same behavior broken across multiple workspaces | shared-root diagnosis first |
| Shared runtime regression | shared layer broke behavior | recovery or targeted shared fix |
| Artifact-only issue | source safe, report/zip failed | command-only/report-only |
| Blocking user-confirmed defect | user confirms severe active bug | pause unrelated continuation |

User-confirmed bug rule:

```text
IF user asks “were you aware?” about a real active bug
AND the bug affects core interaction behavior
THEN classify as high-priority review defect.
THEN record it.
THEN do not bury it as a minor deferred issue.
```

Deferred bug rule:

```text
A bug may be deferred only if:
1. It is explicitly recorded.
2. Its severity is stated.
3. Its affected workspaces are stated.
4. The next prompt does not conflict with it.
5. The user has not elevated it.
```

If user elevates it, it is no longer silently deferred.

---

## 13. Proof-Run Amendment Log Requirement

Every proof run that produces REWRITE must create an amendment log.

Required format:

```text
Draft tested:
Proof suite:
Score:
Hard gates passed:
Hard gates failed:
Case weaknesses:
Required amendments:
Reason each amendment exists:
New proof cases added:
Promotion decision:
```

A rewrite must only change what the proof run exposed.

Forbidden:

```text
Rewrite entire law because of style preference.
Add broad unrelated theory.
Add more words without new gate/proof.
Remove passing hard gates.
```

Each amendment must map to at least one:

```text
SG case
SysGrid failure
User instruction
SOP rule
proof weakness
```

If it maps to none, it does not belong in the law.

---

## 14. Project-File Promotion Rule

No draft may be added to project files merely because it is complete.

A law version may enter project files only if:

```text
1. It has passed SG-01 through SG-10 proof run.
2. All hard gates passed.
3. Total score >= 95.
4. User approves promotion.
5. Linear records the promotion decision.
```

Allowed statuses:

```text
DRAFT
REWRITE
PROVEN
PROMOTED
DISCARDED
```

Only `PROVEN` or `PROMOTED` can be used as project law.

Use ban:

```text
IF law status is DRAFT or REWRITE
THEN do not use it for real OUT-8 coding prompts.
```

Promotion record must include:

```text
Law version:
Proof score:
Hard gate result:
Amendments since prior draft:
User approval:
Date:
Active issue:
```

---

## 15. Law Self-Test / First-Use Validation

Prompt Generation Law v2.0 passed the SG-01 through SG-10 proof suite.

Required first-use validation:

```text
The first real OUT-8 prompt generated from this law must be reviewed as a validation case.
If first-use behavior violates any hard gate, this law returns to REWRITE status.
```

Required test cases for future reruns:

```text
SG-01: Missing report repeated.
SG-02: Report not in zip / wrong zip path.
SG-03: Zip/Git risk.
SG-04: Saved-view persistence regression.
SG-05: Row-menu opener/setter regression.
SG-06: Shift-selection random range bug.
SG-07: Broad runtime refactor too wide.
SG-08: Typecheck/build blocked.
SG-09: Manual UI validation missing.
SG-10: Same objective no improvement after second try.
```

For each SG case, law must output:

```text
Failure class:
Allowed next action:
Forbidden next action:
Prompt type:
Proof required:
PASS condition:
FAIL/WORSE condition:
Discard trigger:
```

Hard gates:

```text
100% correct WORSE routing to recovery-only.
100% correct repeated artifact failure routing to command-only.
100% ban on third same-style retry after two failures.
100% ban on PASS without required proof.
100% source unclear → discovery-only.
100% broad scope failure → one-surface split.
100% score-type separation.
100% cross-workspace user-confirmed defect escalation.
```

---

## 16. Banned Anti-Patterns

The following are illegal:

```text
Same prompt but stronger wording.
Normal correction after WORSE.
Feature continuation after regression.
PASS without zip review.
Done without lesson.
Report failure handled by another prose prompt after second miss.
Broad refactor after broad refactor failure.
Implementation before source-of-truth discovery.
Claiming build/typecheck passed when blocked.
Mixing cumulative and iteration scores.
Creating zip inside repo.
Uploading zip without zipinfo proof.
Treating model intelligence as first suspect before prompt/process classification.
Letting unknowns become facts.
Letting worker fix unrelated bugs silently.
Deferring user-confirmed cross-workspace interaction bugs without explicit severity decision.
```

---

## 17. Final Operating Checklist

Before releasing any prompt, answer:

```text
1. What is the active issue?
2. What is the iteration number?
3. What is the objective?
4. What is the task type?
5. What is the source of truth?
6. What works?
7. What fails?
8. What is unknown?
9. What is the failure class?
10. Is this first try, second try, or repeated failure?
11. Has this prompt family failed twice?
12. What files are allowed?
13. What areas are forbidden?
14. What proof is required?
15. What artifact must be returned?
16. What is PASS?
17. What is PARTIAL?
18. What is FAIL?
19. What is WORSE?
20. What is the stop condition?
21. What is the next-action rule if it fails?
22. What prompt type is forbidden?
23. What score will be cumulative?
24. What score will be iteration-only?
25. Is the law proven for this use?
```

If any answer is missing, do not generate the prompt.

---

## 18. Minimal Prompt Release Format — Consolidated v2.2

Prompt templates are internal checklists, not mandatory copyable boilerplate.

Default copyable prompt shape:

```text
Task:
Allowed:
Forbidden:
Required behavior/report:
Proof required:
PASS:
FAIL:
WORSE:
```

Forbidden in copyable worker prompts unless execution-critical:

```text
session/reset line
active issue title
run number
iteration number
worker model line
Linear metadata
history narrative
standard utility-script instructions
```

The prompt body must include only information that changes the worker's implementation or audit decision.

Metadata belongs in Linear/chat records, not in the worker prompt.

For high-risk work, richer prompts are allowed only when the extra text prevents a likely mistake.

## 19. Current Active Status — Consolidated v2.2

```text
Law version: SysGrid Prompt Generation Law v2.2 CONSOLIDATED
Status: ACTIVE CONSOLIDATED LAW
Supersedes active prompt-law file set: v2.0 + v2.1 + v2.2 amendment files
Keep with: SysGrid Linear SOP — Zero-Deviation Operating Law
```

This consolidated file is the only active Prompt Generation Law file needed once adopted.

Older prompt-law files may be archived from active project context after this file is installed.



---

# Integrated v2.2 Zero-Divergence + Token Economy Rules

## 1. Hard Lesson From OUT-8

The law failed to prevent a specific class of mess:

```text
Multiple views had similar-looking UI but divergent behavior.
Local symptom patches accumulated.
Source-level PASS was assigned before human behavior parity was proven.
Backend/action support was not verified before frontend revert behavior was trusted.
```

Therefore, visual similarity is not parity.

A shared UI shell is not enough.

A shared behavior contract is required.

---

## 2. Multi-View Zero-Divergence Gate

If two or more views must behave identically, no implementation prompt is allowed until a zero-divergence audit exists.

This applies to any behavior shared across views, including:

```text
bulk actions
row actions
saved views
display/views switching
selection behavior
floating panels
modals
toasts
undo/revert
validation
archive/restore/purge
```

Required before implementation:

```text
1. Shared user-facing contract.
2. Per-view current-state matrix.
3. Backend/API action support matrix.
4. Toast/message contract.
5. Revert/undo contract.
6. No-op/change/partial/failure contract.
7. PASS/FAIL/WORSE matrix.
8. Exact allowed implementation surface.
```

If this audit is missing, the next prompt must be **audit-only**, not implementation.

---

## 3. Zero-Divergence Failure Rule

For multi-view parity tasks:

```text
Any unexplained divergence = FAIL.
Any known divergence left unplanned = FAIL.
Any implemented divergence = 0/100 failure.
Any broken revert/action mismatch = WORSE if it affects an existing working path.
```

A view may differ only if the user explicitly approves the difference.

Approved differences must be documented as contract exceptions.

No silent exceptions.

---

## 4. Contract-First UI/Behavior Rule

For shared behavior, implementation prompts must be based on a contract, not on one view’s accidental current behavior.

Before coding, define:

```text
Operation:
Selection state:
No-op behavior:
All-change behavior:
Partial-change behavior:
Failure behavior:
Toast text pattern:
Changed count rule:
Changed field/column label rule:
Revert visibility rule:
Revert action name:
Revert payload:
Backend support:
Irreversible action rule:
```

If any field is unknown, prompt type must be discovery/audit.

---

## 5. Backend-Frontend Action Contract Gate

Frontend behavior cannot be trusted until backend/API support is verified.

Before adding or trusting a frontend action, verify:

```text
1. Route/handler exists.
2. Action name is supported.
3. Payload shape is accepted.
4. Failure behavior is known.
5. Revert action is supported if revert is shown.
```

Forbidden:

```text
Show revert button for unsupported action.
Invent frontend-only action names without backend support.
Assume restore_snapshots works because source contains a frontend branch.
Use frontend toast success as proof of backend success.
```

If support cannot be found, state **not found in source** and keep implementation blocked.

---

## 6. Human Validation Supremacy

Zip/source review can only prove source-level compliance.

For user-facing behavior, human UI validation can override source review.

If the user reports behavior failure after source PASS:

```text
1. Immediately downgrade the state.
2. Record human validation failure.
3. Stop implementation continuation.
4. Reclassify failure class.
5. Generate audit/recovery prompt only.
```

Never defend a source PASS against human-observed UI failure.

---

## 7. Prompt Token Economy Gate

Prompts must use the fewest tokens that preserve correctness.

Required rule:

```text
Only include information that changes the worker’s decision.
```

Forbidden in copyable worker prompts unless execution-critical:

```text
session boilerplate
active issue title
run number
iteration number
worker model line
historical narrative
repeated Linear metadata
motivation/prose
standard utility-script instructions
```

Keep metadata in Linear/chat records, not in the copyable prompt.

---

## 8. Utility Script Separation Rule

The user runs the commit/push/zip utility script.

Prompts must not waste tokens telling the worker to run git, push, zip, or the utility script unless the user explicitly asks for those lines.

Allowed:

```text
Required artifact: frontend/<file>.md
Uploaded zip is review source of truth.
```

Forbidden by default:

```text
Run git diff.
Commit changes.
Push branch.
Run commit-push-zip.
Use the standard commit-push-zip workflow.
Upload the zip.
```

Exception:

```text
A proof command may be requested only when it directly verifies scope or behavior.
Do not include packaging commands.
```

v2.1 is amended accordingly: keep the artifact-location rule, remove prompt instructions telling the worker to run the user’s utility workflow.

---

## 9. Compact Prompt Shape

Default prompt shape:

```text
Task:
Allowed:
Forbidden:
Required behavior/report:
Proof required:
PASS:
FAIL:
WORSE:
```

No top boilerplate.

No metadata lines unless they alter execution.

---

## 10. Rich Prompt Exception

Use richer prompts only when one of these is true:

```text
post-WORSE recovery
multi-view zero-divergence audit
backend/frontend contract mismatch
high-risk shared runtime change
ambiguous source of truth
known repeated failure family
```

Even then, richness must be source-anchored, not narrative-heavy.

Preferred rich content:

```text
exact files
exact bad patterns
exact contract matrix
exact grep checks
exact forbidden surfaces
```

Avoid:

```text
background story
full iteration history
model pep talk
repeated constraints already enforced by law
```

---

## 11. Prompt Family Stop Rule For Multi-View Failures

If two local patches fail to produce parity across views, local patch prompts are invalid.

Required next step:

```text
audit-only zero-divergence matrix
```

Forbidden:

```text
third local patch
view-by-view symptom fix
normal continuation
lock-readiness claim
```

---

## 12. Audit Report Artifact Rule

For audit/report-only tasks, create the smallest useful artifact inside `frontend/`.

Required:

```text
single minimal markdown file
clear matrix
source-backed claims
implementation plan only after divergence is known
```

Forbidden:

```text
large narrative report
files outside frontend/
source edits during audit
claims not backed by inspected source
```

Do not tell the worker to zip or run the utility script.

---

## 13. Review Scoring Amendment

For multi-view parity tasks:

```text
Source PASS does not equal behavioral PASS.
Behavioral PASS requires human validation or test evidence across every view in the contract.
```

Score caps:

```text
Audit complete, no implementation: max 90 for audit iteration.
Source implementation passes, no human UI validation yet: max 93.
Any reported multi-view divergence after PASS: downgrade immediately.
Unsupported revert/action error: max 70 until root cause is mapped.
Known divergence across views: max 60 until zero-divergence plan exists.
```

---

## 14. Row Action Title No-Wrap Width Law

For row action golden templates across Monitoring, External, and Services:

```text
Main row action title/header row must never wrap.
Selected entity title must remain one line.
If the window is too narrow for title + controls, width must expand.
If title exceeds viewport-safe max, keep one line with ellipsis, not wrap.
```

Before implementation, audit:

```text
1. Component/template used per view.
2. Current width sizing rule.
3. Header/title markup.
4. CSS wrapping/ellipsis rules.
5. Whether title can wrap.
6. Whether width can expand based on title.
7. Divergence across views.
```

Implementation must be shared or zero-divergence across all applicable views.

---

## 15. Required Self-Check Before Any Prompt

Before producing a prompt, ChatGPT must answer internally:

```text
1. Is this multi-view behavior?
2. If yes, does a zero-divergence audit already exist?
3. Am I adding metadata that the worker does not need?
4. Am I telling the worker to run the user’s utility script?
5. Am I repeating history instead of giving source anchors?
6. Is this prompt shorter than the previous safe version without losing correctness?
```

If answer 2 is no, generate audit-only.

If answer 3 or 4 is yes, remove those lines.


# End of SysGrid Prompt Generation Law v2.2 CONSOLIDATED
