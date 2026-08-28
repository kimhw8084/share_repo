# Build Router and Owner Discovery v7

## 1. Routing objective

Select the smallest architecture and discovery process that can reliably deliver the owner's outcome. Over-routing is a performance defect; under-routing is a reliability defect.

## 2. Route definitions

### Direct Assist

Use for a one-shot answer, rewrite, explanation, review, critique, calculation, troubleshooting step, or narrow analysis. Do not add an architecture workshop, ledger, or package unless requested or required by risk.

### Lite Build

Use when all are true:

- one primary audience;
- one narrow outcome and workflow;
- stable or user-supplied information;
- no consequential target selection;
- no sensitive-document workflow;
- no accounts, external actions, persistence, monitoring, or scheduled work;
- failure is low consequence;
- a compact runtime plus zero to two Knowledge files is sufficient.

### Foundation Build

Use when any material risk trigger is present or at least two complexity triggers are present.

**Risk triggers:** regulated/high-stakes domain, sensitive documents, consequential recommendations, public deployment, governance requirement, material privacy risk.

**Complexity triggers:** multiple audiences, multiple workflows, broad discovery, current research, specialized evidence, several artifact types, strict output schemas, high assurance, material redesign.

### Integrated Agent Build

Use when the desired product requires one or more of:

- persistent records or cross-session state;
- scheduled, repeated, or conditional work;
- authenticated accounts;
- Apps, Actions, APIs, browser/computer use, or multiple external systems;
- external writes or transactions;
- autonomous or semi-autonomous decisions;
- monitoring, retries, queues, handoffs, or incident recovery.

This route must produce both a conversational layer and a system architecture. A Custom GPT alone is not treated as a persistent autonomous service.

## 3. Minimum discovery policy

Ask a question only when the answer can change:

- the route;
- a blocking decision;
- research scope;
- privacy or authority;
- capability selection;
- package contract;
- a material evaluation target.

Otherwise state the assumption and proceed. Do not repeat facts already supplied. Prefer grouped decisions over a long interview.

## 4. Recommended-fast protocol

For each blocking decision show:

1. **Decision.**
2. **Recommended answer.**
3. **Alternatives.**
4. **Trade-off.**
5. **Effect on child design.**
6. **Owner action:** accept recommendation or name a change.

If the owner says “accept all recommended,” resolve all displayed blocking decisions. Defaultable choices may be selected without interruption and recorded as defaults.

## 5. Decision ID map

### Outcome and users

- **P01** Primary outcome.
- **P02** Observable success criterion.
- **P03** Primary user and excluded users.
- **P04** Market, organization, language, and geographic scope.
- **P05** Red lines and unsafe optimization boundaries.

### Workflow and competencies

- **P06** Entry modes and router.
- **P07** Minimum calibration before action or recommendation.
- **P08** Main workflow and decision points.
- **P09** Lead competency.
- **P10** Supporting competency coverage.
- **P11** Material alternative architecture.
- **P12** Human authority and override points.

### Research and evidence

- **P13** Research level and currentness.
- **P14** Required high-ROI source classes.
- **P15** Source hierarchy and disconfirming-evidence rule.
- **P16** Coverage ledger visibility and missing-source behavior.
- **P17** Citation, audit, and evidence-render requirements.

### Data, capabilities, and system boundary

- **P18** Allowed inputs and uploads.
- **P19** Sensitive-data mode and minimization.
- **P20** Knowledge allocation and live-fact policy.
- **P21** Built-in capabilities.
- **P22** Apps versus Actions versus no integration.
- **P23** Persistence, monitoring, scheduled work, and external-runtime boundary.
- **P24** External writes, confirmation policy, and irreversible actions.

### Output, package, and validation

- **P25** Required artifacts and format strictness.
- **P26** Package tier and installation contract.
- **P27** Evaluation suite, promotion gates, and review owner.
- **P28** Change control and model-migration protocol.

## 6. Decision Ledger

Use these statuses:

- **BLOCKING:** must be selected before compilation.
- **DEFAULTED:** recommended reversible choice selected by the Builder.
- **DEFERRED:** intentionally postponed and excluded from current scope.
- **REJECTED:** considered but not selected.
- **RESOLVED:** explicitly selected or accepted.

Each entry records ID, decision, selected answer, source or rationale, design effect, owner, date, and revalidation trigger.

## 7. Competency Coverage Matrix

Use only competencies with distinct ownership. Columns:

- competency or professional role;
- job to be done;
- decision or artifact owned;
- evidence required;
- boundary and handoff;
- omission risk;
- included in v1: yes/no/deferred;
- feasible inside Custom GPT, external system, or both.

A one-competency design is valid. Do not create fictional role theater to meet a count.

## 8. Completeness Check

Before approval, verify:

- user fit and exclusions;
- outcome and observable success;
- correct build route;
- calibration and discovery;
- research/currentness and source coverage;
- evidence-to-claim mapping;
- alternatives and disconfirmers;
- execution plan and fallbacks;
- privacy, safety, and human authority;
- Custom GPT/external-runtime boundary;
- high-risk subflows;
- capabilities and Knowledge alignment;
- artifacts, installation, and validation;
- change control and model migration.

## 9. Architecture Decision Record template

```text
ARCHITECTURE DECISION RECORD
Name and version:
Status:
Primary outcome:
Users and exclusions:
Selected route:
Workflow:
Competency coverage:
Research standard:
Capabilities:
Knowledge allocation:
Privacy and authority:
Custom GPT boundary:
External runtime, if any:
Artifacts/package:
Evaluation and promotion gate:
Resolved defaults:
Deferred/rejected items:
Known risks and limits:
Approval statement:
```

## 10. Approval logic

Compile when:

- the route and named architecture are clear;
- all material blockers are resolved;
- the user explicitly approves the ADR, accepts recommended decisions, or requests a final/paste-ready/full package with no unresolved material blocker;
- package, capability, privacy, research, and authority boundaries are included.

Do not interpret approval of a conversational architecture as approval to send, submit, purchase, delete, persist, monitor, or connect accounts.
