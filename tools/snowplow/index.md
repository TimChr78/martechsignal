# Snowplow review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 5/10 | The open-source pipeline is free to self-host and clearly stated; BDP Cloud is quoted by sales (verified Sep 2026). |
| Feature depth | 7/10 | Event pipelines to six warehouse/lake formats plus real-time profiles with propensity and intent signals (vendor documentation). |
| Integrations | 8/10 | Snowflake, Databricks, BigQuery, Redshift, Delta Lake, Iceberg, Kafka, Kinesis and Pub/Sub documented (vendor documentation). |
| AI capability | 6/10 | Signals propensity predictions, intent detection and agentic context for AI agents make it model-ready plumbing (vendor documentation). |
| Openness | 9/10 | Apache-2.0 self-hosted pipeline with 7.0k GitHub stars and warehouse-first design (the source repository). |
| Operational maturity | 7/10 | Founded 2012 with a commercial cloud arm and long enterprise deployments (vendor documentation). |


| Pros | Cons |
| --- | --- |
| &#10003; Apache-2.0 licence with free self-hosting | &#10007; No hands-on test - this assessment is based on vendor documentation and the public repository |
| &#10003; AI capabilities: signals real-time profiles with propensity predictions |  |
| &#10003; Established community (7,031 GitHub stars) |  |
| &#10003; Native integrations include Snowflake, Databricks, BigQuery (9 listed) |  |

**What is Snowplow?**
Customer context infrastructure: behavioral event pipeline for warehouses and AI agents. It ships with signals real-time profiles with propensity predictions, 7,031 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Snowplow cost?**
Snowplow is open source - Apache-2.0 licensed and free to self-host; the public repository carries 7,031 stars; native integrations cover Snowflake, Databricks, BigQuery. You pay in server time and maintenance, not licences.

**Is Snowplow a good self-hosted Analytics &amp; Attribution tool in 2026?**
The deepest behavioral-event infrastructure for teams that own their data pipeline, now priced and licensed like enterprise software rather than the free open-source project it once was.

**Is Snowplow still open source?**
Partly, and the details matter. The GitHub repo badge says Apache-2.0, but the README states that since January 8, 2024, new core pipeline releases ship under the Snowplow Limited Use License Agreement v1.1, which restricts commercial use, and the self-hosted docs say the community edition is for testing and evaluation and must not be deployed in production. Components released before 2024 keep Apache terms but get no security patches. The JavaScript tracker remains BSD-3-Clause, as are some client libraries. In practical terms: you can still inspect everything and self-host for evaluation, but production self-hosting requires a paid plan, which is why the pricing page lists a Self-Hosted Pipeline option described as removing the non-commercial restriction.

**What is Snowplow Signals?**
Signals, launched in May 2025, is Snowplow&#x27;s real-time context layer and the home of its AI-facing features. It combines a profiles store serving customer context with a published sub-10-millisecond p95 API claim, an interventions engine that triggers on rules or machine learning, and propensity predictions for conversion, churn, and lifetime value. It also exposes agentic context, meaning AI agents can read customer state at runtime through Python and Node SDKs. It sits downstream of the event pipeline: behavioral events feed profiles, profiles feed interventions and agents. If you are not building real-time personalization or agent-driven experiences, Signals is the part of the platform you can ignore.

- **Pricing:** Free tier
- **Category:** [Analytics &amp; Attribution](/categories/analytics/)
- **GitHub:** ★ 7031
- **Founded:** 2012
- **API:** Yes
- **Last verified:** 2026-09-25

**Verdict:** Snowplow is a tool in Analytics &amp; Attribution with free and open source. The catalog documents 3 AI features, 9 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

Mixpanel

Product analytics platform with AI-powered insights for user behavior tracking

Tealium

Enterprise customer data platform with real-time data orchestration and AI

Amplitude

AI-powered digital analytics platform for product and marketing teams

Twilio Segment

Customer data platform for collecting, unifying, and activating customer data

Attribution

AI-powered marketing attribution platform connecting ad spend to revenue

[More Analytics &amp; Attribution Tools →](/categories/analytics/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Analytics &amp; Attribution](/categories/analytics/)
- Snowplow
## Snowplow review (2026): pricing, AI features, verdict

Customer context infrastructure: behavioral event pipeline for warehouses and AI agents

Analytics &amp; Attribution · Free tier · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-25

[Visit Snowplow &#8594;](https://snowplow.io)

[How we review](/methodology/) · No affiliate links

[Visit Snowplow &#8594;](https://snowplow.io)

## MartechSignal Score: 42/60

Snowplow is behavioral data infrastructure you can own: the pipeline is Apache-2.0 and the cloud is a quote. If an event schema matters more than a dashboard, this is the right layer.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Snowplow is behavioral event infrastructure that has repositioned itself for the AI era: the company now calls its product a Customer Context Layer that turns raw behavioral data into real-time context for AI agents and analytics, delivered to your warehouse, lake, or stream. Founded in 2012 by Alex Dean and Yali Sassoon, it names Strava, HelloFresh, Auto Trader, and Burberry among its customers. The tracking model is the enduring core: trackers send events that are validated against self-describing JSON schemas, with vendor, name, and version carried in an iglu: reference, invalid events routed out rather than silently accepted, and Iglu acting as the schema registry. Eighteen documented enrichments cover campaign attribution, bot detection, user-agent parsing, IP anonymization, PII pseudonymization, and currency conversion, and destinations include Snowflake, Databricks, BigQuery, Redshift, Delta Lake, and Apache Iceberg, plus Kafka, Kinesis, and Pub/Sub streams. Snowplow Console manages the pipeline, Snowplow Mini provides single-instance testing, and Event Studio and data model packs round out the tooling. Signals, launched in May 2025, is the AI-facing layer: a profiles store with a sub-10-millisecond API claim, an interventions engine driven by rules or machine learning, conversion, churn, and lifetime-value propensity predictions, and agentic context exposed through Python and Node SDKs. One licensing change matters more than any feature: since January 8, 2024, new core pipeline releases ship under the Snowplow Limited Use License Agreement, and the documentation states the community edition is for testing and evaluation and must not be deployed in production; the paid Self-Hosted Pipeline plan exists specifically to remove that restriction. Components still release actively (enrich 6.13.1 in August 2026, the BSD-3 JavaScript tracker at 4.10.1). Pricing has no published figures: a 14-day full trial with no credit card, then quote-based managed and self-hosted plans priced on event volume and destinations.

Snowplow homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Signals real-time profiles with propensity predictions
- Intent detection
- Agentic context for AI agents
## Key Integrations

- Snowflake
- Databricks
- BigQuery
- Redshift
- Delta Lake
- Apache Iceberg
- Kafka
- Kinesis
- Google Pub/Sub
## Pricing

Snowplow is open core: the self-hosted version is free.

The open-source pipeline is free to self-host. Snowplow BDP Cloud is quoted by sales (verified Sep 2026).

## How to install

- Managed path: start the 14-day free trial from snowplow.io/pricing; the page states no credit card and no sales call are required to start.
- Local testing: run Snowplow Micro, a lightweight pipeline in a Docker image (snowplow/snowplow-micro) that receives, validates, and enriches events with a UI at localhost:9090/micro/ui; the docs state it is not designed for production traffic.
- Self-hosted path is Terraform, not docker compose: sign up for the Community Edition, then terraform init, plan, and apply for the Iglu server followed by the pipeline, with reference architectures for AWS Kinesis to Redshift, Snowflake, or Databricks, GCP Pub/Sub to BigQuery, and Azure Event Hubs to ADLS.
- Instrumentation starts with a tracker; the JavaScript tracker (BSD-3-Clause, v4.10.1) is the common entry point, and Snowtype generates typed tracking code from your schemas.
- Validate early: events that fail schema validation are routed to a failed-events path rather than dropped silently, so wiring that monitoring in on day one is the documented pattern.
## Requirements

Self-hosting means Terraform plus a cloud message queue (Kinesis, Pub/Sub, or Event Hubs) and a warehouse or lake destination, operated by your team. Micro needs only Docker. The managed platform removes the pipeline operations entirely; the community edition&#x27;s SLULA 1.1 terms forbid production deployment, so plan licensing before you build.

## Best for

Organizations with data engineering capacity that want event-level behavioral data they own in their own warehouse, schema-governed and enrichment-rich, and that are building personalization, propensity modeling, or AI agents on top of a real-time context layer.

## Not for

Teams wanting a dashboard-first product analytics tool (Snowplow models data, it does not hand you product dashboards), and anyone expecting the free open-source pipeline of earlier years: production self-hosting now requires a paid plan under SLULA 1.1, and small teams without pipeline operations experience will feel the weight.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from snowplow.io, docs.snowplow.io, the pricing page, and the component repos. Not a hands-on review. The scale signals are consistent across sources: 7,000-plus stars on the umbrella repo, named customers including Strava and Burberry, and components shipping point releases in August 2026.

The correction that matters against our earlier record: Snowplow is no longer free open source for production use. Since January 8, 2024, new core pipeline releases ship under the Snowplow Limited Use License Agreement v1.1, and the self-hosted quick start states the community edition must not be deployed in production; the paid Self-Hosted Pipeline plan is described as removing the non-commercial restriction. Our record previously said open-source self-hosted free, and the repo&#x27;s Apache-2.0 badge obscures the README&#x27;s licensing note. The JavaScript tracker remains BSD-3-Clause, and pre-2024 versions still carry Apache terms but receive no security patches.

The product surface has widened beyond the pipeline: Snowplow Signals (May 2025) adds real-time profiles, an interventions engine with rules or ML triggers, and propensity predictions exposed through Python and Node SDKs, and the site now leads with agentic context for AI. Data-model packs, event studio, and identities round out the managed platform. None of this changes the fundamental shape: you design schemas, own the event stream, and build models downstream.

The eighteen documented enrichments are the quiet differentiator versus SaaS SDKs: campaign attribution, referrer and UA parsing, bot detection, IP lookup and anonymization, PII pseudonymization, currency conversion, and API or SQL enrichment. Everything is schema-validated before storage, which is why failed-event monitoring is a first-class concern in the docs.

## Verdict

The deepest behavioral-event infrastructure for teams that own their data pipeline, now priced and licensed like enterprise software rather than the free open-source project it once was.

## Pros and cons

## Related concepts

- [Attribution models](/glossary/marketing-attribution-models/)
- [First-party data](/glossary/first-party-data/)
- [DMP](/glossary/dmp/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Customer context infrastructure: behavioral event pipeline for warehouses and AI agents. It ships with signals real-time profiles with propensity predictions, 7,031 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Snowplow is open source - Apache-2.0 licensed and free to self-host; the public repository carries 7,031 stars; native integrations cover Snowflake, Databricks, BigQuery. You pay in server time and maintenance, not licences.

The deepest behavioral-event infrastructure for teams that own their data pipeline, now priced and licensed like enterprise software rather than the free open-source project it once was.

Partly, and the details matter. The GitHub repo badge says Apache-2.0, but the README states that since January 8, 2024, new core pipeline releases ship under the Snowplow Limited Use License Agreement v1.1, which restricts commercial use, and the self-hosted docs say the community edition is for testing and evaluation and must not be deployed in production. Components released before 2024 keep Apache terms but get no security patches. The JavaScript tracker remains BSD-3-Clause, as are some client libraries. In practical terms: you can still inspect everything and self-host for evaluation, but production self-hosting requires a paid plan, which is why the pricing page lists a Self-Hosted Pipeline option described as removing the non-commercial restriction.

Signals, launched in May 2025, is Snowplow&#x27;s real-time context layer and the home of its AI-facing features. It combines a profiles store serving customer context with a published sub-10-millisecond p95 API claim, an interventions engine that triggers on rules or machine learning, and propensity predictions for conversion, churn, and lifetime value. It also exposes agentic context, meaning AI agents can read customer state at runtime through Python and Node SDKs. It sits downstream of the event pipeline: behavioral events feed profiles, profiles feed interventions and agents. If you are not building real-time personalization or agent-driven experiences, Signals is the part of the platform you can ignore.

## Similar Tools

## Related reading

- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
- [Claude Cowork is eating the edges of your martech stack](/blog/claude-cowork-is-eating-the-edges-of-your-martech-stack/)
- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
### Quick Facts

Related guides: [Snowplow in Matomo alternatives](/alternatives/matomo) · [Marketing Analytics Tools](/best/marketing-analytics-tools)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/snowplow/#app",
    "name": "Snowplow",
    "description": "Customer context infrastructure: behavioral event pipeline for warehouses and AI agents",
    "image": "https://martechsignal.com/og/tools/snowplow.png",
    "url": "https://martechsignal.com/tools/snowplow/",
    "sameAs": [
      "https://snowplow.io"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/snowplow/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-25",
    "datePublished": "2026-07-27",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://snowplow.io",
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
        "name": "Analytics & Attribution",
        "item": "https://martechsignal.com/categories/analytics/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Snowplow",
        "item": "https://martechsignal.com/tools/snowplow/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Snowplow?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Customer context infrastructure: behavioral event pipeline for warehouses and AI agents. It ships with signals real-time profiles with propensity predictions, 7,031 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Snowplow cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Snowplow is open source - Apache-2.0 licensed and free to self-host; the public repository carries 7,031 stars; native integrations cover Snowflake, Databricks, BigQuery. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Snowplow a good self-hosted Analytics & Attribution tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The deepest behavioral-event infrastructure for teams that own their data pipeline, now priced and licensed like enterprise software rather than the free open-source project it once was."
        }
      },
      {
        "@type": "Question",
        "name": "Is Snowplow still open source?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Partly, and the details matter. The GitHub repo badge says Apache-2.0, but the README states that since January 8, 2024, new core pipeline releases ship under the Snowplow Limited Use License Agreement v1.1, which restricts commercial use, and the self-hosted docs say the community edition is for testing and evaluation and must not be deployed in production. Components released before 2024 keep Apache terms but get no security patches. The JavaScript tracker remains BSD-3-Clause, as are some client libraries. In practical terms: you can still inspect everything and self-host for evaluation, but production self-hosting requires a paid plan, which is why the pricing page lists a Self-Hosted Pipeline option described as removing the non-commercial restriction."
        }
      },
      {
        "@type": "Question",
        "name": "What is Snowplow Signals?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Signals, launched in May 2025, is Snowplow's real-time context layer and the home of its AI-facing features. It combines a profiles store serving customer context with a published sub-10-millisecond p95 API claim, an interventions engine that triggers on rules or machine learning, and propensity predictions for conversion, churn, and lifetime value. It also exposes agentic context, meaning AI agents can read customer state at runtime through Python and Node SDKs. It sits downstream of the event pipeline: behavioral events feed profiles, profiles feed interventions and agents. If you are not building real-time personalization or agent-driven experiences, Signals is the part of the platform you can ignore."
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
    "reviewBody": "Snowplow is behavioral data infrastructure you can own: the pipeline is Apache-2.0 and the cloud is a quote. If an event schema matters more than a dashboard, this is the right layer.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/snowplow/#app",
      "name": "Snowplow",
      "url": "https://martechsignal.com/tools/snowplow/"
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
