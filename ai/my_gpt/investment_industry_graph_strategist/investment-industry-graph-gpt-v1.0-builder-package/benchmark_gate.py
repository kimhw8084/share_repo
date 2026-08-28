from pathlib import Path

ROOT = Path(__file__).resolve().parent

KNOWLEDGE_FILES = [
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

BENCHMARKS = {
    "AI infrastructure": [
        "gpu", "hbm", "advanced packaging", "data center", "power",
        "cooling", "networking", "optics", "inference economics",
        "enterprise adoption",
    ],
    "GLP-1 drugs": [
        "api manufacturing", "fill-finish", "injector", "payer",
        "pharmacy", "prescriber", "patient adherence", "side effects",
        "reimbursement", "clinical trial",
    ],
    "Copper mining": [
        "ore grade", "mine permitting", "smelting", "refining",
        "concentrate", "treatment charge", "grid demand", "ev",
        "china demand", "inventory",
    ],
    "Nuclear power": [
        "reactor", "uranium", "enrichment", "fuel fabrication",
        "regulatory approval", "safety", "waste", "grid reliability",
        "power purchase agreement", "construction risk",
    ],
    "Private credit": [
        "direct lending", "spread", "default rate", "covenant",
        "fundraising", "bank regulation", "middle market",
        "interest rate", "liquidity", "valuation",
    ],
}

ARCHETYPE_QUERY_BUNDLES = [
    "technology infrastructure",
    "pharma healthcare",
    "commodity materials",
    "regulated energy",
    "financial services",
]

TRACEABILITY_ANCHORS = [
    "evidence",
    "signal",
    "node/edge",
    "money-flow",
    "investment theme",
    "catalyst",
    "falsifier",
]

def combined_text():
    parts = []
    for name in KNOWLEDGE_FILES:
        p = ROOT / name
        if p.exists():
            parts.append(p.read_text(encoding="utf-8"))
    return "\n".join(parts).lower()

def main():
    text = combined_text()
    score = 100
    failures = []

    for industry, anchors in BENCHMARKS.items():
        missing = [a for a in anchors if a.lower() not in text]
        if missing:
            failures.append(f"{industry}: missing benchmark anchors {missing}")
            score -= min(20, len(missing) * 2)

    for bundle in ARCHETYPE_QUERY_BUNDLES:
        if bundle not in text:
            failures.append(f"missing deep-research query bundle for archetype: {bundle}")
            score -= 4

    for anchor in TRACEABILITY_ANCHORS:
        if anchor not in text:
            failures.append(f"missing traceability anchor: {anchor}")
            score -= 3

    if "evidence → signal" not in text and "evidence -> signal" not in text:
        failures.append("missing explicit evidence-to-thesis traceability chain")
        score -= 10

    if "gold standard" not in text:
        failures.append("missing gold-standard output pattern guidance")
        score -= 8

    print(f"BENCHMARK SCORE: {score}/100")
    if failures:
        print("FAILURES:")
        for f in failures:
            print(f"- {f}")
        raise SystemExit(1)
    if score < 95:
        print("FAILURES:")
        print("- benchmark score below 95")
        raise SystemExit(1)
    print("BENCHMARK GATE PASSED")

if __name__ == "__main__":
    main()
