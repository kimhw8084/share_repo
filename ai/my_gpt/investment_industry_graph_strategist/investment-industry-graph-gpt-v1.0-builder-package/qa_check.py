from pathlib import Path

ROOT = Path(__file__).resolve().parent
required = [
    "00_Knowledge_Pack_Index_and_Routing.md",
    "01_Industry_Graph_Taxonomy.md",
    "02_Economic_Dependency_and_Money_Flow_Framework.md",
    "03_Research_Evidence_Standard.md",
    "04_Current_Signal_Extraction_Playbook.md",
    "05_Bottleneck_Detection_Playbook.md",
    "06_Simulation_Engine_Playbook.md",
    "07_Investment_Theme_Scoring_Rubric.md",
    "08_Report_Template_and_Snapshot_Format.md",
    "09_Evaluation_Test_Suite.md",
    "10_Self_Audit_and_Feedback_Loop_Protocol.md",
    "11_Deep_Research_Execution_Protocol.md",
    "12_Industry_Archetype_Checklists_and_Query_Bundles.md",
    "13_Gold_Standard_Output_Patterns.md",
]

keywords = {
    "graph": ["node", "edge", "upstream", "downstream"],
    "money": ["revenue", "margin", "capex", "opex"],
    "evidence": ["evidence", "confidence", "source"],
    "bottleneck": ["bottleneck"],
    "simulation": ["scenario", "first-order", "second-order"],
    "investment": ["theme", "risk", "catalyst"],
    "self_audit": ["self-audit", "repair", "falsifier"],
    "deep_research": ["deep research", "triangulation", "graph repair"],
}

def main():
    failures = []
    for name in required:
        p = ROOT / name
        if not p.exists():
            failures.append(f"Missing file: {name}")
            continue
        text = p.read_text(encoding="utf-8")
        if not text.startswith("# "):
            failures.append(f"{name}: missing H1 title")
        if "Version:" not in text:
            failures.append(f"{name}: missing version marker")
        if len(text) < 1500:
            failures.append(f"{name}: unexpectedly short")
        if "\t" in text:
            failures.append(f"{name}: contains tab characters")
    combined = "\n".join((ROOT / name).read_text(encoding="utf-8") for name in required if (ROOT / name).exists()).lower()
    for group, words in keywords.items():
        for word in words:
            if word.lower() not in combined:
                failures.append(f"Knowledge pack missing keyword '{word}' for group '{group}'")
    if failures:
        print("QA FAILED")
        for f in failures:
            print(f"- {f}")
        raise SystemExit(1)
    print("QA PASSED")
    print(f"Checked {len(required)} knowledge files.")
    for name in required:
        p = ROOT / name
        text = p.read_text(encoding="utf-8")
        print(f"- {name}: {len(text):,} chars")

if __name__ == "__main__":
    main()
