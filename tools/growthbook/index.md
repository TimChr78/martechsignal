# GrowthBook review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Starter free (3 users), Pro $40/seat/mo (30 users) published with Enterprise custom and managed warehouse event caps listed (tools.json, verified 2026-09-28). |
| Feature depth | 7/10 | Feature flags, A/B testing, a visual editor and contextual bandits cover the experimentation stack (tools.json ai_features). |
| Integrations | 6/10 | Snowflake, BigQuery, Databricks, ClickHouse, Trino and Slack documented plus an API (tools.json). |
| AI capability | 6/10 | AI assistant, AI Visual Editor and MCP servers for Claude, Cursor and VS Code with contextual bandits (tools.json ai_features). |
| Openness | 9/10 | MIT-licensed with 8.4k GitHub stars and free self-hosting (tools.json). |
| Operational maturity | 6/10 | Founded 2020 with a commercial entity behind the open core (tools.json). |


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; Starter caps the account at 3 users and 1 project, so growth past a small team means Pro at USD 40 per seat. |
| &#10003; AI capabilities: growthBook AI assistant (usage-metered per plan) | &#10007; The AI Visual Editor, bandits, and split URL tests sit on paid plans only. |
| &#10003; Established community (8,430 GitHub stars) | &#10007; Three enterprise directories carry a separate GrowthBook Enterprise License on top of the MIT core. |
| &#10003; Native integrations include Snowflake, BigQuery, Databricks (6 listed) |  |
| &#10003; Unlimited flags, experiments, and traffic on every plan, including the free one. |  |
| &#10003; The MCP server is hosted and OAuth-based, so AI tooling works without provisioning API keys. |  |
| &#10003; Cloud and self-hosted are both documented deployment paths, and the warehouse stays on your infrastructure either way. |  |

**What is GrowthBook?**
Open-source feature flags and A/B testing with a visual editor and attribute-based targeting. It ships with growthBook AI assistant (usage-metered per plan), 8,430 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does GrowthBook cost?**
GrowthBook is open source - MIT licensed and free to self-host; the public repository carries 8,430 stars; native integrations cover Snowflake, BigQuery, Databricks. You pay in server time and maintenance, not licences.

**Is GrowthBook worth it past the free tier?**
The warehouse-native choice for teams that want experimentation math they can audit and feature flags in the same tool. Both the price and the licence are legible.

**What licence is GrowthBook under?**
MIT for most of the repository. Three directories (packages/back-end/src/enterprise, packages/front-end/enterprise, and packages/shared/src/enterprise) are under a separate GrowthBook Enterprise License, which is why GitHub reports the overall licence as unclassified.

**Does GrowthBook work without a data warehouse?**
Yes. The managed warehouse option covers teams without one on cloud plans, and the self-hosted path lets you run the whole stack yourself.

- **Pricing:** Freemium
- **Category:** [Personalization &amp; CDP](/categories/personalization/)
- **GitHub:** ★ 8430
- **Founded:** 2020
- **API:** Yes
- **Last verified:** 2026-09-25

**Verdict:** GrowthBook is a tool in Personalization &amp; CDP with free and open source. The catalog documents 4 AI features, 6 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

Flagsmith

Open-source feature flag and remote config platform with segment targeting

Jitsu

Open-source Segment alternative for event capture and warehouse-first data pipelines

ToolJet

Open-source low-code platform for internal tools: prompt or build admin panels, dashboards and operational apps

Mixpanel

Product analytics platform with AI-powered insights for user behavior tracking

[More Personalization &amp; CDP Tools →](/categories/personalization/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Personalization &amp; CDP](/categories/personalization/)
- GrowthBook
## GrowthBook review (2026): pricing, AI features, verdict

Open-source feature flags and A/B testing with a visual editor and attribute-based targeting

Personalization &amp; CDP · Freemium · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-25

[Visit GrowthBook &#8594;](https://www.growthbook.io)

[How we review](/methodology/) · No affiliate links

[Visit GrowthBook &#8594;](https://www.growthbook.io)

## MartechSignal Score: 42/60

GrowthBook is the open-source experiment stack with warehouse-native stats and an AI assistant metered by plan. MIT licensing and 8.4k stars say the community believes in it.

Scored 2026-09-26 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

GrowthBook is an open-source feature flag and A/B testing platform with 8,430 GitHub stars, built warehouse-native: experiments are analyzed in your own data warehouse instead of a vendor copy of your events. Flags support attribute-based targeting and gradual rollouts, and every cloud plan includes unlimited flags, experiments, and traffic. The statistics engine runs frequentist and Bayesian analysis, and Pro adds multi-arm bandits, split URL tests, a power calculator, and customizable dashboards. Cloud pricing starts at zero. Starter is free for up to 3 users and 1 project. Pro runs USD 40 per seat per month for up to 30 users and 3 projects. Enterprise is custom and adds ramp schedules, approval workflows, SSO and SCIM, exportable audit logs, and a 99.99% uptime SLA. A managed warehouse is available for teams without their own: 1 million events a month on Starter, 2 million on Pro and then USD 30 per million. Supported warehouses include Snowflake, BigQuery, Databricks, ClickHouse, Trino, and Adobe Experience Platform Query Service. The AI surface is real and dated. A hosted MCP server at mcp.growthbook.io connects to Claude, Cursor, and VS Code over OAuth so agents can create flags and read experiment results. The AI Visual Editor is a Pro feature, GrowthBook AI usage is metered per plan, and Enterprise can bring its own LLM provider. Version 5.1 added a Slack app and contextual bandits. Self-hosting is documented alongside cloud. The repository is MIT licensed except for three enterprise directories under a separate GrowthBook Enterprise License. The company was founded in 2020 by Graham McNicoll and Jeremy Dorn.

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

GrowthBook is freemium, with a free tier to start.

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

## Related concepts

- [Personalization](/glossary/personalization/)
- [CRO](/glossary/cro/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source feature flags and A/B testing with a visual editor and attribute-based targeting. It ships with growthBook AI assistant (usage-metered per plan), 8,430 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

GrowthBook is open source - MIT licensed and free to self-host; the public repository carries 8,430 stars; native integrations cover Snowflake, BigQuery, Databricks. You pay in server time and maintenance, not licences.

The warehouse-native choice for teams that want experimentation math they can audit and feature flags in the same tool. Both the price and the licence are legible.

MIT for most of the repository. Three directories (packages/back-end/src/enterprise, packages/front-end/enterprise, and packages/shared/src/enterprise) are under a separate GrowthBook Enterprise License, which is why GitHub reports the overall licence as unclassified.

Yes. The managed warehouse option covers teams without one on cloud plans, and the self-hosted path lets you run the whole stack yourself.

## Similar Tools

## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [Multi-Touch Attribution Was Always a Fiction](/blog/multi-touch-attribution-was-always-a-fiction/)
- [Claude SEO benchmark: every score we have earned, and what each one measured](/blog/claude-seo-benchmark/)
### Quick Facts

Related guides: [Ai Personalization Tools](/best/ai-personalization-tools)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/growthbook/#app",
    "name": "GrowthBook",
    "description": "Open-source feature flags and A/B testing with a visual editor and attribute-based targeting",
    "image": "https://martechsignal.com/og/tools/growthbook.png",
    "url": "https://martechsignal.com/tools/growthbook/",
    "sameAs": [
      "https://www.growthbook.io"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/growthbook/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-25",
    "datePublished": "2026-09-25",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://www.growthbook.io/pricing",
      "priceValidUntil": "2026-12-31"
    }
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://martechsignal.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Tools",
        "item": "https://martechsignal.com/tools/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Personalization & CDP",
        "item": "https://martechsignal.com/categories/personalization/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "GrowthBook",
        "item": "https://martechsignal.com/tools/growthbook/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is GrowthBook?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source feature flags and A/B testing with a visual editor and attribute-based targeting. It ships with growthBook AI assistant (usage-metered per plan), 8,430 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does GrowthBook cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "GrowthBook is open source - MIT licensed and free to self-host; the public repository carries 8,430 stars; native integrations cover Snowflake, BigQuery, Databricks. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is GrowthBook worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The warehouse-native choice for teams that want experimentation math they can audit and feature flags in the same tool. Both the price and the licence are legible."
        }
      },
      {
        "@type": "Question",
        "name": "What licence is GrowthBook under?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "MIT for most of the repository. Three directories (packages/back-end/src/enterprise, packages/front-end/enterprise, and packages/shared/src/enterprise) are under a separate GrowthBook Enterprise License, which is why GitHub reports the overall licence as unclassified."
        }
      },
      {
        "@type": "Question",
        "name": "Does GrowthBook work without a data warehouse?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. The managed warehouse option covers teams without one on cloud plans, and the self-hosted path lets you run the whole stack yourself."
        }
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "Review",
    "author": {
      "@type": "Person",
      "name": "Tim Christensen",
      "url": "https://martechsignal.com/authors/tim-christensen/",
      "@id": "https://martechsignal.com/authors/tim-christensen/#person"
    },
    "publisher": {
      "@type": "Organization",
      "@id": "https://martechsignal.com/#organization",
      "name": "MartechSignal"
    },
    "datePublished": "2026-09-26",
    "reviewBody": "GrowthBook is the open-source experiment stack with warehouse-native stats and an AI assistant metered by plan. MIT licensing and 8.4k stars say the community believes in it.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/growthbook/#app",
      "name": "GrowthBook",
      "url": "https://martechsignal.com/tools/growthbook/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 42,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
