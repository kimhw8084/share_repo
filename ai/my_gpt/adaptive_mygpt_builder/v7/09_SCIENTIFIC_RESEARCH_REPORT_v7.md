# Scientific Research Report for Adaptive MyGPT Builder v7

**Research date:** 2026-07-27  
**Decision supported:** redesign of Adaptive MyGPT Builder v6 into a higher-performance, lower-regression v7 release candidate  
**Coverage label:** `ADEQUATE ARCHITECTURE SCAN`  
**Validation status:** research-informed architecture; comparative Custom GPT Preview validation not yet executed

## 1. Research question

What design, prompting, retrieval, agent-security, and evaluation changes are most likely to improve the real performance of MyGPT creation while preserving the valuable v6 baseline and minimizing accidental regressions?

## 2. Scope

The review used:

- the uploaded v6 runtime, Constitution, workshop, role/domain pack, Research Diligence OS, evidence lanes, compiler, evaluation standard, immutable baseline, stress evidence, and benchmark registry;
- current official OpenAI documentation for Custom GPT configuration, Knowledge, capabilities, Apps, Actions, memory, model selection, prompt design, and Preview;
- current OpenAI research and evaluation guidance;
- peer-reviewed or primary research on long prompts and contexts, RAG evaluation, LLM judges, benchmark contamination, clarification, abstention, tool-agent reliability, and prompt injection.

The source-by-source map is in `09B_RESEARCH_SOURCE_REGISTRY_v7.csv`.

## 3. Source-derived findings

### 3.1 Leaner prompts are a testable performance hypothesis, not an aesthetic preference

Current OpenAI model guidance recommends removing repeated instructions, stating each rule once, exposing only relevant tools, and comparing changes on representative tasks. It reports directional internal results where leaner system prompts improved coding-agent evaluation scores and reduced token use, while explicitly warning that workloads differ. SCULPT similarly treats long-prompt improvement as structured, targeted refinement rather than wholesale rewriting. Long-context research shows that models can use information unevenly depending on position, supporting prominent placement of core routing and authority rules.

**v7 implication:** reduce the runtime from the v6 near-limit text to a 6,666-character kernel; move detailed schemas and domain methods to six clear Knowledge modules; require same-prompt regression testing rather than assuming shorter is better.

### 3.2 Better models can infer more, so over-specification can become a regression

Current model guidance says modern models better infer intent and often need less prescription of intermediate steps, while still needing domain context, hard constraints, approval boundaries, and success criteria. OpenAI's GPT-building guidance recommends explicit trigger/action workflow structure, positive concrete instructions, and brief examples only where classification is ambiguous.

**v7 implication:** keep hard constraints and route triggers, but remove repeated procedure. Replace “Foundation Build for every new GPT” with Direct, Lite, Foundation, and Integrated Agent routes. Treat unnecessary workshops and questions as measurable performance defects.

### 3.3 Knowledge retrieval must be evaluated separately from answer quality

OpenAI distinguishes Instructions (behavior) from Knowledge (reference). RAG research repeatedly shows that retrieval does not eliminate unsupported or contradictory generation. RAGAs, ARES, RAGTruth, RAGChecker-related work, and later faithfulness studies support separating retrieval relevance/coverage from generation faithfulness and answer relevance.

**v7 implication:** evaluate whether the correct Knowledge module was retrieved, whether claims are supported, whether conflicts were surfaced, and whether the model falsely implied full-file review. Keep citations distinct from research-coverage proof.

### 3.4 One LLM judge is insufficient for promotion

Large studies find position bias, repeat inconsistency, and sensitivity to presentation cues in LLM-as-judge evaluation. Multi-agent judging can also amplify some biases. OpenAI evaluation guidance emphasizes contextual evals, golden sets, real outputs, error analysis, and validity checks.

**v7 implication:** deterministic checks first; blinded and order-randomized pairwise grading second; reverse order; human review for critical/disputed/sample cases; repeat critical nondeterministic cases; report disagreement instead of hiding it.

### 3.5 Realistic and fresh cases reduce false confidence

LiveBench and contamination studies show why public or repeatedly tuned benchmarks can become unreliable. OpenAI deployment simulation shows that realistic conversation contexts can reveal failure distributions and novel behaviors missed by narrow challenge sets. OpenAI's 2026 evaluation guidance also stresses reporting the tested system, tools, harness, budget, elicitation, and validity checks.

**v7 implication:** replace prompt summaries with full executable cases; keep a development suite, provisional holdout outside Knowledge, and anonymized real-prompt suite; preserve model/settings/tools/raw outputs; audit the benchmark itself for broken or ambiguous tasks.

### 3.6 Tool access does not imply agent reliability

WebArena, GAIA, ToolEmu, and related benchmarks show that realistic end-to-end tool tasks can remain difficult even when component capabilities exist. Failures can cause privacy, financial, or operational harm. A Custom GPT also does not inherently provide persistent storage or a continuous external runtime.

**v7 implication:** add Integrated Agent Build. Separate conversational reasoning from external execution, state, authentication, permissions, retries, idempotency, logs, monitoring, and recovery. Require end-to-end sandbox tests and honest unsupported-source/manual-handoff states.

### 3.7 Prompt injection requires architecture and tests, not only a warning sentence

Instruction-hierarchy research and current OpenAI security guidance emphasize trust levels and the growing social-engineering character of prompt injection. Agent Security Bench and WASP find vulnerabilities across prompts, tools, memory, and realistic web trajectories. Task Shield provides evidence for checking whether each action serves the user's authorized objective.

**v7 implication:** preserve evidence-as-data quarantine, add a six-part task-alignment gate before consequential tool calls, use least privilege and confirmations, and test indirect injections inside files, webpages, tool results, and multi-agent handoffs.

### 3.8 Clarification and abstention should be selective

Research on clarification shows that asking is valuable when ambiguity changes the likely intent or outcome, but excessive clarification harms speed. Abstention research supports refusing or withholding an answer when evidence is insufficient, with the threshold depending on task risk and values.

**v7 implication:** ask only decision-changing questions; track unnecessary and missed clarification rates; use `NOT ENOUGH COVERAGE TO RECOMMEND` when a material evidence gap could reverse a consequential recommendation.

## 4. v6 diagnosis grounded in uploaded material

### Strengths preserved

- explicit research-coverage proof rather than citation theater;
- direct-task bypass;
- owner discovery and blocking decisions;
- approval and artifact-status discipline;
- privacy and external-action boundaries;
- prompt-injection quarantine;
- immutable baseline and critical-failure gate;
- 95+ as a benchmark target rather than a self-awarded label.

### Main performance risks addressed

1. **Instruction saturation:** the v6 runtime was effectively at its 8,000-character gate, leaving negligible maintenance margin.
2. **Over-routing:** every new GPT could enter Foundation Build even when a Lite Build was sufficient.
3. **Role theater:** mandatory 3–8 roles could add complexity without distinct ownership.
4. **Research-output overhead:** full ledgers risked dominating ordinary answers.
5. **Non-executable benchmark:** v6 B01–B18 used placeholder scenario summaries rather than full prompts.
6. **Missing Integrated Agent route:** persistent, authenticated, external-action systems were treated mainly as boundaries rather than a complete architecture class.
7. **Judge validity gaps:** no explicit order randomization, repeated grading, benchmark-defect audit, or deployment-like prompt distribution.

## 5. Architecture selected

### Runtime kernel

A 6,666-character paste-ready runtime containing only:

- identity and objective;
- trust/priority;
- route triggers;
- core mode behavior;
- research and evidence trigger;
- capability/privacy/scope boundary;
- artifact contract;
- evaluation and non-regression gate.

### Six Knowledge modules

1. Governance and immutable baseline.
2. Build router and owner discovery.
3. Research and Evidence OS.
4. Domain and Integrated Agent patterns.
5. Compiler and package contract.
6. Evaluation and non-regression system.

### Evaluation assets

- full-prompt development registry;
- provisional holdout kept outside Knowledge;
- evaluation workbook;
- structural validator and hashes;
- owner real-prompt requirement before promotion.

## 6. Job-agent capability test

v7 is designed to classify an automated job-search/application request as an Integrated Agent Build. It should create:

- candidate calibration and verified profile schema;
- role-family research and primary/adjacent/bridge/training-first portfolio;
- separate career-value and speed-to-offer scoring;
- authorized source-access matrix;
- structured job-description evaluation;
- apply/approval/hold/do-not-apply policy;
- persistent database or tracking-sheet schema;
- Apps/Actions/API and authentication design;
- platform-policy verification;
- retries, idempotency, logging, monitoring, and failure recovery;
- truthful manual fallback for restricted platforms;
- end-to-end and adversarial tests.

It must not pretend that a standalone Custom GPT can continuously access every platform, preserve state, or submit everywhere without an implemented external system and permission.

## 7. Research Coverage Ledger

**Decision supported:** v7 architecture and release-candidate package.

**Required source classes:** full v6 package; current official Custom GPT documentation; current model/prompt guidance; evaluation methodology; long-context/prompt research; RAG evaluation; agent reliability/security; clarification/abstention; raw v6 and v7 Preview outputs; owner real prompts.

**Checked:** all listed classes except raw comparative Preview outputs and owner real-use evidence.

**Directly used:** 30 official, peer-reviewed, or primary sources listed in the source registry.

**Checked but not relied on:** general news and secondary commentary were excluded where official or primary sources were available.

**Missing/blocked:** current editor state in the owner's account, actual model options, v6/v7 raw Preview outputs, real prompt distribution, external integration implementation, independent reviewer results.

**Disconfirmers:** newer models may handle long prompts better than earlier systems; reducing prompt length alone does not prove improvement. Some agent benchmarks use older models or simulated environments. LLM-judge mitigation does not eliminate all bias. These limits are why v7 is a release candidate and requires same-prompt Preview validation.

**Freshness limit:** platform/model facts can change after 2026-07-27.

**Stop rule:** high-ROI architecture source classes were checked; further browsing cannot substitute for missing product-specific execution data.

**Coverage label:** `ADEQUATE ARCHITECTURE SCAN`.

**Confidence impact:** high confidence in the need for modularization, executable evaluation, selective routing, and an Integrated Agent route; insufficient evidence to quantify the performance gain or award 95+.

**Allowed claim:** the package is research-informed and locally structurally verified. It is not yet proven superior to v6 or validated in Custom GPT Preview.

## 8. References

See `09B_RESEARCH_SOURCE_REGISTRY_v7.csv` for titles, dates, findings, limitations, and URLs.
