# Self-Audit and Feedback Loop Protocol

Version: 1.0  
Use this file before finalizing full industry reports and when improving the GPT knowledge pack after evaluation.

## Objective

The GPT must improve answer quality without requiring the user to act as the quality-control system. Before finalizing a full report, it should internally audit the report, repair weaknesses, and disclose only the remaining material uncertainty.

This file creates a feedback loop:

`draft → self-audit → repair → confidence adjustment → final answer → reusable snapshot → evaluation → knowledge/instruction update`

## Pre-final self-audit

Before showing a full report, check the draft against these failure modes.

### 1. Missing critical nodes

Ask:

- What node would an expert be angry I missed?
- Did I include energy, regulation, infrastructure, capital, labor, data, trust, and distribution when material?
- Did downstream paths end at real final customers?
- Did upstream expansion stop for a materiality reason?

Repair:

- Add missing nodes.
- Mark uncertain nodes as watchlist if evidence is weaker.
- Explain why excluded nodes were not material.

### 2. Wrong or unsupported claims

Ask:

- Did I state any current fact without evidence?
- Did I invent market share, ranking, recent event, customer relationship, or price?
- Are citations connected to the claims they support?

Repair:

- Remove unsupported specifics.
- Downgrade to inference or weak signal.
- State verification needed.

### 3. Weak money-flow logic

Ask:

- Who pays?
- Who captures revenue?
- Where does margin concentrate?
- Who spends capex?
- Who bears opex?
- Who has pricing power?
- Who is squeezed?

Repair:

- Add money-flow path.
- Add budget owner.
- Separate technical importance from value capture.

### 4. Shallow bottleneck detection

Ask:

- Did I identify only obvious bottlenecks?
- Did I search for hidden/underpriced constraints?
- Did I rank bottlenecks?
- Did I explain who benefits if each bottleneck worsens or is solved?

Repair:

- Add hidden bottleneck watchlist.
- Add winner/loser logic.
- Add timing and confidence.

### 5. Weak simulation

Ask:

- Did the simulation start from final-customer demand or a defined shock?
- Did it show first-order and second-order effects?
- Did it identify new bottlenecks, winners, losers, margin, and capex impact?
- Did it distinguish consumer, enterprise, government, and industry-specific demand?

Repair:

- Add causal chain.
- Add second-order pressure movement.
- Add assumptions and falsifiers.

### 6. Generic investment themes

Ask:

- Is the theme more specific than “industry is growing”?
- Is it tied to money flow, bottleneck, catalyst, and evidence?
- Is the ranking justified?
- Is there a falsifier?

Repair:

- Sharpen theme around a node, edge, bottleneck, or money-flow path.
- Add catalyst, risk, time horizon, and beneficiary exposure.

### 7. Broken evidence-to-thesis trace

Ask:

- Can the top themes be traced from evidence to signal to node/edge to money-flow or bottleneck to theme to catalyst to falsifier?
- Is any theme based mainly on excitement, market size, or vague growth?

Repair:

- Add traceability chain.
- Downgrade or remove unsupported themes.
- Replace generic themes with node/edge-specific themes.

## Confidence adjustment rules

Downgrade confidence when:

- Evidence is weak or old.
- Sources conflict.
- The thesis depends on multiple uncertain assumptions.
- The causal chain is long.
- The theme depends on regulation, commodity cycles, or customer adoption timing.

Upgrade confidence only when:

- Primary sources and recent data agree.
- The causal chain is direct.
- Money-flow logic is clear.
- Bottleneck evidence is strong.
- Falsifiers are observable.

## Visible self-audit summary

Usually do the audit silently and present the improved answer.

Show a short self-audit summary when:

- Evidence is insufficient for a key claim.
- The user asks for maximum rigor.
- A full investment report is produced.
- The report contains speculative or hidden weak-signal theses.

Short format:

| Audit area | Status | Remaining weakness |
|---|---|---|
| Graph completeness | Pass / Watch / Fail | ... |
| Evidence quality | Pass / Watch / Fail | ... |
| Money-flow logic | Pass / Watch / Fail | ... |
| Bottleneck depth | Pass / Watch / Fail | ... |
| Simulation depth | Pass / Watch / Fail | ... |
| Theme specificity | Pass / Watch / Fail | ... |
| Evidence-to-thesis traceability | Pass / Watch / Fail | ... |

## Knowledge-pack improvement loop

When evaluating the GPT or improving these files:

1. Run a hard test industry.
2. Score using the evaluation suite.
3. Identify the failure type:
   - Instruction failure: the GPT ignored a requirement.
   - Knowledge failure: the framework lacked needed guidance.
   - Evidence failure: the GPT lacked current/credible data.
   - Reasoning failure: the GPT failed to connect evidence to graph/money flow.
   - Format failure: the output was hard to use.
4. Patch the smallest responsible file.
5. Increment version.
6. Retest same industry.
7. Test a different industry to avoid overfitting.
8. Record changes in changelog.

## Anti-overfitting rule

Do not add industry-specific facts to general framework files unless they are clearly examples. The knowledge pack should improve reasoning across industries, not memorize one industry.

## Done criteria

A report is ready when:

- Critical graph nodes are present.
- Money flow is explicit.
- Evidence is labeled.
- Hidden bottlenecks are considered.
- Simulations include second-order effects.
- Investment themes are ranked and falsifiable.
- Remaining uncertainty is visible.
