# Investment Industry Graph Strategist Knowledge Pack

Version: 1.0  
Purpose: Custom GPT knowledge files for an investment-grade industry graph strategist.

## Design philosophy

These files are not the GPT's main instruction law. The GPT Builder instruction field should contain the short global law under 8,000 characters. These files are the GPT's reference brain: taxonomies, playbooks, scoring rubrics, templates, and tests.

Use this package when the GPT must turn an industry input into:

`industry → graph → money flow → evidence → bottlenecks → simulations → investment themes → recommendation → reusable snapshot`

## Upload files

Upload these Markdown files as GPT knowledge:

0. `00_Knowledge_Pack_Index_and_Routing.md`
1. `01_Industry_Graph_Taxonomy.md`
2. `02_Economic_Dependency_and_Money_Flow_Framework.md`
3. `03_Research_Evidence_Standard.md`
4. `04_Current_Signal_Extraction_Playbook.md`
5. `05_Bottleneck_Detection_Playbook.md`
6. `06_Simulation_Engine_Playbook.md`
7. `07_Investment_Theme_Scoring_Rubric.md`
8. `08_Report_Template_and_Snapshot_Format.md`
9. `09_Evaluation_Test_Suite.md`
10. `10_Self_Audit_and_Feedback_Loop_Protocol.md`
11. `11_Deep_Research_Execution_Protocol.md`
12. `12_Industry_Archetype_Checklists_and_Query_Bundles.md`
13. `13_Gold_Standard_Output_Patterns.md`

Do not upload `qa_check.py` or `quality_gate.py` as GPT knowledge. They are only for local quality checking.

Paste `GLOBAL_GPT_LAW_v1.0.txt` into the GPT Builder Instructions field. It is designed to stay under the 8,000-character instruction limit.

## How the final GPT instruction should reference these files

The final under-8,000-character GPT instruction should say:

> When producing a full industry report, consult the uploaded knowledge files if available. Start with the knowledge-pack index/routing file. Use the graph taxonomy to build nodes and edges, the money-flow framework to trace economics, the evidence standard, signal playbook, and deep research protocol to research current status, the bottleneck playbook to detect constraints, the simulation engine to model scenarios, the scoring rubric to rank investment themes, and the report template to structure the output and snapshot.

Add this when using File 10:

> Before finalizing a full report, run the self-audit protocol: check for missed nodes, unsupported claims, weak money-flow logic, shallow bottlenecks, weak simulations, and generic investment themes. Repair the answer before showing it when possible.

## Feedback loop

The improvement loop is:

1. Run the GPT on a test industry.
2. Score the result using `09_Evaluation_Test_Suite.md`.
3. Record failure modes:
   - missed critical node
   - wrong confident claim
   - weak money-flow logic
   - shallow bottleneck detection
   - poor second-order simulation
   - generic investment themes
   - weak citations
4. Update the specific knowledge file that failed.
5. Retest on the same industry and one new industry.

## Versioning rule

Increment the package version when:

- a new knowledge file is added;
- a rubric, template, or required output field changes;
- an evaluation test reveals a reusable failure mode;
- the global GPT instruction must change to invoke the files more reliably.

## Local autonomous quality loop

Run:

```bash
python3 qa_check.py
python3 quality_gate.py
python3 benchmark_gate.py
python3 instruction_gate.py
```

The release is upload-ready only when all gates pass. `quality_gate.py` checks architecture conditions. `benchmark_gate.py` checks diverse-industry readiness across technology infrastructure, pharma/healthcare, commodity/materials, regulated energy, and financial services. `instruction_gate.py` checks the global GPT instruction length and required anchors.
