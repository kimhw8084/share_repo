# Deep Research Execution Protocol

Version: 1.0  
Use this file when a user asks for a full industry report, current market status, citations, investment themes, or any analysis that depends on recent evidence.

## Objective

The GPT must use research as a targeted evidence engine, not as random web browsing. Research should verify, falsify, and improve the industry graph, money-flow map, bottleneck radar, simulations, and investment themes.

The ideal process is:

`hypothesis graph → targeted research plan → source triangulation → evidence grading → graph repair → investment synthesis`

## When to use deep research

Use deep research or web research when:

- The user asks for a full industry report.
- The user wants investment insight.
- Current status matters.
- Company rankings, market share, revenue, capex, regulation, prices, or recent events are involved.
- The report includes a current 30-day signal table.
- The answer includes citations or source evidence.
- The analysis makes a hidden bottleneck or underpriced-theme claim.

If deep research tools are unavailable, say:

`Current deep research was unavailable in this run. I can provide a framework-level analysis, but current-status conclusions should be verified.`

## Research-pass structure

### Pass 1: Hypothesis graph before search

Before searching, draft a hypothesis graph:

- Focal industry
- Upstream nodes
- Downstream nodes
- Final customers
- Likely money-flow paths
- Obvious bottlenecks
- Possible hidden bottlenecks
- Candidate investment themes

Purpose: guide search queries and avoid shallow source collection.

### Pass 2: Source plan

Search by evidence type, not just by industry name.

Use query groups:

1. Industry structure and value chain
2. Last-30-day news and current signals
3. Public company filings and earnings calls
4. Investor presentations and capex guidance
5. Government/regulatory/statistical data
6. Supply chain, shortages, lead times
7. Pricing and margin signals
8. Technology breakthroughs and patents
9. Job postings/hiring clusters
10. Funding, M&A, and private-market signals
11. Customer adoption and pain points

### Pass 3: Source quality triage

Prioritize:

1. Primary sources
2. Official data
3. Reputable financial/news sources
4. Technical papers/patents
5. Weak-signal sources

Never let blogs, social media, or isolated anecdotes drive a high-confidence conclusion.

### Pass 4: Evidence extraction

For each useful source, extract:

- What changed?
- Which graph node does it affect?
- Which edge does it strengthen/weaken?
- Does it affect demand, supply, pricing, margins, capex, opex, regulation, or risk?
- Does it reveal a bottleneck?
- Does it create or weaken an investment theme?
- What is the confidence?

### Pass 5: Graph repair

After research, update the hypothesis graph:

- Add missing nodes.
- Remove unsupported nodes.
- Move nodes between core graph and watchlist graph.
- Strengthen/weaken edges.
- Add new bottlenecks.
- Update final customer demand map.
- Update money-flow paths.

### Pass 6: Triangulation

For important claims, seek at least two support types when possible:

- Company source + market source
- Filing/transcript + government data
- News report + official announcement
- Capex announcement + supplier signal
- Hiring signal + product strategy
- Patent signal + product roadmap

If only one weak source supports a claim, label it weak signal or evidence insufficient.

### Pass 7: Stop condition

Research is sufficient when:

- Critical graph nodes are identified.
- Top money-flow paths are supported.
- Current signals are not based on a single weak source.
- Bottlenecks have evidence or are labeled weak-signal theses.
- Investment themes have catalysts, risks, and falsifiers.
- Remaining uncertainty is explicit.

Research is not sufficient when:

- Company rankings are unsupported.
- Current claims lack dates/sources.
- A major bottleneck is asserted but not evidenced.
- The report cannot explain who pays and who captures value.
- Investment themes are generic.

## Query design examples

Use targeted query patterns:

- `[industry] value chain upstream downstream`
- `[industry] earnings call capex demand supply bottleneck`
- `[industry] shortage lead time capacity expansion`
- `[industry] regulation policy subsidy export control`
- `[industry] investor presentation margin pricing`
- `[industry] patent breakthrough cost reduction`
- `[industry] hiring [specialized role] demand signal`
- `[industry] customer adoption friction compliance`

For company-heavy nodes:

- `[company] 10-K segment revenue risk factors`
- `[company] earnings call backlog capex guidance`
- `[company] investor presentation capacity expansion`

## Industry-archetype query bundles

When a user asks for a full report, identify the closest archetype and use targeted query bundles from `12_Industry_Archetype_Checklists_and_Query_Bundles.md`.

Required archetypes:

- Technology infrastructure
- Pharma healthcare
- Commodity materials
- Regulated energy
- Financial services

These bundles improve deep research because the best evidence sources differ by industry. Pharma needs clinical trial, reimbursement, and manufacturing capacity searches. Commodity materials need ore grade, permitting, inventory, treatment charge, and demand searches. Financial services need spread, default rate, covenant, fundraising, liquidity, and bank regulation searches.

## Evidence-to-output mapping

Every important source should map to at least one output section:

| Evidence type | Output section |
|---|---|
| Filing risk factor | Assumption audit, bottleneck radar |
| Earnings call demand comment | Current signal table, demand map |
| Capex guidance | Money-flow map, investment themes |
| Government data | Market context, regulation, demand/supply |
| Patent/technical paper | Technology breakthrough scenario |
| Job postings | Weak-signal watchlist |
| Funding/M&A | Private-market signal, theme crowding |
| Customer complaint/adoption friction | Bottleneck radar, solution theme |

## Evidence-to-thesis traceability

For the top three investment themes, trace:

`Evidence → Signal → Node/Edge → Money-flow/Bottleneck → Investment Theme → Catalyst → Falsifier`

If this chain cannot be completed, downgrade confidence or remove the theme.

## Research failure modes

Avoid:

- Collecting sources without updating the graph
- Overweighting recent news over structural economics
- Treating market size as investment attractiveness
- Using source quantity instead of source quality
- Ignoring contradictory sources
- Failing to identify final customer budget
- Failing to distinguish actual data from analyst opinion

## Final research disclosure

In the final report, include:

- What research window was used
- Which source types were strongest
- Which areas remain weakly evidenced
- Which claims are inference or weak-signal thesis
