# Amplitude review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 6/10 | Free 2M events/mo with no time limit and Plus starting at $0 scaling with volume; Growth and Enterprise are custom (verified Sep 2026: [vendor site](https://amplitude.com), verified 2026-09-28). |
| Feature depth | 8/10 | Product analytics, funnels, cohorts and predictive analytics cover the behavioral analysis stack (vendor documentation: [vendor site](https://amplitude.com), verified 2026-09-28). |
| Integrations | 8/10 | Segment, Snowflake, Salesforce, Braze, Slack, Zapier, Google Ads and Meta Ads documented plus an API (vendor documentation: [vendor site](https://amplitude.com), verified 2026-09-28). |
| AI capability | 7/10 | AI root cause analysis, anomaly detection and natural-language queries turn analysis into answers (vendor documentation: [vendor site](https://amplitude.com), verified 2026-09-28). |
| Openness | 3/10 | Closed SaaS with warehouse-native exports softening the lock-in (the source repository: [repository](https://amplitude.com), verified 2026-09-28). |
| Operational maturity | 8/10 | Founded 2012 and publicly listed with enterprise analytics deployments behind it (vendor documentation: [vendor site](https://amplitude.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; AI capabilities: AI root cause analysis | &#10007; Closed source - no self-hosting option |
| &#10003; G2 rating 4.5/5 |  |
| &#10003; Native integrations include Segment, Snowflake, Salesforce (8 listed) |  |
| &#10003; Free tier to evaluate before committing (Free plan includes 2M events/month, no time limit) |  |

**What is Amplitude?**
AI-powered digital analytics platform for product and marketing teams. It ships with AI root cause analysis, 8 integrations documented on this page. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Amplitude cost?**
Amplitude has a free tier, so you can run a real evaluation before paying. Free plan includes 2M events/month, no time limit. Plus starts at $0 and scales with event volume. Growth and Enterprise are custom-priced (verified Sep 2026). We last checked the plan structure on 2026-09-25; paid tiers mainly raise limits rather than unlocking core features.

**Is Amplitude worth it past the free tier?**
Standard choice for product-led companies. For pure marketing analytics, Google Analytics 4 covers more channels with less cost.

**Does Amplitude have heatmaps?**
Not as classic click and scroll overlays. Amplitude&#x27;s closest equivalents are session replay and journey analysis, which reconstruct where users struggle after the fact. If heatmap overlays are the requirement, tools like Hotjar or Microsoft Clarity fill that gap, and both pair fine with Amplitude data.

**What are Amplitude&#x27;s pricing tiers?**
Four tiers.. Free: 2M events and 50,000 MTUs per month, 10 saved charts, 1,000 session replays, one year of data access, no credit card. Plus: usage based, first 2M events free, scaling to 70M events and 700,000 MTUs, two year retention, 20 behavioral cohorts, credit card required. Growth and Enterprise: both quoted by sales, with Enterprise adding unlimited projects, RBAC and SCIM, 50,000 replays, and a one business day SLA. A Startup Scholarship covers one free year of Growth for companies under $10M raised with fewer than 20 employees. Amplitude publishes no per tier dollar table; Plus is priced through an event volume calculator on its pricing page.

**What is an MTU in Amplitude, and what happens if I exceed my limit?**
An MTU is a unique user who triggers at least one event in your product in a calendar month. Anonymous users count by device ID, known users by user ID, and a person counts once across projects. The Free plan allows 50,000 MTUs and caps each at 1,000 events per month. On paid plans the limit is the MTU volume you purchase, and exceeding it can bring overage charges: each extra 1,000 events converts to one MTU at the plan&#x27;s per unit rate, with alerts at 80%, 90%, 100%, and 110%. On Free, crossing the limit three times blocks the account; Amplitude keeps ingesting data but you cannot read it until you upgrade, and the account is deleted after six months over limit.

**Amplitude vs Mixpanel: which should you pick?**
Mixpanel is cheaper and does event analytics well, which is enough if behavioral charts are the whole job. Amplitude&#x27;s comparison page argues for more than a point solution: experimentation, session replay, and a customer data platform in the same suite, plus autocapture, governance, and support it credits Mixpanel with lacking. Treat that as vendor framing. The practical test is whether you would buy a separate testing or replay tool anyway; if not, Mixpanel at a lower price point is the rational pick.

**Do you need Amplitude if you already have Google Analytics 4?**
They answer different questions. GA4 is built around acquisition, meaning which campaign or channel brought the visit, and it costs nothing. Amplitude is built around in product behavior: what a user did after arriving, which features retain, where a funnel breaks. Teams running a product led motion usually keep GA4 for channel reporting and add Amplitude for product decisions; teams that only need channel reporting usually do not need Amplitude at all. Amplitude&#x27;s own comparison page positions GA4 as a web and ads point solution that depends on BigQuery for deeper analysis, which is the vendor&#x27;s framing rather than an independent verdict.

**Does Amplitude have AI features?**
Yes. Amplitude AI is the umbrella for named agents including Global Agent, Dashboard Agent, Session Replay Agent, and Customer Feedback Agent, plus custom agents, predictive audiences, and automated anomaly detection. An MCP server connects Claude, Cursor, and other MCP clients, and Amplitude states it works on every plan including Free. Wave, described as a proactive product agent, is listed as reaching customers in the second half of 2026. Scope moves often; Amplitude&#x27;s AI docs carry the current list.

- **Pricing:** Freemium
- **Category:** [Analytics &amp; Attribution](/categories/analytics/)
- **Third-party ratingsG2 rating:** 4.5/5 (3,865 reviews) · [source](https://www.g2.com/sellers/amplitude)as of 2026-09-01
- **Founded:** 2012
- **HQ:** San Francisco, CA, USA
- **API:** Yes
- **Last verified:** 2026-09-25

**Verdict:** Amplitude is a tool in Analytics &amp; Attribution with a free tier. The catalog documents 5 AI features, 8 integrations and a public API. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

Heap

AI-powered product analytics with autocapture and digital experience insights

Mixpanel

Product analytics platform with AI-powered insights for user behavior tracking

PostHog

Open-source product analytics platform with session replay, feature flags, experiments, and surveys

Triple Whale

AI-powered ecommerce analytics and attribution platform for DTC brands

Ratings shown are third-party (G2), not MartechSignal's. Our hands-on assessment is disclosed on this page.

[More Analytics &amp; Attribution Tools →](/categories/analytics/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Analytics &amp; Attribution](/categories/analytics/)
- Amplitude
## Amplitude review (2026): pricing, AI features, verdict

AI-powered digital analytics platform for product and marketing teams

Analytics &amp; Attribution · Freemium Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-25

[Visit Amplitude &#8594;](https://amplitude.com)

[How we review](/methodology/) · No affiliate links

[Visit Amplitude &#8594;](https://amplitude.com)

## MartechSignal Score: 40/60

Amplitude is the analytics platform that answers product questions before marketing asks them, and the free 2M-event tier is genuinely usable. The AI root cause analysis earns its keep on messy funnels.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Amplitude is a digital analytics platform built on events: each action a user takes in a product becomes an event with properties, so teams can read funnels, retention, and feature adoption without writing SQL. The suite covers product analytics, experimentation and A/B testing, session replay, and customer data activation that syncs behavioral audiences to engagement tools. A Warehouse Native deployment queries data directly in Snowflake or Databricks rather than copying it, which is the draw for enterprises that already keep behavioral data in a warehouse. Metering is the part buyers most often misread. Amplitude counts monthly tracked users (MTUs), defined as unique users who trigger at least one event in a calendar month, alongside event volume. The Free plan includes 2M events and 50,000 MTUs per month with no credit card, capped at 1,000 events per MTU. Plus is usage based: the first 2M events cost nothing and the plan scales to 70M events and 700,000 MTUs, with overage billed at the same per unit rate as the plan and usage alerts at 80%, 90%, 100%, and 110%. Growth and Enterprise are quoted by sales, and a Startup Scholarship covers one free year of Growth for companies that have raised under $10M with fewer than 20 employees. AI features sit under the Amplitude AI label: named agents including Global Agent, Dashboard Agent, and Session Replay Agent, predictive audiences, anomaly detection, and an MCP server that connects Claude, Cursor, and other MCP clients on every plan including Free. Wave, described as a proactive product agent, is listed as reaching customers in the second half of 2026. Amplitude&#x27;s own comparison pages frame it against Google Analytics 4 as self service across the full customer journey rather than a web and ads point solution, and against Mixpanel as one suite with experimentation, session replay, and CDP included.

Amplitude homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI root cause analysis
- Predictive analytics
- AI anomaly detection
- AI-powered recommendations
- Natural language queries
## Key Integrations

- Segment
- Snowflake
- Salesforce
- Braze
- Slack
- Zapier
- Google Ads
- Meta Ads
## Pricing

Amplitude is freemium, with a free tier to start.

Free plan includes 2M events/month, no time limit. Plus starts at $0 and scales with event volume. Growth and Enterprise are custom-priced (verified Sep 2026).

Current plans and limits live on the [Amplitude pricing page](https://amplitude.com/pricing).

## Best for

Product-led growth teams that need event analytics, funnels, and experimentation in one place, and enterprises that want warehouse-native querying against Snowflake or Databricks.

## Not for

Teams that mainly need channel-level marketing reporting; GA4 covers acquisitions and campaigns at zero cost. Amplitude earns its price when product behavior questions drive decisions.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from Amplitude&#x27;s public docs, pricing pages, and comparison pages. Not a hands-on review. Amplitude is product analytics: events, funnels, retention, and now AI-generated insights. The strength is the event model, which lets you ask product questions without SQL. Funnel analysis and behavioral cohorts are the core reports. The learning curve is real but shallow enough for a data-literate marketer.

It helps to separate product analytics from web analytics. GA4 reports sessions, pageviews, and campaigns; Amplitude reports behavior: which features people use, in what order, and what the power users do differently. Marketing teams that only need channel reporting are fine in GA4. Teams that need to explain why retention moved or which feature drives upgrade need an event model like this one. The practical test: if your questions start with &#x27;which segment&#x27; or &#x27;what behavior&#x27; rather than &#x27;which channel&#x27;, you are in product analytics territory.

Instrumentation is the real cost. The free plan is generous, but the data is only as good as the tracking plan behind it: someone has to name events, define properties, and keep the taxonomy sane as the product changes. Amplitude&#x27;s partnership with Segment and its warehouse-native setup (querying data in Snowflake or Databricks instead of duplicating it) reduce that work for teams that already have pipelines. Teams starting from zero should budget effort for the tracking plan before budgeting for the plan tier.

Pricing has a generous entry point and scales steeply past it. As published in September 2026 the free plan covers 2M events and 50,000 MTUs per month, Plus is usage based with the first 2M events free and a ceiling of 70M events and 700,000 MTUs, and Growth and Enterprise are quoted by sales. Amplitude publishes no per tier dollar figure, so budget from the event volume calculator on its pricing page. Event volume is the part to watch: traffic spikes, bot traffic, and sloppy instrumentation all inflate the bill.

## Verdict

Standard choice for product-led companies. For pure marketing analytics, Google Analytics 4 covers more channels with less cost.

## Pros and cons

## Related concepts

- [Attribution models](/glossary/marketing-attribution-models/)
- [First-party data](/glossary/first-party-data/)
- [DMP](/glossary/dmp/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

AI-powered digital analytics platform for product and marketing teams. It ships with AI root cause analysis, 8 integrations documented on this page. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Amplitude has a free tier, so you can run a real evaluation before paying. Free plan includes 2M events/month, no time limit. Plus starts at $0 and scales with event volume. Growth and Enterprise are custom-priced (verified Sep 2026). We last checked the plan structure on 2026-09-25; paid tiers mainly raise limits rather than unlocking core features.

Standard choice for product-led companies. For pure marketing analytics, Google Analytics 4 covers more channels with less cost.

Not as classic click and scroll overlays. Amplitude&#x27;s closest equivalents are session replay and journey analysis, which reconstruct where users struggle after the fact. If heatmap overlays are the requirement, tools like Hotjar or Microsoft Clarity fill that gap, and both pair fine with Amplitude data.

Four tiers.. Free: 2M events and 50,000 MTUs per month, 10 saved charts, 1,000 session replays, one year of data access, no credit card. Plus: usage based, first 2M events free, scaling to 70M events and 700,000 MTUs, two year retention, 20 behavioral cohorts, credit card required. Growth and Enterprise: both quoted by sales, with Enterprise adding unlimited projects, RBAC and SCIM, 50,000 replays, and a one business day SLA. A Startup Scholarship covers one free year of Growth for companies under $10M raised with fewer than 20 employees. Amplitude publishes no per tier dollar table; Plus is priced through an event volume calculator on its pricing page.

An MTU is a unique user who triggers at least one event in your product in a calendar month. Anonymous users count by device ID, known users by user ID, and a person counts once across projects. The Free plan allows 50,000 MTUs and caps each at 1,000 events per month. On paid plans the limit is the MTU volume you purchase, and exceeding it can bring overage charges: each extra 1,000 events converts to one MTU at the plan&#x27;s per unit rate, with alerts at 80%, 90%, 100%, and 110%. On Free, crossing the limit three times blocks the account; Amplitude keeps ingesting data but you cannot read it until you upgrade, and the account is deleted after six months over limit.

Mixpanel is cheaper and does event analytics well, which is enough if behavioral charts are the whole job. Amplitude&#x27;s comparison page argues for more than a point solution: experimentation, session replay, and a customer data platform in the same suite, plus autocapture, governance, and support it credits Mixpanel with lacking. Treat that as vendor framing. The practical test is whether you would buy a separate testing or replay tool anyway; if not, Mixpanel at a lower price point is the rational pick.

They answer different questions. GA4 is built around acquisition, meaning which campaign or channel brought the visit, and it costs nothing. Amplitude is built around in product behavior: what a user did after arriving, which features retain, where a funnel breaks. Teams running a product led motion usually keep GA4 for channel reporting and add Amplitude for product decisions; teams that only need channel reporting usually do not need Amplitude at all. Amplitude&#x27;s own comparison page positions GA4 as a web and ads point solution that depends on BigQuery for deeper analysis, which is the vendor&#x27;s framing rather than an independent verdict.

Yes. Amplitude AI is the umbrella for named agents including Global Agent, Dashboard Agent, Session Replay Agent, and Customer Feedback Agent, plus custom agents, predictive audiences, and automated anomaly detection. An MCP server connects Claude, Cursor, and other MCP clients, and Amplitude states it works on every plan including Free. Wave, described as a proactive product agent, is listed as reaching customers in the second half of 2026. Scope moves often; Amplitude&#x27;s AI docs carry the current list.

## Similar Tools

## Related reading

- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
- [MCP Rewrites the Integration Economics of Your Marketing Stack](/blog/mcp-rewrites-the-integration-economics-of-your-marketing-stack/)
### Quick Facts

Related guides: [Amplitude in Matomo alternatives](/alternatives/matomo/) · [Marketing Analytics Tools](/best/marketing-analytics-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/amplitude/#app",
    "name": "Amplitude",
    "description": "AI-powered digital analytics platform for product and marketing teams",
    "image": "https://martechsignal.com/og/tools/amplitude.png",
    "url": "https://martechsignal.com/tools/amplitude/",
    "sameAs": [
      "https://amplitude.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/amplitude/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-26",
    "datePublished": "2026-07-27"
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
        "name": "Amplitude",
        "item": "https://martechsignal.com/tools/amplitude/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Amplitude?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "AI-powered digital analytics platform for product and marketing teams. It ships with AI root cause analysis, 8 integrations documented on this page. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Amplitude cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Amplitude has a free tier, so you can run a real evaluation before paying. Free plan includes 2M events/month, no time limit. Plus starts at $0 and scales with event volume. Growth and Enterprise are custom-priced (verified Sep 2026). We last checked the plan structure on 2026-09-25; paid tiers mainly raise limits rather than unlocking core features."
        }
      },
      {
        "@type": "Question",
        "name": "Is Amplitude worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Standard choice for product-led companies. For pure marketing analytics, Google Analytics 4 covers more channels with less cost."
        }
      },
      {
        "@type": "Question",
        "name": "Does Amplitude have heatmaps?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Not as classic click and scroll overlays. Amplitude's closest equivalents are session replay and journey analysis, which reconstruct where users struggle after the fact. If heatmap overlays are the requirement, tools like Hotjar or Microsoft Clarity fill that gap, and both pair fine with Amplitude data."
        }
      },
      {
        "@type": "Question",
        "name": "What are Amplitude's pricing tiers?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Four tiers.. Free: 2M events and 50,000 MTUs per month, 10 saved charts, 1,000 session replays, one year of data access, no credit card. Plus: usage based, first 2M events free, scaling to 70M events and 700,000 MTUs, two year retention, 20 behavioral cohorts, credit card required. Growth and Enterprise: both quoted by sales, with Enterprise adding unlimited projects, RBAC and SCIM, 50,000 replays, and a one business day SLA. A Startup Scholarship covers one free year of Growth for companies under $10M raised with fewer than 20 employees. Amplitude publishes no per tier dollar table; Plus is priced through an event volume calculator on its pricing page."
        }
      },
      {
        "@type": "Question",
        "name": "What is an MTU in Amplitude, and what happens if I exceed my limit?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "An MTU is a unique user who triggers at least one event in your product in a calendar month. Anonymous users count by device ID, known users by user ID, and a person counts once across projects. The Free plan allows 50,000 MTUs and caps each at 1,000 events per month. On paid plans the limit is the MTU volume you purchase, and exceeding it can bring overage charges: each extra 1,000 events converts to one MTU at the plan's per unit rate, with alerts at 80%, 90%, 100%, and 110%. On Free, crossing the limit three times blocks the account; Amplitude keeps ingesting data but you cannot read it until you upgrade, and the account is deleted after six months over limit."
        }
      },
      {
        "@type": "Question",
        "name": "Amplitude vs Mixpanel: which should you pick?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Mixpanel is cheaper and does event analytics well, which is enough if behavioral charts are the whole job. Amplitude's comparison page argues for more than a point solution: experimentation, session replay, and a customer data platform in the same suite, plus autocapture, governance, and support it credits Mixpanel with lacking. Treat that as vendor framing. The practical test is whether you would buy a separate testing or replay tool anyway; if not, Mixpanel at a lower price point is the rational pick."
        }
      },
      {
        "@type": "Question",
        "name": "Do you need Amplitude if you already have Google Analytics 4?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "They answer different questions. GA4 is built around acquisition, meaning which campaign or channel brought the visit, and it costs nothing. Amplitude is built around in product behavior: what a user did after arriving, which features retain, where a funnel breaks. Teams running a product led motion usually keep GA4 for channel reporting and add Amplitude for product decisions; teams that only need channel reporting usually do not need Amplitude at all. Amplitude's own comparison page positions GA4 as a web and ads point solution that depends on BigQuery for deeper analysis, which is the vendor's framing rather than an independent verdict."
        }
      },
      {
        "@type": "Question",
        "name": "Does Amplitude have AI features?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. Amplitude AI is the umbrella for named agents including Global Agent, Dashboard Agent, Session Replay Agent, and Customer Feedback Agent, plus custom agents, predictive audiences, and automated anomaly detection. An MCP server connects Claude, Cursor, and other MCP clients, and Amplitude states it works on every plan including Free. Wave, described as a proactive product agent, is listed as reaching customers in the second half of 2026. Scope moves often; Amplitude's AI docs carry the current list."
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
    "reviewBody": "Amplitude is the analytics platform that answers product questions before marketing asks them, and the free 2M-event tier is genuinely usable. The AI root cause analysis earns its keep on messy funnels.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/amplitude/#app",
      "name": "Amplitude",
      "url": "https://martechsignal.com/tools/amplitude/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 40,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
