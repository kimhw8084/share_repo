from pathlib import Path

ROOT = Path(__file__).resolve().parent
INSTRUCTION = ROOT / "GLOBAL_GPT_LAW_v1.0.txt"
LIMIT = 8000

REQUIRED = [
    "Investment Industry Graph Strategist",
    "00_Knowledge_Pack_Index_and_Routing.md",
    "`01`",
    "`02`",
    "`03`",
    "`04`",
    "`05`",
    "`06`",
    "`07`",
    "`08`",
    "`09`",
    "`10`",
    "`11`",
    "`12`",
    "`13`",
    "Hypothesis graph",
    "Deep research",
    "Graph repair",
    "Money conversion",
    "Bottleneck radar",
    "Simulation",
    "Theme scoring",
    "Traceability",
    "Self-audit",
    "Reusable snapshot",
    "Do not invent",
    "personalized buy/sell",
]

def main():
    text = INSTRUCTION.read_text(encoding="utf-8")
    failures = []
    if len(text) > LIMIT:
        failures.append(f"Instruction too long: {len(text)} > {LIMIT}")
    if len(text) < 5000:
        failures.append(f"Instruction may be too short for this GPT: {len(text)} chars")
    for item in REQUIRED:
        if item not in text:
            failures.append(f"Missing required anchor: {item}")
    if "Evidence → Signal → Node/Edge → Money-flow/Bottleneck → Investment Theme → Catalyst → Falsifier" not in text:
        failures.append("Missing exact evidence-to-thesis traceability chain")
    print(f"INSTRUCTION LENGTH: {len(text)} / {LIMIT}")
    if failures:
        print("INSTRUCTION GATE FAILED")
        for f in failures:
            print(f"- {f}")
        raise SystemExit(1)
    print("INSTRUCTION GATE PASSED")

if __name__ == "__main__":
    main()

