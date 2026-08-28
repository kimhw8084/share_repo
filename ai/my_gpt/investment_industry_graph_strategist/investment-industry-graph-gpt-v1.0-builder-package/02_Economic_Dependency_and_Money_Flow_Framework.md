# Economic Dependency and Money Flow Framework

Version: 1.0  
Use this file to trace who pays whom, where value is captured, where capex/opex flows, and why a technically important node may or may not be investable.

## Objective

The GPT must treat money flow as the spine of the analysis. Product flow explains how the industry works; money flow explains where investors should look.

Always separate:

- Product/service flow
- Data flow
- Revenue flow
- Margin flow
- Capex flow
- Opex flow
- Pricing-power flow
- Risk flow

## Money-flow questions

For each major node, answer:

1. Who pays?
2. Who receives revenue?
3. Who controls the budget?
4. Is the spending capex or opex?
5. Is demand recurring, one-time, cyclical, regulated, usage-based, or discretionary?
6. Where does gross margin concentrate?
7. Where does operating leverage exist?
8. Who has pricing power?
9. Who is squeezed when input costs rise?
10. Who benefits when volume grows?
11. Who benefits if the bottleneck worsens?
12. Who benefits if the bottleneck is solved?

## Value capture vs technical importance

Never assume technical importance equals investment attractiveness.

| Situation | Interpretation |
|---|---|
| High technical importance + weak pricing power | Critical but poor value capture |
| Low technical complexity + supply scarcity | Potentially strong value capture |
| Platform controls customers | Margin may flow to platform |
| Commodity input with shortage | Cyclical upside but high downside risk |
| Regulated asset | Lower explosive upside, possible durable return |
| Services layer | Fast adoption signal, often lower moat |
| Software layer | High margin if it owns workflow/data/customer |

## Business model taxonomy

Classify major nodes by business model:

- Hardware sale
- Component sale
- Commodity/material sale
- Subscription software
- Usage-based software/API
- Licensing/royalty
- Advertising
- Services/consulting/integration
- Marketplace/take-rate
- Regulated return
- Government contract
- Insurance/premium
- Financing/spread income
- Leasing/rental
- Maintenance/aftermarket
- Data monetization
- Hybrid

## Revenue-flow map format

Use this format:

`Final customer budget → buyer/intermediary → focal product/service → suppliers/enablers → scarce inputs`

Example:

`Enterprise AI budget → cloud provider/API vendor → GPU data center capacity → GPU/HBM/networking/cooling/power suppliers → semiconductor equipment/materials/grid equipment`

## Capex-flow map format

Use this format:

`Growth expectation → capacity owner capex → equipment/infrastructure suppliers → component/material suppliers`

Example:

`AI demand growth → hyperscaler data center capex → servers, networking, cooling, power equipment → GPUs, HBM, optical modules, switchgear, transformers, copper`

## Opex-flow map format

Use this format:

`Operating usage → recurring cost drivers → margin pressure or pass-through`

Example:

`AI inference usage → electricity + cloud operation + model serving cost → margin pressure unless pricing/efficiency improves`

## Pricing power indicators

Positive indicators:

- Scarce capacity
- High switching cost
- Mission-critical input
- Regulatory approval barrier
- Technical monopoly/oligopoly
- Long qualification cycle
- Customer cannot easily dual-source
- Demand grows faster than supply
- Standards or ecosystem lock-in
- Strong brand/trust requirement

Negative indicators:

- Many suppliers
- Low differentiation
- Customer can insource
- Customer has purchasing power
- Product commoditizes quickly
- Easy substitution
- No recurring relationship
- High inventory cycles
- Price transparency

## Margin pool analysis

For each major node, classify:

- Revenue size: low, medium, high, very high
- Gross margin: low, medium, high
- Operating leverage: low, medium, high
- Capex intensity: low, medium, high
- Cyclicality: low, medium, high
- Pricing power: weak, medium, strong
- Investability: public, private, indirect, not investable

## Budget-owner rule

Investment insight improves when the actual budget owner is identified.

Examples:

- AI software: CIO, CTO, business unit leader, developer team, procurement
- Hospital equipment: hospital system, payer, government, department budget
- Grid equipment: utility capex budget, regulator-approved rate base
- Defense technology: defense ministry/agency procurement
- Consumer goods: household discretionary income

## Economic dependency categories

A node is economically dependent on another node when it depends on:

- Input cost
- Supply availability
- Customer budget
- Financing cost
- Regulation
- Technical standard
- Distribution access
- Data access
- Trust/safety
- Installed base
- Complementary infrastructure

## Output requirement

Every full report must include:

- Product-flow map
- Money-flow map
- Capex-flow map where applicable
- Margin-pool table
- Budget-owner identification
- Value-capture explanation

## Self-audit checklist for money-flow quality

Before finalizing, check:

- Is the buyer different from the final user? If yes, identify both.
- Is capex separated from opex?
- Is revenue growth separated from margin capture?
- Did the report identify who has pricing power and why?
- Did it explain who benefits if the key bottleneck worsens?
- Did it explain who benefits if the key bottleneck is solved?
- Did it avoid assuming technical importance equals investability?
- Did it identify public/private/indirect exposure where possible?

If the report cannot explain who pays, who captures margin, and who is squeezed, the investment recommendation is not ready.
