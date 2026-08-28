# Current Signal Extraction Playbook

Version: 1.0  
Use this file to identify what is changing right now in an industry, especially during the default last-30-day research window.

## Objective

The GPT must not only describe structure. It must extract signals that indicate changing demand, supply, pricing, margins, regulation, capex, bottlenecks, and investor attention.

## Signal categories

### Demand signals

Look for:

- Revenue acceleration/deceleration
- Bookings, backlog, orders, reservations
- Usage metrics
- Customer adoption
- Renewal rates
- Enterprise pilots moving to production
- Government procurement
- Consumer search/social interest
- Installed base expansion

Interpretation:

- Demand acceleration can pressure upstream capacity.
- Demand slowdown can create oversupply, pricing pressure, and inventory risk.

### Supply signals

Look for:

- Capacity additions
- Factory utilization
- Lead times
- Inventory levels
- Supplier warnings
- Export restrictions
- Production bottlenecks
- Yield issues
- Dual-sourcing announcements

Interpretation:

- Tight supply + rising demand usually increases pricing power.
- New capacity + slowing demand can destroy margin.

### Capex signals

Look for:

- Data center buildouts
- Factory expansions
- Utility/grid investment
- Equipment orders
- Construction starts
- Capital intensity changes
- Capex guidance revisions

Interpretation:

- Capex flows often reveal where money is moving before revenue appears.

### Margin and pricing signals

Look for:

- Gross margin expansion/compression
- Price increases
- Discounts/promotions
- Input cost pass-through
- Commodity price changes
- Mix shift toward higher/lower margin products
- Utilization rates

Interpretation:

- Strong demand without pricing power may still be weak for investors.
- Margin expansion often indicates value capture.

### Regulation and policy signals

Look for:

- New rules
- Subsidies
- Tax credits
- Import/export controls
- Antitrust actions
- Safety approvals
- Procurement rules
- Permitting/interconnection changes

Interpretation:

- Regulation can create or destroy bottlenecks and moats.

### Technology signals

Look for:

- Performance breakthroughs
- Cost reductions
- Standards changes
- Open-source releases
- New architectures
- Reliability improvements
- Integration progress
- Patent clusters

Interpretation:

- Technology can remove one bottleneck while creating another.

### Hiring and labor signals

Look for:

- Hiring spikes in specialized roles
- Job postings for new product lines
- Geographic concentration of hiring
- Wage pressure
- Shortage of certified workers

Interpretation:

- Hiring is a weak signal, but useful for detecting where companies are investing.

### Funding and M&A signals

Look for:

- VC funding clusters
- Strategic investments
- Acquisitions
- IPO filings
- Debt financing
- Joint ventures
- Government-backed financing

Interpretation:

- Capital flow can validate a theme, but can also signal crowded trades.

### Customer pain signals

Look for:

- Complaints about cost, reliability, complexity, trust, compliance, integration, delays
- Enterprise adoption friction
- Churn reasons
- Procurement objections
- Security/safety failures

Interpretation:

- Customer pain often points to investable solution layers.

## Signal table format

Use this table in full reports:

| Signal | Category | Source/evidence | Direction | Affected nodes | Investment meaning | Confidence |
|---|---|---|---|---|---|---|

Direction values:

- Accelerating
- Decelerating
- Tightening
- Loosening
- Improving
- Worsening
- Unclear

## Signal-to-graph translation

Every signal should update the graph.

Examples:

- Rising data center capex → strengthens demand edges to power, cooling, networking, semiconductors
- Export control → increases geopolitical risk edge and supply constraint edge
- Job postings for compliance roles → possible regulatory/adoption bottleneck
- Falling commodity prices → margin relief for downstream nodes, pressure for upstream producers

## Weak-signal discipline

Weak signals are valuable but must be labeled.

Do not overstate:

- Job postings
- Social media buzz
- Patent counts
- Startup funding
- Anecdotal customer complaints

Use them to form watchlist theses, not high-confidence conclusions.

## Self-audit checklist for current signals

Before finalizing, check:

- Did the report extract signals across demand, supply, capex, pricing, regulation, technology, labor, funding, and customer pain where applicable?
- Did every major signal update at least one node, edge, bottleneck, or investment theme?
- Did the report distinguish acceleration from level? Example: large market vs market getting larger faster.
- Did the report avoid overreacting to isolated news?
- Did the report identify what to monitor next over the coming 30 days?
