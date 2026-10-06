# Best Customer Data Platforms (2026): composable to self-hosted

## Best Customer Data Platforms (2026): composable to self-hosted

RudderStack fits warehouse-first teams that want a self-hostable event router with a free 250K events/mo tier. Hightouch activates data already in the warehouse with no event collection of its own. Jitsu is the fully open-source option. Apache Unomi suits consent- and residency-governed European stacks. Segment is the documented default at a price, Tealium the enterprise governance play.


| Tool | Pricing | Open source | Best for |
| --- | --- | --- | --- |
| [RudderStack](/tools/rudderstack/) | Open-core from $265/mo | Source-available (fair-code) | Best Segment-compatible router for warehouse-first stacks on a budget. |
| [Hightouch](/tools/hightouch/) | Freemium | No | Best activation layer when the warehouse is already the source of truth. |
| [Jitsu](/tools/jitsu/) | Freemium from $99/mo | Yes (MIT) | Best fully open-source event collection for self-hosting the pipeline. |
| [Apache Unomi](/tools/apache-unomi/) | Open Source | Yes (Apache-2.0) | Best when data-residency rules and European-consent governance drive the architecture. |
| [Twilio Segment](/tools/segment/) | Freemium from $120/mo | No | Best documented default when budget is not the deciding axis. |
| [Tealium](/tools/tealium/) | Enterprise | No | Best enterprise governance and consent orchestration at large scale. |

**Our top pick: [RudderStack](#rudderstack)** — Best Segment-compatible router for warehouse-first stacks on a budget. [Try RudderStack](https://www.rudderstack.com/)

Last verified 2026-10-01.

## How we picked

A customer data platform solves one problem: events arrive from an app, and a coherent profile has to come out where the campaigns run. The 2026 market splits cleanly along one axis - does the tool store the profile itself (classic CDPs like Segment and Tealium), or does it only route warehouse data and leave storage to Snowflake or BigQuery (composable CDPs like Hightouch, and event routers like RudderStack or Jitsu)?

This list draws only from tools already in the catalog, each with verified pricing on its own page and, where open source, a live GitHub snapshot. It is desk research against vendor documentation and receipts, not a hands-on bake-off. Pricing figures are the catalog's last verified numbers, dated on each tool page.

Cuts to start from: cheapest Segment-compatible router is RudderStack (free 250K events/mo, self-hostable data plane). Activation-only over an existing warehouse is Hightouch (free for 2 active syncs). Fully self-hosted and open-source routes are Jitsu (event router) and Apache Unomi (rules-based profile store). The documented classic profile CDP is Segment. Enterprise tag-and-hub governance is Tealium.

## What we checked and when

Pricing checked 2026-09-28 against each vendor's own pricing page · API availability confirmed from public documentation · Integrations read from vendor listings and source repositories. Not installed and not benchmarked: this is desk research with dates on it.

What we could not verify is called out under each tool below.

## Browse the hubs behind these picks

- [Open-Source Tools](/categories/open-source/)
- [Personalization & CDP](/categories/personalization/)
## Key terms

- [Marketing ops](/glossary/marketing-ops/)
- [Workflow automation](/glossary/workflow-automation/)
- [Personalization](/glossary/personalization/)
- [CRO](/glossary/cro/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

## Open-source momentum, with receipts

Star counts we snapshot ourselves every morning - check any of them against GitHub in one click.

- Jitsu - 5,099 stars, +8 in the 10-snapshot window to 2026-10-05 5,091→5,099 [verify on GitHub](https://github.com/jitsucom/jitsu)
- Apache Unomi - 375 stars, +0 in the 10-snapshot window to 2026-10-05 375→375 [verify on GitHub](https://github.com/apache/unomi)
[All movers on the trending page](/trending/).

## [RudderStack](/tools/rudderstack/)

RudderStack plays the budget Segment-shaped router. Events route into warehouses and cloud destinations with reverse ETL back out. The free plan allows 250K events/mo, and Growth starts at $265/mo. The trade is that the self-hostable plane leaves profile storage to your warehouse.

**Verdict:** Best Segment-compatible router for warehouse-first stacks on a budget.

Vendor: [Official site](https://www.rudderstack.com/) · [Pricing](https://www.rudderstack.com/pricing/) · [GitHub](https://github.com/rudderlabs/rudder-server)

**Skip it if you want a managed profile store with identity resolution out of the box - the OSS data plane leaves that to your warehouse.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Hightouch](/tools/hightouch/)

Hightouch stays warehouse-only with nothing to collect events itself. Syncs run from a warehouse you already operate. The free plan allows 2 active syncs/mo, and entry deployments run around $1,000+/mo. That rules Hightouch out for any team without one.

**Verdict:** Best activation layer when the warehouse is already the source of truth.

Vendor: [Official site](https://hightouch.com/) · [Pricing](https://hightouch.com/pricing)

**Skip it if the company has no modern data warehouse - there is nothing for it to sync from.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Jitsu](/tools/jitsu/)

Jitsu brings fully open-source collection under MIT with a Segment-compatible API. Existing SDK code keeps working. The free plan allows 200K active events/mo, Business is $99/mo, extra volume is $40 per additional 1M, and extra syncs are $20 each. The trade is a smaller destination set and thinner managed identity against Segment.

**Verdict:** Best fully open-source event collection for self-hosting the pipeline.

Vendor: [Official site](https://jitsu.com) · [Pricing](https://jitsu.com/pricing) · [GitHub](https://github.com/jitsucom/jitsu)

**Skip it if managed identity graphs and a large destination catalog are day-one requirements.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Apache Unomi](/tools/apache-unomi/)

Apache Unomi supplies governance plumbing for consent handling and data residency. The project is free self-hosted Apache with no commercial cloud tier. The trade is heavier operations and a plain UI against the routers here.

**Verdict:** Best when data-residency rules and European-consent governance drive the architecture.

Vendor: [Official site](https://unomi.apache.org) · [GitHub](https://github.com/apache/unomi)

**Skip it if you need a modern UI, SDK breadth, or quick time-to-value - Unomi is plumbing, not product.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Twilio Segment](/tools/segment/)

Twilio Segment remains the documented default with catalog breadth and docs leading the group. The free plan covers 1,000 MTUs and 2 sources, Team starts at $120/mo for 10,000 MTUs, and overages run $10 to $12 per extra 1,000 MTUs. The trade is volume pricing scaling faster than the warehouse-first and open-source options here.

**Verdict:** Best documented default when budget is not the deciding axis.

Vendor: [Official site](https://segment.com) · [Pricing](https://www.twilio.com/en-us/pricing/customer-data)

**Skip it if event volume pricing at scale outruns the budget; warehouse-first or open-source stacks start cheaper.**

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

## [Tealium](/tools/tealium/)

Tealium enforces enterprise control through tag management plus consent orchestration and audit trails. Pricing is enterprise custom on annual contracts. The trade suits large-scale teams and blocks smaller buyers.

**Verdict:** Best enterprise governance and consent orchestration at large scale.

Vendor: [Official site](https://tealium.com) · [Pricing](https://tealium.com/pricing/)

**What we could not verify:** installed behaviour, support quality and limits under real load. A hands-on pass would settle them; we have not run one.

Every price quoted here comes from the vendor's own pricing page as catalogued on the tool page. Browse [all 166 tools](/tools/) or read [how we evaluate](/methodology/), or download the [machine-readable catalog](/catalog-tools.json).

## What is the difference between a classic and a composable CDP?

A classic CDP (Segment, Tealium) collects events itself and owns the profile store. A composable CDP (Hightouch) leaves collection and storage to the warehouse you already have and only routes data out to tools. RudderStack straddles both: it can collect events and push them to your warehouse.

## Which one can we self-host completely?

Jitsu (MIT, event routing plus light profiles) and Apache Unomi (ASF, rules-based profile store). RudderStack self-hosts the data plane while the control plane runs in the cloud.

## Which one is cheapest to start?

RudderStack's 250K-events free tier and Hightouch's 2-sync free plan are both $0. Segment's free tier stops at 1,000 monthly tracked users, then Team pricing starts at $120/mo.

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
