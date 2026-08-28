# Simulation Engine Playbook

Version: 1.0  
Use this file to simulate how shocks or changes move through the industry graph and convert into investment implications.

## Objective

The GPT must model how pressure moves through the graph when downstream demand, supply, prices, regulation, or technology changes.

Simulation is not prediction certainty. It is structured causal reasoning with assumptions.

## Default horizons

Always show:

- Immediate effect
- 1-year effect

Add 1–5 year structural effect when relevant.

## Required scenario types

For full reports, simulate:

1. Downstream demand increase
2. Downstream demand decrease
3. Customer mix shift
4. Supply shock
5. Price shock
6. Regulation shock
7. Technology breakthrough
8. Combined scenario

## Customer mix rule

Always distinguish:

- Consumer demand
- Enterprise demand
- Government demand
- Industry-specific demand

Reason: each demand type has different budgets, adoption speed, compliance needs, margin impact, and upstream pressure.

## Simulation input format

If the user provides a scenario:

`Scenario: [customer segment/input] changes by [amount] over [time] in [geography].`

If user does not provide one, create reasonable default scenarios and state assumptions.

## Simulation output fields

For each scenario:

- Scenario assumption
- Immediate effect
- 1-year effect
- First-order effects
- Second-order effects
- Affected nodes
- New or intensified bottlenecks
- Winners
- Losers
- Revenue impact
- Margin impact
- Capex impact
- Opex impact
- Investment themes strengthened
- Investment themes weakened
- Confidence level
- Falsifiers

## First-order vs second-order

First-order effects are direct.

Example:

`Enterprise AI demand rises → cloud/data center demand rises`

Second-order effects are indirect.

Example:

`Cloud/data center demand rises → power interconnection queues worsen → power-ready sites gain scarcity value → grid equipment and backup power demand rises`

## Scenario templates

### Demand increase

Ask:

- Which customer segment increases demand?
- Is demand usage-based or capex-driven?
- Which downstream layer captures revenue first?
- Which upstream nodes face pressure next?
- Which bottleneck becomes tighter?
- Can suppliers raise price?

### Demand decrease

Ask:

- Where does excess capacity appear?
- Which nodes lose pricing power?
- Which suppliers face inventory correction?
- Which customers gain negotiating power?
- Which investment themes weaken?

### Customer mix shift

Ask:

- Does demand shift from consumer to enterprise, enterprise to government, or broad to specialized industry use?
- Does compliance/security need rise?
- Does unit economics improve or worsen?
- Does sales cycle change?
- Does infrastructure requirement change?

### Supply shock

Ask:

- Which node loses capacity?
- Is there substitute supply?
- How long is lead time?
- Who has inventory?
- Who can pass through price?
- Who gains scarcity value?

### Price shock

Ask:

- Which cost rises or falls?
- Is the cost capex or opex?
- Who absorbs vs passes through?
- Which substitutes become attractive?
- Which margins compress or expand?

### Regulation shock

Ask:

- Does regulation restrict supply, demand, exports, approvals, data use, safety, or capital?
- Who is compliant already?
- Who must spend to comply?
- Does regulation create a moat?

### Technology breakthrough

Ask:

- Which bottleneck is reduced?
- Which old node is commoditized?
- Which new bottleneck appears?
- Does demand expand because cost falls?
- Does value shift from hardware to software, from services to platform, or from scarce input to downstream adoption?

### Combined scenario

Use when multiple shocks interact.

Example:

`Enterprise demand +100%, power prices +30%, export controls tighten`

Trace interaction effects, not isolated effects.

## Simulation table

| Scenario | Immediate effect | 1-year effect | Bottlenecks | Winners | Losers | Themes strengthened | Confidence |
|---|---|---|---|---|---|---|---|

## Caution

Never present simulation as guaranteed. Present it as:

`If assumptions hold, pressure likely moves through the graph this way.`

## Self-audit checklist for simulation quality

Before finalizing, check:

- Did the simulation start from the final customer or specified shock?
- Did it show both immediate and 1-year effects?
- Did it include first-order and second-order effects?
- Did it identify winners, losers, new bottlenecks, margin impact, and capex impact?
- Did it distinguish consumer, enterprise, government, and industry-specific demand where relevant?
- Did it state assumptions and falsifiers?
- Did at least one scenario combine multiple shocks when the industry is complex?

If a simulation only restates that demand rises or falls, it is not deep enough.
