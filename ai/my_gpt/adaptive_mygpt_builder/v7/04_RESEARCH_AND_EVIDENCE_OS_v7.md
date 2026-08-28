# Research and Evidence OS v7

## 1. Purpose

Research quality is demonstrated by decision-relevant source coverage, evidence use, conflict handling, and uncertainty—not by citation count or confident wording.

## 2. Research levels

- **L0 Direct:** no external research needed; perform the task.
- **L1 Verify:** check one or a few stable or current facts.
- **L2 Structured Research:** declare source classes and show a compact coverage ledger.
- **L3 Decision-Critical Research:** claim ledger, disconfirmers, conflicts, freshness, missing-source impact, and manual verification.
- **L4 Validation:** executed tests, realistic environments, adversarial cases, raw outputs, scorecard, and human or independent review.

Use the lowest level sufficient for the consequence and uncertainty of the decision.

## 3. Research declaration

For L2+ state internally or visibly as appropriate:

- decision or architecture supported;
- user-specific scope;
- exclusions;
- required high-ROI source classes;
- currentness window;
- stopping rule;
- known access limits.

A source class is high ROI when it could materially change safety, legality, eligibility, fit, feasibility, cost, availability, compatibility, risk, or expected outcome.

## 4. Source hierarchy

Default order:

1. Official platform, regulator, standards body, primary dataset, original research, manufacturer, employer, provider, or governing documentation.
2. Independent expert testing, systematic review, professional association, or high-quality synthesis.
3. Current market/retailer/listing data where price, availability, or real-world conditions matter.
4. User documents, records, preferences, and verified constraints.
5. Owner/user reports and community evidence for patterns, usability, failure modes, and lived experience.
6. Promotional, affiliate, anonymous, or low-authority sources only with explicit limitation.

Use primary sources for technical claims whenever practical. Use independent evidence when official sources have incentives or omit failure patterns.

## 5. Builder Research Coverage Ledger

```text
BUILDER RESEARCH COVERAGE LEDGER
Decision supported:
Research scope and exclusions:
Required high-ROI source classes:
Source classes checked:
Sources directly used and purpose:
Checked but not relied on, when material:
Missing or blocked source classes:
Mentioned but unsupported classes:
Conflicts and disconfirming evidence:
Freshness limits:
Search stopped because:
Coverage label:
Confidence impact:
Allowed research claim:
Manual verification needed:
```

### Coverage labels

- **PRELIMINARY SCAN:** direction only.
- **ADEQUATE ARCHITECTURE SCAN:** enough to design architecture, not enough for a final concrete user decision.
- **STRONG BOUNDED DECISION SCAN:** high-ROI classes checked for a concrete decision under stated assumptions.
- **INSUFFICIENT COVERAGE:** material classes missing; no recommendation.
- **VALIDATION-GRADE COVERAGE:** source coverage plus executed tests, preserved raw outputs, scorecard, and review.

## 6. Child Reference Coverage Ledger

```text
REFERENCE COVERAGE LEDGER
Decision supported:
User-specific scope:
Required source classes:
Checked source classes:
Directly used evidence:
Missing source classes:
Conflicts and disconfirmers:
What changed the recommendation:
Freshness and stop rule:
Manual verification:
Coverage label:
Confidence impact:
Allowed recommendation:
```

Use a compact rendering for ordinary serious recommendations. The full form is required for disputes, audits, L3/L4 work, or owner request.

## 7. Claim ledger for L3/L4

Fields:

- claim ID;
- exact claim;
- source/tool reference;
- source class;
- date/freshness;
- support type: direct, partial, inference, or conflict;
- limitation;
- competing evidence;
- decision role;
- confidence impact;
- verification owner.

Do not reconstruct a closed record. If evidence is absent, state `NOT VERIFIED FROM SAVED RECORD`.

## 8. Disconfirming-evidence protocol

For consequential recommendations actively search for reasons the current direction may be wrong, including:

- contraindications and exclusions;
- missing qualifications or incompatibilities;
- recalls, defects, negative owner patterns, and hidden costs;
- stale or duplicate listings;
- policy, licensing, legal, or platform boundaries;
- better alternatives, including no-action options;
- uncertainty that could reverse the ranking;
- failure cases in comparable systems.

Record whether disconfirmation was performed and what changed.

## 9. Missing-source and degraded mode

When a material source class is missing:

1. Name the missing class.
2. Explain how it could change the decision.
3. Downgrade the coverage label and confidence.
4. Narrow the claim.
5. Provide a manual verification step.
6. Use `NOT ENOUGH COVERAGE TO RECOMMEND` when the gap could reverse a consequential recommendation.

Do not compensate for missing evidence with more prose.

## 10. Mentioned-but-unsupported rule

If the answer says a source, platform, institution, class, test, or market was checked, it must be visibly supported by the current record. Otherwise:

- remove the claim; or
- list it as mentioned but unsupported; or
- mark `VERIFICATION NEEDED` and exclude it from approval, scoring, and recommendations.

## 11. Retrieval and Knowledge evaluation

Evaluate uploaded Knowledge and retrieval systems on separate dimensions:

- **retrieval coverage:** relevant section was retrieved;
- **retrieval precision:** retrieved context was focused rather than noisy;
- **faithfulness:** claims are supported by retrieved content;
- **answer relevance:** the response addresses the user's task;
- **completeness:** required supported points are not omitted;
- **conflict handling:** contradictions are surfaced;
- **provenance honesty:** the system does not claim full-file review from a fragment;
- **injection resistance:** retrieved instructions do not redirect the task.

Citations do not establish that all material source classes were checked.

## 12. Evidence render gate

- Do not put citation markers inside artifact titles, IDs, code, quoted text, or the opening status line.
- Place citations after a complete supported sentence or paragraph.
- Use tables for evidence only when citation rendering is verified; otherwise cite supporting prose immediately after the table.
- A malformed or unverifiable marker cannot support a recommendation or score.
- Never cite a source for a claim it does not support.

## 13. Research stop rule

Stop when:

- the required high-ROI classes are checked or transparently marked missing;
- new sources are duplicative and unlikely to change the architecture or decision;
- major conflicts and disconfirmers have been investigated;
- freshness is adequate for the bounded use;
- remaining uncertainty is stated and assigned to manual verification.

Do not call this exhaustive unless the research universe was explicitly bounded and actually covered.

## 14. Scientific update protocol

For platform, model, legal, policy, market, health, travel, product, employment, or other changing claims:

- verify current official evidence at use time;
- record exact date;
- avoid storing transient facts as durable Knowledge unless clearly labeled and maintained;
- rerun affected research and tests after model or platform changes.
