# Evaluation Test Suite

Version: 1.0  
Use this file to test whether the GPT is actually producing world-class industry investment intelligence.

## Objective

The GPT must be tested against hard industries. The goal is not pretty writing. The goal is to catch:

- Missing important nodes
- Wrong confident claims
- Weak money-flow logic
- Shallow bottleneck detection
- Poor second-order simulation
- Generic investment recommendations
- Weak evidence/citations

## Minimum quality target

Score each report out of 100.

- 90+: strong enough for v1.0
- 80–89: useful but needs refinement
- 70–79: not reliable enough
- below 70: redesign instruction/files

## Test industries

Use these first:

1. AI
2. Semiconductor equipment
3. Data center power infrastructure
4. GLP-1 obesity drugs
5. EV batteries
6. Copper mining
7. Nuclear power
8. Cybersecurity
9. Robotics/automation
10. Private credit

For minimum v1.0 readiness, test at least five completely different fields:

1. AI infrastructure: technology infrastructure
2. GLP-1 drugs: pharma healthcare
3. Copper mining: commodity materials
4. Nuclear power: regulated energy
5. Private credit: financial services

## Scoring rubric

| Category | Points | What good looks like |
|---|---:|---|
| Scope clarity | 8 | Clear assumption, geography, horizon, exclusions |
| Graph completeness | 14 | Captures critical upstream/downstream nodes |
| Final customer tracing | 8 | Every downstream path reaches real customer |
| Edge quality | 8 | Edges typed, directional, reasoned, confidence-labeled |
| Money-flow logic | 14 | Separates product flow from revenue/margin/capex/opex |
| Evidence quality | 12 | Uses strong sources, cites current signals, labels uncertainty |
| Bottleneck detection | 10 | Finds obvious and hidden constraints |
| Simulation quality | 10 | Includes first/second-order effects and winners/losers |
| Investment theme ranking | 10 | Ranked, thesis-driven, catalyst/risk/falsifier included |
| Non-expert clarity | 6 | Clear, teach-from-zero explanation without dumbing down |
| Self-audit repair | 10 | Catches and repairs missing nodes, unsupported claims, generic themes before final |
| Evidence-to-thesis traceability | 10 | Top themes trace evidence → signal → node/edge → money-flow/bottleneck → theme → catalyst → falsifier |

Total: 120. Normalize to 100 by multiplying by 100/120 if needed.

## Failure mode log

After each test, record:

```text
TEST RESULT
Industry:
Date:
Score:
Top 3 strengths:
Top 5 failures:
Missed nodes:
Wrong or unsupported claims:
Weak money-flow areas:
Weak simulation areas:
Instruction change needed:
Knowledge file change needed:
Retest prompt:
END TEST RESULT
```

## Autonomous improvement protocol

After each failed or weak test:

1. Classify each failure as instruction failure, knowledge-file failure, evidence limitation, or model reasoning failure.
2. Patch the smallest responsible file.
3. Update version and changelog.
4. Retest the same prompt.
5. Test a different industry to avoid overfitting.
6. Keep the change only if it improves the original test without weakening the new test.

## Red-team prompts

Use these prompts to stress test:

### AI

`Map the AI industry as an investment graph and identify the most underpriced bottlenecks.`

Expected strong answer includes:

- GPUs/accelerators
- HBM
- advanced packaging
- data centers
- power
- cooling
- networking/optics
- cloud platforms
- model layer
- enterprise applications
- final customers
- inference economics
- regulation/trust/security
- money flow from enterprise/consumer/government demand

### Data center power infrastructure

`Analyze data center power infrastructure as an investment graph. Where will money flow if AI demand keeps rising?`

Expected strong answer includes:

- utilities
- grid interconnection
- transformers
- switchgear
- substations
- backup generation
- cooling
- copper/electrical steel
- power-ready land
- data center developers
- hyperscalers
- regulators

### GLP-1 obesity drugs

`Build an investment-grade map of GLP-1 obesity drugs, including downstream customers and second-order effects.`

Expected strong answer includes:

- API manufacturing
- fill-finish capacity
- pens/injectors
- payers/employers/governments
- obesity/diabetes patients
- providers
- pharmacies
- competitors
- oral formulations
- side-effect/adherence issues
- food/medical-device second-order effects

## Feedback loop rule

When a report scores below 90:

1. Identify whether the failure belongs to instructions or knowledge.
2. If behavior failure, edit the global GPT law.
3. If framework failure, edit the relevant knowledge file.
4. Retest same prompt.
5. Test one unrelated industry to ensure the fix generalizes.
