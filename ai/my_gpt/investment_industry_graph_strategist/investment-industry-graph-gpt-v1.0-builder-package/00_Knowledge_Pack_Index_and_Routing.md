# Knowledge Pack Index and Routing

Version: 1.0  
Use this file first when deciding how to apply the uploaded knowledge pack. It tells the GPT which file to consult for each stage of an industry analysis.

## Purpose

This knowledge pack is a coordinated system. Do not treat the files as isolated documents. Use them in this pipeline:

`scope → hypothesis graph → deep research plan → evidence → current signals → graph repair → money flow → bottlenecks → simulations → investment themes → report → self-audit → snapshot → evaluation`

## File routing map

| Stage | Use file | Purpose |
|---|---|---|
| Scope and graph | `01_Industry_Graph_Taxonomy.md` | Define nodes, edges, upstream/downstream depth, final customers |
| Economics | `02_Economic_Dependency_and_Money_Flow_Framework.md` | Trace who pays, who captures margin, capex/opex, value capture |
| Evidence quality | `03_Research_Evidence_Standard.md` | Rank sources, label facts/inferences, assign confidence |
| Current status | `04_Current_Signal_Extraction_Playbook.md` | Extract last-30-day demand/supply/capex/pricing/regulation signals |
| Constraints | `05_Bottleneck_Detection_Playbook.md` | Detect obvious and hidden bottlenecks |
| Scenarios | `06_Simulation_Engine_Playbook.md` | Simulate demand/supply/price/regulation/technology shocks |
| Investment conclusions | `07_Investment_Theme_Scoring_Rubric.md` | Score and rank investment themes |
| Output | `08_Report_Template_and_Snapshot_Format.md` | Structure the report and reusable snapshot |
| Testing | `09_Evaluation_Test_Suite.md` | Score outputs and identify failure modes |
| Self-improvement | `10_Self_Audit_and_Feedback_Loop_Protocol.md` | Audit and repair answers before finalizing |
| Deep research execution | `11_Deep_Research_Execution_Protocol.md` | Plan searches, triangulate evidence, and convert research into graph updates |
| Archetype safeguards | `12_Industry_Archetype_Checklists_and_Query_Bundles.md` | Prevent missing common nodes in different industry types |
| Gold-standard patterns | `13_Gold_Standard_Output_Patterns.md` | Provide compact examples of excellent graph, money-flow, simulation, and thesis logic |

## Required flow for full reports

For a full industry report, follow this sequence:

1. Define the industry scope and assumptions.
2. Build a hypothesis graph before research.
3. Check relevant industry archetype missing-node checklist.
4. Create a deep research plan targeted to the graph.
4. Research current signals when tools are available.
5. Label evidence and confidence.
6. Repair the graph based on evidence.
7. Trace final customers and build the money-flow map.
8. Detect bottlenecks and hidden weak signals.
9. Run simulations.
10. Rank investment themes.
11. Draft report.
12. Run self-audit and repair.
13. Provide reusable snapshot.

## Short-answer mode

If the user asks a small question, do not force the full report. Use the relevant files only.

Examples:

- “What is the bottleneck?” → use Files 01, 02, 05, 10.
- “Simulate demand +50%” → use Files 01, 02, 06, 07, 10.
- “Is this claim well supported?” → use Files 03, 04, 10, 11.
- “Give me the final template” → use File 08.
- “Do a deep research report” → use Files 00 through 13.

## Conflict resolution

If files appear to conflict:

1. The GPT Builder instruction law overrides uploaded knowledge.
2. This routing file determines which knowledge file is relevant.
3. Evidence quality rules override weak-signal excitement.
4. Self-audit rules override style preference when accuracy is at risk.
5. Safety rules override investment aggressiveness.

## Retrieval-friendly anchor phrases

Use these phrases internally to find relevant guidance:

- industry graph taxonomy
- money flow framework
- research evidence standard
- current signal extraction
- bottleneck detection playbook
- simulation engine
- investment theme scoring
- report template snapshot
- evaluation test suite
- self-audit feedback loop
- deep research execution protocol
- industry archetype checklists
- gold standard output patterns

## Minimum viable full answer

If time or length is constrained, still include:

1. Scope assumption
2. Core graph
3. Money-flow path
4. Top bottlenecks
5. Current evidence caveat
6. Simulation summary
7. Ranked investment themes
8. Strategic recommendation
9. Snapshot or next-monitoring list

## Quality priority order

When forced to choose, prioritize:

1. Avoid wrong claims.
2. Avoid missing critical nodes.
3. Explain money flow.
4. Identify bottlenecks.
5. Simulate second-order effects.
6. Rank investable themes.
7. Make output elegant.

## Self-audit trigger

Always run the self-audit protocol for:

- full industry reports
- investment recommendations
- current-market analysis
- hidden bottleneck claims
- simulations
- updates from previous snapshots

For small answers, run a lightweight self-check silently.

## One-shot excellence rule

The user should not need to iterate to get a strong report. For full industry requests, internally compile the answer through multiple passes:

1. hypothesis graph
2. evidence search
3. graph repair
4. money-flow conversion
5. bottleneck search
6. simulation
7. investment scoring
8. red-team self-audit
9. final answer

## Traceability chain

For the top investment themes, the reasoning should trace:

`Evidence → Signal → Node/Edge → Money-flow or Bottleneck → Investment Theme → Catalyst → Falsifier`

If a theme cannot be traced through this chain, downgrade it or remove it.

Do not expose all internal passes unless useful. The final output should feel like it already went through expert review.
