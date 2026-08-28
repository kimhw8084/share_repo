from pathlib import Path
import re

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

REQUIRED_ANCHORS = {
    "one_shot_loop": [
        "hypothesis graph",
        "deep research",
        "graph repair",
        "money-flow",
        "bottleneck",
        "simulation",
        "investment",
        "self-audit",
    ],
    "graph_quality": [
        "upstream",
        "downstream",
        "final customer",
        "edge type",
        "materiality",
        "watchlist",
    ],
    "money_quality": [
        "who pays",
        "margin",
        "capex",
        "opex",
        "pricing power",
        "value capture",
    ],
    "evidence_quality": [
        "source priority",
        "fact",
        "inference",
        "weak signal",
        "confidence",
        "do not invent",
    ],
    "research_quality": [
        "source plan",
        "triangulation",
        "evidence extraction",
        "stop condition",
        "research failure modes",
    ],
    "archetype_quality": [
        "technology infrastructure",
        "pharma healthcare",
        "commodity materials",
        "regulated energy",
        "financial services",
    ],
    "traceability_quality": [
        "evidence → signal",
        "node/edge",
        "falsifier",
        "gold standard",
    ],
    "bottleneck_quality": [
        "hidden",
        "who benefits if",
        "score",
        "urgency",
        "underpriced",
    ],
    "simulation_quality": [
        "first-order",
        "second-order",
        "winners",
        "losers",
        "falsifiers",
    ],
    "theme_quality": [
        "roi potential",
        "catalyst",
        "falsification",
        "downside risk",
        "theme type",
    ],
    "output_quality": [
        "executive investment conclusion",
        "evidence/citation",
        "reusable snapshot",
        "assumption audit",
        "strategic recommendation",
    ],
    "evaluation_quality": [
        "score",
        "failure mode",
        "retest",
        "autonomous improvement",
    ],
}

def read(name):
    return (ROOT / name).read_text(encoding="utf-8")

def version_of(text):
    m = re.search(r"^Version:\s*([0-9]+\.[0-9]+)", text, re.M)
    return m.group(1) if m else None

def main():
    failures = []
    warnings = []
    score = 100

    for name in KNOWLEDGE_FILES:
        p = ROOT / name
        if not p.exists():
            failures.append(f"missing knowledge file: {name}")
            score -= 10
            continue
        text = read(name)
        if not text.startswith("# "):
            failures.append(f"{name}: missing H1")
            score -= 2
        if len(text) < 2500:
            warnings.append(f"{name}: short file ({len(text)} chars)")
            score -= 1
        if len(text) > 12000:
            warnings.append(f"{name}: may be too long for focused retrieval ({len(text)} chars)")
            score -= 1

    combined = "\n".join(read(name) for name in KNOWLEDGE_FILES if (ROOT / name).exists()).lower()

    for group, anchors in REQUIRED_ANCHORS.items():
        missing = [a for a in anchors if a.lower() not in combined]
        if missing:
            failures.append(f"{group}: missing anchors {missing}")
            score -= 3 * len(missing)

    index = read("00_Knowledge_Pack_Index_and_Routing.md") if (ROOT / "00_Knowledge_Pack_Index_and_Routing.md").exists() else ""
    for name in KNOWLEDGE_FILES[1:]:
        if name not in index:
            failures.append(f"routing file does not reference {name}")
            score -= 3

    readme = read("README.md") if (ROOT / "README.md").exists() else ""
    for name in KNOWLEDGE_FILES:
        if name not in readme:
            failures.append(f"README upload list missing {name}")
            score -= 2

    versions = {name: version_of(read(name)) for name in KNOWLEDGE_FILES if (ROOT / name).exists()}
    version_set = {v for v in versions.values() if v is not None}
    if len(version_set) > 2:
        warnings.append(f"many mixed versions: {versions}")
        score -= 2
    if None in versions.values():
        failures.append("at least one file missing Version marker")
        score -= 5

    forbidden_uploads = ["qa_check.py", "quality_gate.py", "README.md", "CHANGELOG.md"]
    if "Do not upload" not in readme:
        failures.append("README lacks do-not-upload guidance")
        score -= 3
    for f in forbidden_uploads:
        if f not in readme and f in ["qa_check.py", "quality_gate.py"]:
            failures.append(f"README should mention not uploading {f}")
            score -= 1

    if "current deep research was unavailable" not in combined:
        warnings.append("missing explicit fallback phrase for unavailable deep research")
        score -= 1

    print(f"QUALITY SCORE: {score}/100")
    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"- {w}")
    if failures:
        print("FAILURES:")
        for f in failures:
            print(f"- {f}")
        raise SystemExit(1)
    if score < 95:
        print("FAILURES:")
        print("- score below release threshold 95")
        raise SystemExit(1)
    print("QUALITY GATE PASSED")

if __name__ == "__main__":
    main()
