# Bottleneck Detection Playbook

Version: 1.0  
Use this file to identify, classify, rank, and explain obvious and hidden bottlenecks in an industry value chain.

## Objective

The GPT must find where growth, margin, adoption, or strategic control is constrained. The best investment opportunities often appear near bottlenecks before the market fully prices them.

## Bottleneck definition

A bottleneck is any constraint that limits industry growth, raises cost, delays adoption, concentrates pricing power, increases risk, or redirects money flow.

## Bottleneck categories

| Category | Examples |
|---|---|
| Physical capacity | factories, mines, fabs, warehouses, ports |
| Technical limit | performance ceiling, latency, yield, reliability |
| Energy | electricity availability, grid interconnection, fuel, cooling |
| Materials | copper, lithium, rare earths, specialty chemicals |
| Components | chips, sensors, optics, batteries, transformers |
| Infrastructure | grid, data centers, logistics, pipelines, charging networks |
| Regulation | permitting, approvals, export controls, safety rules |
| Labor/talent | nurses, pilots, electricians, chip engineers, welders |
| Capital | financing cost, capex availability, balance-sheet capacity |
| Data | access, quality, privacy, rights, labeling |
| Trust/adoption | safety, cybersecurity, compliance, user acceptance |
| Integration | workflow fit, interoperability, legacy systems |
| Geopolitical | trade restrictions, chokepoints, sanctions |
| Manufacturing yield | defect rates, ramp difficulty, quality control |
| Customer budget | willingness/ability to pay, procurement cycle |

## Bottleneck discovery questions

Ask:

1. What must scale for downstream demand to be met?
2. Which input has the longest lead time?
3. Which node has the fewest qualified suppliers?
4. Which node has the highest switching cost?
5. Which node has high technical difficulty or yield risk?
6. Which regulation or permit can delay deployment?
7. Which cost item can destroy margins?
8. Which customer objection blocks adoption?
9. Which node is small today but becomes critical if demand doubles?
10. Which constraint is mentioned indirectly in capex, hiring, earnings calls, or procurement?

## Hidden bottleneck signals

Hidden bottlenecks may appear through:

- Rising lead times
- Backlog growth
- Capex acceleration in overlooked categories
- Hiring spikes for niche roles
- Supplier qualification delays
- Regulatory filing delays
- Local power constraints
- Increasing customer integration complaints
- Sudden price increases in obscure components
- Strategic partnerships around one input
- Startups clustering around one pain point
- Patents around cost/performance constraints

Mark these as:

`Hidden / Underpriced / Weak-Signal Thesis`

## Bottleneck ranking formula

Score each bottleneck from 1–5:

- Urgency
- Economic impact
- Probability
- Investment upside
- Market underpricing
- Time to catalyst
- Evidence strength

Optional total:

`Bottleneck score = urgency + economic impact + probability + investment upside + underpricing + catalyst + evidence`

Interpretation:

- 30–35: critical priority
- 24–29: high priority
- 17–23: watchlist
- below 17: monitor only

## Winner/loser logic

For each bottleneck, identify:

- Who benefits if it worsens?
- Who benefits if it is solved?
- Who is squeezed?
- Who can pass through cost?
- Who has pricing power?
- Who must spend capex?
- Who has the scarce asset?

Example:

If grid interconnection is a bottleneck:

- Beneficiaries if worsens: owners of power-ready sites, backup generation, grid equipment, local utilities with capacity
- Beneficiaries if solved: data center developers, cloud providers, AI customers
- Losers/squeezed: projects without secured power, customers facing higher compute costs

## Bottleneck output table

| Bottleneck | Type | Affected nodes | Why it matters | Who benefits if worsens | Who benefits if solved | Evidence | Score | Confidence |
|---|---|---|---|---|---|---|---|---|

## Anti-generic rule

Do not say only “regulation is a risk” or “supply chain is a bottleneck.”

Specify:

- Which regulation?
- Which permit?
- Which component?
- Which supplier group?
- Which geography?
- Which customer segment?
- Which timeline?

## Self-audit checklist for bottleneck quality

Before finalizing, check:

- Did the report identify both obvious and hidden bottlenecks?
- Did it rank bottlenecks instead of merely listing them?
- Did it explain who benefits if each bottleneck worsens?
- Did it explain who benefits if each bottleneck is solved?
- Did it separate real bottlenecks from ordinary risks?
- Did it identify the timing: immediate, 1 year, or 1–5 years?
- Did it avoid generic labels such as “supply chain risk” without naming the constrained node?

If no hidden bottleneck is found, explicitly say whether none was found or evidence was insufficient.
