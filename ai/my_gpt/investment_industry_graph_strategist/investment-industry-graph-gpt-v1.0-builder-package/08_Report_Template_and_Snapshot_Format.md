# Report Template and Snapshot Format

Version: 1.0  
Use this file to structure full industry reports and create reusable snapshots for future updates.

## Objective

Every full report should be consistent, investment-grade, readable for non-experts, and reusable in future sessions.

## Full report structure

Use this order:

1. Executive Investment Conclusion
2. Industry Definition and Scope
3. Zero-to-One Explanation
4. Upstream/Downstream Graph
5. Final Customer Demand Map
6. Money-Flow Map
7. Company Layer
8. Current 30-Day Signal Table
9. Bottleneck Radar
10. Hidden Bottleneck Watchlist
11. Simulation Scenarios
12. Investment Theme Ranking
13. Future Trend Prediction
14. Strategic Recommendation
15. Assumption Audit
16. Pre-Final Self-Audit
17. Evidence/Citation List
18. Reusable Snapshot

## 1. Executive Investment Conclusion

Short, decisive, 5–10 lines.

Include:

- What matters most
- Where money is moving
- Most important bottleneck
- Hidden/underpriced thesis
- Best investment theme
- Main risk
- Confidence

## 2. Industry Definition and Scope

Include:

- Focal industry
- Geography
- Time horizon
- Scope assumption
- What is excluded
- Whether clarification would improve precision

## 3. Zero-to-One Explanation

Explain for an intelligent non-expert:

- What this industry does
- Who needs it
- Why it exists
- What must happen for it to grow
- Where money normally comes from

## 4. Upstream/Downstream Graph

Use graph-like bullets:

```text
Upstream:
Input/material → component → infrastructure/enabler → focal industry

Center:
Focal industry

Downstream:
Focal industry → use case → buyer → final customer
```

Separate:

- Core graph
- Watchlist graph

## 5. Final Customer Demand Map

Table:

| Final customer | What they want | Budget owner | Demand driver | Adoption friction | Impact on graph |
|---|---|---|---|---|---|

## 6. Money-Flow Map

Include:

- Revenue flow
- Margin flow
- Capex flow
- Opex flow
- Pricing-power nodes

Table:

| Money path | Who pays | Who captures value | Capex/opex | Pricing power | Investment meaning |
|---|---|---|---|---|---|

## 7. Company Layer

For major nodes:

| Node | Key companies | Why they matter | Market/control evidence | Risk |
|---|---|---|---|---|

## 8. Current 30-Day Signal Table

| Signal | Category | Source/evidence | Direction | Affected nodes | Investment meaning | Confidence |
|---|---|---|---|---|---|---|

If current research is unavailable, say so clearly.

## 9. Bottleneck Radar

| Bottleneck | Type | Affected nodes | Why it matters | Score | Confidence |
|---|---|---|---|---|---|

## 10. Hidden Bottleneck Watchlist

| Hidden thesis | Weak signal | Why it may matter | Who benefits | What confirms it | Confidence |
|---|---|---|---|---|---|

## 11. Simulation Scenarios

| Scenario | Immediate effect | 1-year effect | Bottlenecks | Winners | Losers | Themes strengthened | Confidence |
|---|---|---|---|---|---|---|---|

## 12. Investment Theme Ranking

| Rank | Theme | Type | Score | Thesis | Catalyst | Beneficiaries | Risk | Confidence |
|---|---|---|---|---|---|---|---|---|

For the top three themes, add a traceability line:

`Evidence → Signal → Node/Edge → Money-flow/Bottleneck → Investment Theme → Catalyst → Falsifier`

## 13. Future Trend Prediction

Separate:

- Immediate
- 1 year
- 1–5 years if useful

Label:

- High confidence
- Medium confidence
- Low confidence
- Speculative but important

## 14. Strategic Recommendation

Include:

1. Where to look first
2. What is likely underpriced
3. What to avoid or treat cautiously
4. What evidence would upgrade/downgrade the thesis
5. What to monitor next

## 15. Assumption Audit

Table:

| Assumption | Why it matters | Confidence | What would change the conclusion |
|---|---|---|---|

## 16. Evidence/Citation List

## 16. Pre-Final Self-Audit

Before finalizing a full report, silently run the self-audit protocol. If important weaknesses are found, repair the report before presenting it. If a weakness cannot be repaired because evidence is missing, disclose it in the assumption audit.

Minimum checks:

- Missing critical nodes
- Unsupported current claims
- Weak or absent money-flow logic
- Downstream paths not ending at final customers
- Bottlenecks too generic
- Simulations lacking second-order effects
- Investment themes too generic
- Confidence too high for evidence quality

Only show a short self-audit summary when it helps the user trust the result or when evidence remains insufficient.

## 17. Evidence/Citation List

Include:

- Source title
- Owner/publisher
- Date
- What it supports
- Source quality tier

## 18. Reusable Snapshot

Use this exact block:

```text
REUSABLE INDUSTRY SNAPSHOT
Industry:
Date:
Geography:
Scope assumption:
Core upstream nodes:
Core downstream nodes:
Watchlist nodes:
Final customer segments:
Key edges:
Top money-flow paths:
Top bottlenecks:
Hidden bottlenecks:
Top investment themes:
Confidence levels:
Key citations/sources:
Assumptions:
Unresolved questions:
Changes vs previous snapshot:
END SNAPSHOT
```

## Update-from-snapshot method

When the user provides a previous snapshot:

1. Parse old scope, nodes, edges, bottlenecks, and themes.
2. Research latest 30-day signals.
3. Mark changes:
   - new node
   - removed node
   - strengthened edge
   - weakened edge
   - new bottleneck
   - resolved bottleneck
   - upgraded theme
   - downgraded theme
4. Provide updated snapshot.
