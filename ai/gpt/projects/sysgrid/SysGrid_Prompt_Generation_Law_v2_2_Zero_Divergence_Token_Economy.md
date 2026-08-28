# SysGrid Prompt Generation Law v2.2 — Zero-Divergence + Token Economy Amendment

Status: **ACTIVE AMENDMENT**
Base law: **SysGrid Prompt Generation Law v2.0**
Previous amendment: **v2.1 Workflow Amendment**
Purpose: Fix prompt-law gaps exposed during OUT-8 multi-view bulk divergence and remove prompt-token waste.

---

## 0. Authority

This amendment overrides v2.0/v2.1 wherever it is stricter.

Priority order:

```text
1. SysGrid Linear SOP — Zero-Deviation Operating Law
2. Prompt Generation Law v2.2
3. Prompt Generation Law v2.1
4. Prompt Generation Law v2.0
```

If any rule conflicts, the higher-priority rule wins.

---

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

---

## 16. Active Law Status

```text
v2.0 remains active for core gates and failure taxonomy.
v2.1 remains active for zip-as-source-of-truth and frontend artifact placement.
v2.2 overrides v2.1 by forbidding prompt instructions to run git/zip/utility workflow.
v2.2 adds zero-divergence contract gates and token economy gates.
```

# End of SysGrid Prompt Generation Law v2.2
