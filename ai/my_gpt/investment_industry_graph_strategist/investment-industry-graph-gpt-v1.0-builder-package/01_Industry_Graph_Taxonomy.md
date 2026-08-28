# Industry Graph Taxonomy

Version: 1.0  
Use this file when building an upstream/downstream industry map, choosing nodes, defining edges, deciding expansion depth, or checking whether a graph is economically meaningful.

## Objective

The GPT must not create a loose “related industries” map. It must create a dependency graph where every node and edge has a reason to exist.

Good industry graph:

`final customer demand → downstream use cases → focal industry → enabling layers → suppliers → scarce inputs → economically material boundary conditions`

Bad industry graph:

`industry → random adjacent topics → famous companies → generic trends`

## Center node

The user’s chosen industry is the center node. If the input is broad, choose the most investment-relevant scope and state the assumption.

Examples:

| User input | Default scope assumption |
|---|---|
| AI | Global + US commercial AI value chain: infrastructure, model layer, application layer, enterprise/consumer/government demand |
| Energy | Ask a clarification unless the user accepts a broad split across oil/gas, power, renewables, nuclear, batteries, grid |
| Semiconductors | Split by design, EDA/IP, wafer fab, equipment, materials, packaging, memory, logic, end markets |
| Healthcare | Ask or split by payers, providers, pharma, medtech, services, digital health |

## Node types

Valid node types:

- Industry
- Sub-industry
- Product category
- Component
- Material
- Technology
- Infrastructure layer
- Process step
- Regulation/policy
- Customer segment
- Distribution channel
- Business model
- Capital source
- Company cluster
- Geographic chokepoint
- Data source or data asset
- Labor/talent constraint, only when material

## Company rule

Companies usually belong inside a node, not as primary graph nodes.

Use company nodes only when a company is itself a bottleneck, platform, gatekeeper, monopoly/oligopoly controller, standard setter, or unavoidable buyer/supplier.

Example:

- Good node: `High-bandwidth memory`
  - Companies inside: SK hynix, Samsung, Micron
- Possible company node: `ASML EUV lithography`, because ASML controls a unique bottleneck in advanced semiconductor manufacturing.

## Edge types

Every important edge must have a typed relationship.

| Edge type | Meaning |
|---|---|
| requires | Node A cannot operate or scale without Node B |
| supplies | Node A provides input to Node B |
| sells_to | Node A sells product/service to Node B |
| buys_from | Node A purchases from Node B |
| enables | Node A unlocks performance, adoption, scale, or cost reduction for Node B |
| constrains | Node A limits Node B’s growth, margin, speed, or adoption |
| substitutes | Node A can replace Node B |
| competes_with | Node A competes with Node B for demand, capital, supply, or budget |
| regulated_by | Node A is materially affected by Node B regulation/policy |
| funded_by | Node A depends on Node B capital source |
| bottleneck_for | Node A is a bottleneck for Node B |
| margin_flows_to | Economic value capture shifts from Node A to Node B |
| cost_driver_of | Node A is a major cost driver of Node B |
| capex_driver_of | Node A drives capital expenditure in Node B |
| demand_driver_of | Node A creates demand for Node B |
| risk_transmits_to | Risk in Node A propagates to Node B |

## Edge required fields

For each important edge, specify:

- Direction
- Edge type
- Strength: weak, medium, strong, critical
- Evidence or reasoning
- Money-flow relevance
- Confidence level

Example:

`AI inference demand → data center power`

- Type: demand_driver_of / requires
- Strength: critical
- Reason: inference workloads require sustained compute, which converts into power demand at data centers
- Money-flow relevance: increases capex and opex for power, cooling, grid interconnection, backup generation
- Confidence: high

## Graph layers

Use two graph layers.

### Core graph

Dependencies that are critical today.

Include nodes that:

- Are required for current production/adoption
- Control significant cost, supply, margin, or capacity
- Are already visible in financial statements, capex, pricing, or shortages

### Watchlist graph

Dependencies that are secondary today but may become critical within 1–5 years.

Include nodes that:

- Show early bottleneck signals
- Are small but scaling quickly
- Are exposed to new regulation
- Have technical constraints that may bind later
- Could become scarce if demand accelerates

## Upstream expansion rule

Continue upstream while a node is economically material.

Include upstream nodes when at least one is true:

- Influences 1%+ of total value-chain cost, or another clearly material share
- Affects 5%+ of growth capacity, timing, output, or adoption
- Creates shortage, delay, pricing power, or margin pressure
- Has investable public/private exposure
- Could become critical within 1–5 years
- Is a strategic chokepoint even if small today
- Is required for regulation, safety, trust, or adoption
- Creates asymmetric investor upside/downside

Stop upstream when:

- The node is too generic to produce investment insight
- It is not a bottleneck, margin pool, catalyst, or risk transmitter
- It does not materially affect demand, supply, pricing, capex, adoption, or regulation

Do not blindly expand to “labor → food → agriculture” unless labor is itself the industry bottleneck.

## Downstream completion rule

Every downstream path must end at a final customer.

Final customers include:

- Individual consumers
- Businesses
- Governments
- Hospitals
- Factories
- Utilities
- Banks
- Schools
- Developers
- Telecom operators
- Logistics operators
- Defense agencies
- Insurers
- Asset managers
- Other concrete buyers/users

Do not stop at an intermediate customer if that customer only passes value onward.

## Materiality labels

Use these labels for nodes:

- Critical today
- Important today
- Secondary today
- Watchlist
- Hidden/underpriced
- Boundary condition
- Excluded as non-material

## Common graph failure modes

Avoid:

- Listing famous companies without explaining node economics
- Mapping buzzwords instead of dependencies
- Stopping downstream before final customers
- Treating technical importance as equal to value capture
- Ignoring regulation, capital, energy, or infrastructure
- Missing substitute technologies
- Missing customer budget owners
- Expanding upstream forever into generic inputs

## Self-audit checklist for graph quality

Before finalizing a full report, check:

- Did every major downstream path end at a concrete final customer?
- Did the graph include both core dependencies and watchlist dependencies?
- Did the graph distinguish companies from industry/product nodes?
- Did every critical edge explain why the relationship exists?
- Did the graph include non-obvious constraint layers such as energy, regulation, infrastructure, capital, data, trust, or labor when material?
- Did upstream expansion stop for a defensible materiality reason?
- Are any important substitute technologies or alternative business models missing?

If any answer is no, repair the graph before presenting the final report.
