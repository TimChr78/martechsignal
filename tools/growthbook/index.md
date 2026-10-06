# GrowthBook review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Personalization & CDP](/categories/personalization/)
- GrowthBook
## GrowthBook review (2026): pricing, AI features, verdict

Open-source feature flags and A/B testing with a visual editor and attribute-based targeting

Personalization & CDP · Freemium from $40/seat/mo · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit GrowthBook →](https://www.growthbook.io)

[How we review](/methodology/) · No affiliate links

**Verdict:** GrowthBook is a tool in Personalization & CDP with free and open source. The catalog documents 4 AI features, 6 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

[Visit GrowthBook →](https://www.growthbook.io)

## MartechSignal Score: 42/60

GrowthBook is the open-source experiment stack with warehouse-native stats and an AI assistant metered by plan. MIT licensing and 8,474 stars say the community believes in it.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Starter free (3 users), Pro $40/seat/mo (30 users) published with Enterprise custom and managed warehouse event caps listed (the vendor pricing page: [pricing page](https://www.growthbook.io/pricing), verified 2026-09-25). |
| Feature depth | 7/10 | Feature flags, A/B testing, a visual editor and contextual bandits cover the experimentation stack (vendor documentation: [vendor site](https://www.growthbook.io), verified 2026-09-28). |
| Integrations | 6/10 | Snowflake, BigQuery, Databricks, ClickHouse, Trino and Slack documented plus an API (vendor documentation: [vendor site](https://www.growthbook.io), verified 2026-09-28). |
| AI capability | 6/10 | AI assistant, AI Visual Editor and MCP servers for Claude, Cursor and VS Code with contextual bandits (vendor documentation: [vendor site](https://www.growthbook.io), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with free self-hosting (the source repository: [repository](https://github.com/growthbook/growthbook), verified 2026-09-28). |
| Operational maturity | 6/10 | Founded 2020 with a commercial entity behind the open core (vendor documentation: [vendor site](https://www.growthbook.io), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

GrowthBook is an open-source feature flag and A/B testing platform with 8,474 GitHub stars, built warehouse-native: experiments are analyzed in your own data warehouse instead of a vendor copy of your events. Flags support attribute-based targeting and gradual rollouts, and every cloud plan includes unlimited flags, experiments, and traffic. The statistics engine runs frequentist and Bayesian analysis, and Pro adds multi-arm bandits, split URL tests, a power calculator, and customizable dashboards. Cloud pricing starts at zero. Starter is free for up to 3 users and 1 project. Pro runs USD 40 per seat per month for up to 30 users and 3 projects. Enterprise is custom and adds ramp schedules, approval workflows, SSO and SCIM, exportable audit logs, and a 99.99% uptime SLA. A managed warehouse is available for teams without their own: 1 million events a month on Starter, 2 million on Pro and then USD 30 per million. Supported warehouses include Snowflake, BigQuery, Databricks, ClickHouse, Trino, and Adobe Experience Platform Query Service. The AI surface is real and dated. A hosted MCP server at mcp.growthbook.io connects to Claude, Cursor, and VS Code over OAuth so agents can create flags and read experiment results. The AI Visual Editor is a Pro feature, GrowthBook AI usage is metered per plan, and Enterprise can bring its own LLM provider. Version 5.1 added a Slack app and contextual bandits. Self-hosting is documented alongside cloud. The repository is MIT licensed except for three enterprise directories under a separate GrowthBook Enterprise License. The company was founded in 2020 by Graham McNicoll and Jeremy Dorn.

## AI Capabilities

- GrowthBook AI assistant (usage-metered per plan)
- AI Visual Editor (Pro and up)
- MCP Server for Claude, Cursor, and VS Code
- Contextual bandits (Enterprise)
## Key Integrations

- Snowflake
- BigQuery
- Databricks
- ClickHouse
- Trino
- Slack
## Pricing

GrowthBook is freemium, with a free tier to start, paid plans start at $40/seat/mo as of 2026-09.

Starter free (3 users, 1 project). Pro USD 40/seat/month (30 users, 3 projects). Enterprise custom. Managed warehouse: 1M events/mo on Starter, 2M on Pro then USD 30 per additional million.

Current plans and limits live on the [GrowthBook pricing page](https://www.growthbook.io/pricing).

## Best for

Product and data teams running A/B tests against their own warehouse who also want feature flags, with a free tier that carries a small team.

## Not for

Teams shopping for a full product analytics suite or marketing automation, and buyers who need every feature under a pure open-source licence: the enterprise directories are separately licensed.

## Review notes

Assessed from growthbook.io, docs.growthbook.io, the pricing page, and the repository in September 2026, without a live deployment. The product treats the data warehouse as the source of truth: Snowflake, BigQuery, Databricks, ClickHouse, Trino, and Adobe Experience Platform Query Service are supported, and a managed warehouse is offered for teams that do not have one.

The plan lines are clear and worth reading closely. Starter is free for three users and one project with unlimited flags, experiments, and traffic. Pro at USD 40 per seat a month adds the AI Visual Editor, multi-arm bandits, split URL tests, safe rollouts, and a power calculator. Enterprise adds contextual bandits, ramp schedules, approval workflows, SSO and SCIM, and audit log export. The managed warehouse allowance is 1 million events a month on Starter, 2 million on Pro and then USD 30 per million.

The AI work goes further than in most flag tools. The hosted MCP server connects to Claude, Cursor, and VS Code over OAuth with no API key and lets agents create flags and query experiment results. GrowthBook AI usage is metered per plan, and Enterprise can point it at its own LLM provider. One detail to note in procurement: the code is MIT except for three enterprise directories that carry a separate GrowthBook Enterprise License.

## Verdict

The warehouse-native choice for teams that want experimentation math they can audit and feature flags in the same tool. Both the price and the licence are legible.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Paid plans start at $40/seat/mo once past the free tier |
| ✓ AI capabilities: growthBook AI assistant (usage-metered per plan) | ✗ Starter caps the account at 3 users and 1 project, so growth past a small team means Pro at USD 40 per seat. |
| ✓ Active public repository (8,474 GitHub stars counted at last check) | ✗ The AI Visual Editor, bandits, and split URL tests sit on paid plans only. |
| ✓ Native integrations include Snowflake, BigQuery, Databricks (6 listed) | ✗ Three enterprise directories carry a separate GrowthBook Enterprise License on top of the MIT core. |
| ✓ Unlimited flags, experiments, and traffic on every plan, including the free one. |  |
| ✓ The MCP server is hosted and OAuth-based, so AI tooling works without provisioning API keys. |  |
| ✓ Cloud and self-hosted are both documented deployment paths, and the warehouse stays on your infrastructure either way. |  |

## Related concepts

- [Personalization](/glossary/personalization/)
- [CRO](/glossary/cro/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is GrowthBook?**
GrowthBook: Open-source feature flags and A/B testing with a visual editor and attribute-based targeting. GrowthBook ships with growthBook AI assistant (usage-metered per plan). The public repository carries 8,474 stars.

**How much does GrowthBook cost?**
GrowthBook has a free tier; paid plans start at $40/seat/mo. Starter free (3 users, 1 project). Pro USD 40/seat/month (30 users, 3 projects). Enterprise custom. Managed warehouse: 1M events/mo on Starter, 2M on Pro then USD 30 per additional million. We last checked both ends of that split on 2026-09-25. The pricing section above shows what the free tier actually covers.

**Is GrowthBook worth it past the free tier?**
The warehouse-native choice for teams that want experimentation math they can audit and feature flags in the same tool. Both the price and the licence are legible.

**What licence is GrowthBook under?**
MIT for most of the repository. Three directories (packages/back-end/src/enterprise, packages/front-end/enterprise, and packages/shared/src/enterprise) are under a separate GrowthBook Enterprise License, which is why GitHub reports the overall licence as unclassified.

**Does GrowthBook work without a data warehouse?**
Yes. The managed warehouse option covers teams without one on cloud plans, and the self-hosted path lets you run the whole stack yourself.

## Similar Tools

- [Flagsmith](/tools/flagsmith/): Open-source feature flag and remote config platform with segment targeting
- [Jitsu](/tools/jitsu/): Open-source Segment alternative for event capture and warehouse-first data pipelines
- [RudderStack](/tools/rudderstack/): Warehouse-first CDP: open-source Go data plane plus managed routing
- [ToolJet](/tools/tooljet/): Open-source low-code platform for internal tools: prompt or build admin panels, dashboards and operational apps
## Related reading

- [The fully open-source agentic marketing stack you can run today: 19 MCP servers, one agent](/blog/open-source-agentic-martech-stack-mcp/)
- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
- [Where open-source martech momentum actually lives](/blog/oss-momentum-tracker-september-2026/)
## Also featured in

- [Best AI Personalization & CDP tools (2026): 8 compared](/best/ai-personalization-tools/) — Best for product teams that want feature flags and A/B testing they can self-host, with a free Starter plan for 3 users.
### Quick Facts

- **Pricing:** Freemium from $40/seat/mo
- **Category:** [Personalization & CDP](/categories/personalization/)
- **GitHub:** ★ 8474
- **Founded:** 2020
- **API:** Yes
- **Repository checked:** 2026-10-05
- **Page updated:** 2026-09-25

Related guides: [Ai Personalization Tools](/best/ai-personalization-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Personalization & CDP Tools →](/categories/personalization/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
