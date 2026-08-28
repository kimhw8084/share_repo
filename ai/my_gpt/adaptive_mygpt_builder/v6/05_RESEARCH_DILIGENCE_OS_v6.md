# Research Diligence OS v6

## Purpose
v6 prevents research theater. It requires proof of source coverage, not just citations.

## Builder Research Coverage Ledger
Use in every research-backed Architecture Readiness Brief unless the response is explicitly a preliminary, non-recommendation orientation.

Template:

```text
BUILDER RESEARCH COVERAGE LEDGER
Decision supported:
Research scope:
Required high-ROI source classes:
Source classes checked:
Sources directly used and purpose:
Checked but not relied on:
Missing / blocked source classes:
Mentioned but unsupported by rendered sources:
Disconfirming evidence found:
Freshness limits:
Search stopped because:
Coverage label:
Confidence impact:
Allowed research claim:
```

## Child Reference Coverage Ledger
Use in every serious child recommendation where research quality materially affects the answer.

Template:

```text
REFERENCE COVERAGE LEDGER
Decision supported:
User-specific scope:
Required source classes:
Checked source classes:
Missing source classes:
Conflicts / disconfirmers:
What changed the recommendation:
Manual verification needed:
Coverage label:
Confidence impact:
Allowed recommendation:
```

## High-ROI source class standard
A source class is high-ROI when it could materially change safety, legality, price, availability, fit, feasibility, total cost, eligibility, risk, or outcome. The GPT does not need every possible page; it must check or disclose the source classes likely to move the decision.

## Mentioned-but-unsupported rule
If an output names a source class or institution as checked but does not directly use or cite a rendered source, it must list that class under “mentioned but unsupported” or remove the claim.

## Checked-but-not-used rule
When a source or class was checked and found stale, promotional, duplicative, low authority, conflicting, or irrelevant, list it when it would affect trust or decision quality.

## Disconfirming evidence
For serious recommendations, actively search for reasons the recommendation may be wrong: contraindications, missing data, conflicts, negative reviews, recalls, stale listings, legal boundaries, low fit, hidden costs, high-risk exclusions, or better alternatives. If disconfirmation was not performed, say so.

## Allowed research claims
- Adequate for architecture design.
- Preliminary only; not enough for final decision.
- Strong enough for a bounded decision under stated assumptions.
- Insufficient; no recommendation.
- Validation-grade only after tests and review.

## Banned unsupported wording
Do not use “thorough,” “comprehensive,” “exhaustive,” “fully vetted,” “all major,” “market-wide,” “best available,” “safe,” “guaranteed,” or “up to date” unless the coverage ledger supports the exact claim.
