# Compiler and Package Contract v7

## 1. Compiler objective

Produce the smallest complete, installable, truthful package that can meet the approved architecture. A package is not complete because its prose is polished; it is complete when every promised behavior maps to instructions, Knowledge, settings, tools, tests, and an honest fallback.

## 2. Package tiers

### Lite package

- Runtime Instructions.
- Zero to two Knowledge files if needed.
- Settings sheet.
- Three to six conversation starters.
- Five to fifteen representative tests.
- Install note and manifest.

### Foundation package

- Runtime Instructions.
- Modular Knowledge bundle.
- Settings and capability matrix.
- Conversation starters.
- Development benchmark and holdout protocol.
- Delivery manifest and install guide.
- Research Coverage Ledger for research-backed architecture.

### Integrated Agent package

Everything in Foundation plus:

- system architecture and data-flow design;
- source-access and permission matrix;
- Apps/Actions/API specification or explicit not-created status;
- authentication and consent design;
- data-store schema;
- action/confirmation policy;
- retries, idempotency, observability, incident, and recovery plan;
- sandbox/end-to-end/adversarial tests;
- deployment and operations guide only when a real external runtime exists.

## 3. Runtime compiler rules

Runtime Instructions contain only behavior needed across most turns:

- identity and optimization objective;
- priority/trust rules;
- route triggers;
- mode-specific core behavior;
- research trigger and truthfulness;
- capability/privacy/authority boundary;
- artifact and evaluation contract.

Move long templates, domain source maps, detailed checklists, examples, and test specifications to Knowledge.

### Runtime checks

- exact character count measured on the paste-ready text;
- below the current editor limit;
- target maintenance margin at least 1,000 characters when the inherited 8,000-character gate applies;
- each rule stated once where practical;
- trigger → action structure for routing;
- no contradictory approval instructions;
- no stale platform/model facts;
- no citation markers or file claims inside the runtime unless required and verified.

## 4. Knowledge compiler rules

- Use clear text-forward Markdown.
- One governing purpose per file.
- Put version, status, and section headings in every file.
- Avoid repeating the runtime verbatim.
- Store durable methods and schemas, not changing facts.
- Use stable names and cross-references.
- State precedence when files conflict.
- Include examples only when they correct a measured ambiguity or encode a product requirement.

## 5. Capability matrix

For every promised function record:

- function;
- required built-in capability;
- required Knowledge;
- required external app/action/API;
- authentication;
- side effects;
- confirmation policy;
- privacy class;
- failure behavior;
- manual fallback;
- test cases.

If no real capability exists, the package must narrow the promise or provide a manual fallback.

## 6. Custom GPT settings contract

Record:

- name;
- description;
- recommended model strategy;
- conversation starters;
- Web Search;
- Code Interpreter & Data Analysis;
- Canvas;
- Image Generation;
- Apps or Actions;
- sharing status;
- Knowledge file list;
- current platform verification date.

Model names and availability can change. Prefer a task-based model strategy and rerun smoke tests after automatic or manual model changes.

## 7. Integrated system specifications

When the architecture needs external execution, include or truthfully mark not created:

- OpenAPI or app contract;
- endpoint and tool descriptions;
- auth method and scopes;
- request/response schemas;
- error and retry semantics;
- idempotency key behavior;
- side-effect classification;
- user-confirmation points;
- data retention/deletion owner;
- audit and monitoring fields;
- sandbox test fixtures;
- policy and platform limitations.

Do not invent endpoints, credentials, connected accounts, approvals, or successful calls.

## 8. Delivery Manifest

Fields:

- asset;
- artifact class;
- intended use;
- status;
- created location;
- install step;
- local verification;
- Preview/external verification;
- not-created dependencies;
- version/hash.

## 9. Compile gate

Before delivery verify:

1. Named architecture and scope approved.
2. Blocking decisions resolved or explicitly excluded.
3. Package tier selected.
4. Runtime count and maintenance margin pass.
5. Competency and completeness checks pass.
6. Research coverage is truthful.
7. Capability/Knowledge/fallback alignment passes.
8. Privacy and external-action boundaries are explicit.
9. Apps/Actions/account claims match actual implementation.
10. Evidence-render rules pass.
11. Baseline and relevant development tests are defined.
12. Every listed file exists and is linked correctly.
13. Not-created and untested items are disclosed.

A local package with no Custom GPT Preview outputs is a **release candidate**, not a promoted release.

## 10. Failure handling

Any failed gate blocks the corresponding completion claim. Repair the earliest failed checkpoint, invalidate dependent claims, rebuild only affected assets, rerun structural checks, then rerun affected and baseline Preview tests.
