# Flagsmith review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 8/10 | Cloud free up to 50K API requests/mo, Scale $50/member/mo (launch discount from $60 shown Sep 2026), extra calls $50 per million (the vendor pricing page: [pricing page](https://www.flagsmith.com/pricing), verified 2026-09-28). |
| Feature depth | 6/10 | Feature flags, remote config and segment targeting cover the flag management job (vendor documentation: [vendor site](https://www.flagsmith.com), verified 2026-09-28). |
| Integrations | 5/10 | Datadog, Grafana, Jira, GitHub, Amplitude and Mixpanel documented plus an API (vendor documentation: [vendor site](https://www.flagsmith.com), verified 2026-09-28). |
| AI capability | 6/10 | MCP flag management, automated flag hygiene and prompt/model A/B testing are current-agent features (vendor documentation: [vendor site](https://www.flagsmith.com), verified 2026-09-28). |
| Openness | 9/10 | BSD-3-Clause with 6.6k GitHub stars and full self-hosting (the source repository: [repository](Flagsmith/flagsmith), verified 2026-09-28). |
| Operational maturity | 6/10 | Commercial backing behind the OSS core with priced cloud tiers (vendor documentation: [vendor site](https://www.flagsmith.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; BSD-3-Clause licence with free self-hosting | &#10007; The free cloud tier caps at 50,000 API requests a month, which a busy production app passes quickly. |
| &#10003; AI capabilities: MCP Server for natural-language flag management | &#10007; Scale pricing is per member, so seat count drives the bill, and the September 2026 price is a launch discount against a USD 60 list. |
| &#10003; Active public repository (6,570 GitHub stars counted at last check) | &#10007; Extra API calls start at USD 50 per million, which turns surprise traffic into a real line item. |
| &#10003; Native integrations include Datadog, Grafana, Jira (6 listed) |  |
| &#10003; Native integrations span observability, delivery, and analytics, so flag changes land in tools teams already watch. |  |
| &#10003; The MCP server puts change requests and approvals in the path when AI tools make flag changes. |  |
| &#10003; Self-hosting the BSD-3-Clause code is a documented deployment path alongside cloud and private cloud. |  |

**What is Flagsmith?**
Open-source feature flag and remote config platform with segment targeting. It ships with MCP Server for natural-language flag management, 6,570 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Flagsmith cost?**
Flagsmith is open source - BSD-3-Clause licensed and free to self-host; the public repository carries 6,570 stars; native integrations cover Datadog, Grafana, Jira. You pay in server time and maintenance, not licences.

**Is Flagsmith worth it past the free tier?**
A flag platform with the change-control story that regulated teams ask for, priced below the big names, and self-hosting keeps the exit open.

**Can Flagsmith be self-hosted?**
Yes. The code is BSD-3-Clause on GitHub, and self-hosted and private cloud deployments are documented alongside the hosted cloud.

**Does Flagsmith have an MCP server?**
Yes. It lets AI tools manage flags, create segments, schedule changes, and automate flag hygiene in natural language, with change requests and approvals still in the loop.

- **Pricing:** Freemium
- **Category:** [Personalization &amp; CDP](/categories/personalization/)
- **GitHub:** ★ 6570
- **HQ:** London, United Kingdom (Bullet Train Ltd, 66 Paul St)
- **API:** Yes
- **Last verified:** 2026-09-25

**Verdict:** Flagsmith is a tool in Personalization &amp; CDP with free and open source. The catalog documents 4 AI features, 6 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

GrowthBook

Open-source feature flags and A/B testing with a visual editor and attribute-based targeting

Jitsu

Open-source Segment alternative for event capture and warehouse-first data pipelines

PostHog

Open-source product analytics platform with session replay, feature flags, experiments, and surveys

n8n

Open-source workflow automation platform with AI agent capabilities and 400+ nodes

[More Personalization &amp; CDP Tools →](/categories/personalization/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Personalization &amp; CDP](/categories/personalization/)
- Flagsmith
## Flagsmith review (2026): pricing, AI features, verdict

Open-source feature flag and remote config platform with segment targeting

Personalization &amp; CDP · Freemium · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-25

[Visit Flagsmith &#8594;](https://www.flagsmith.com)

[How we review](/methodology/) · No affiliate links

[Visit Flagsmith &#8594;](https://www.flagsmith.com)

## MartechSignal Score: 40/60

Flagsmith is the open-source flag platform that grew an AI layer where it belongs: change workflows and prompt testing. BSD-3 licensing and a real free tier make the trial honest.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Flagsmith is an open-source feature flag and remote configuration platform, BSD-3-Clause, with 6,570 GitHub stars GitHub stars, operated commercially by Bullet Train Ltd out of London. Flags and remote config values are managed per environment, with segment targeting, A/B and multivariate testing, and identity evaluation against user traits. Governance carries much of the pitch: role-based access control, four-eyes change requests, scheduled flag changes, audit logs, and flag governance policies. SDKs cover the usual server, web, and mobile stacks, an Edge API serves flags close to users, and real-time flag updates keep clients current. Deployment options are cloud, self-hosted, and private cloud, with data centers listed in East Ohio, London, California, Mumbai, Sydney, and Sao Paulo. Cloud pricing has a free tier up to 50,000 API requests a month. The Scale plan is USD 50 per member per month as of September 2026, shown against a list price of 60 as a launch discount, and extra API calls start at USD 50 per million. Self-hosting the open-source code costs nothing. Integrations run deep on the observability and delivery side: Datadog, Grafana, Dynatrace, New Relic, Sentry, GitHub, GitLab, Jira, Backstage, Amplitude, and Mixpanel all have native connections. An MCP server lets AI tools manage flags in natural language, and change requests and approval workflows stay in the loop when they do. Flag hygiene automation is pitched as the fix for stale flags piling up.

## AI Capabilities

- MCP Server for natural-language flag management
- Automated flag hygiene
- AI-assisted change-request workflows
- Prompt and model A/B testing (Flagsmith for AI)
## Key Integrations

- Datadog
- Grafana
- Jira
- GitHub
- Amplitude
- Mixpanel
## Pricing

Flagsmith is freemium, with a free tier to start.

Cloud free tier up to 50,000 API requests/mo. Scale USD 50/member/month (list 60, launch discount shown Sep 2026). Extra API calls from USD 50 per million. Self-hosted open source is free.

Current plans and limits live on the [Flagsmith pricing page](https://www.flagsmith.com/pricing).

## Best for

Engineering teams in finance, healthcare, or insurance that need change control, audit logs, and a self-hosted path alongside a cloud option.

## Not for

Teams whose main need is experimentation analytics. A/B and multivariate testing exist, but the statistics and warehouse tooling are lighter than a dedicated experimentation platform.

## Review notes

Assessed from flagsmith.com, docs.flagsmith.com, the pricing page, and the repository in September 2026, without running an instance. The product is feature flags and remote config with segment targeting, A/B and multivariate testing, and identity evaluation against user traits. Deployment choices are cloud, self-hosted, and private cloud, and the commercial operator is Bullet Train Ltd, registered in London.

Governance is where Flagsmith puts its weight. Role-based access control, four-eyes change requests, scheduled flag changes, audit logs, and flag governance policies are documented as core features, and the customer logos on the site lean toward banks, insurers, and healthcare. Teams in regulated environments are clearly who the product is built for.

The integration catalog is one of the widest in this category: Datadog, Grafana, Dynatrace, New Relic, Sentry, GitHub, GitLab, Jira, Backstage, Amplitude, and Mixpanel all have native connections. The MCP server lets AI tools create segments, schedule flags, and run rollouts in natural language, with change request approvals still in the loop. Flag hygiene automation is the pitch for the usual problem of stale flags outliving their features.

## Verdict

A flag platform with the change-control story that regulated teams ask for, priced below the big names, and self-hosting keeps the exit open.

## Pros and cons

## Related concepts

- [Personalization](/glossary/personalization/)
- [CRO](/glossary/cro/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open-source feature flag and remote config platform with segment targeting. It ships with MCP Server for natural-language flag management, 6,570 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Flagsmith is open source - BSD-3-Clause licensed and free to self-host; the public repository carries 6,570 stars; native integrations cover Datadog, Grafana, Jira. You pay in server time and maintenance, not licences.

A flag platform with the change-control story that regulated teams ask for, priced below the big names, and self-hosting keeps the exit open.

Yes. The code is BSD-3-Clause on GitHub, and self-hosted and private cloud deployments are documented alongside the hosted cloud.

Yes. It lets AI tools manage flags, create segments, schedule changes, and automate flag hygiene in natural language, with change requests and approvals still in the loop.

## Similar Tools

## Related reading

- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
- [ChatGPT Isn't Search Anymore, It's Checkout](/blog/chatgpt-isnt-search-anymore-its-checkout/)
## Also featured in

- [Best AI Personalization &amp; CDP tools (2026): 8 compared](/best/ai-personalization-tools/) &mdash; Teams that want their experiment engine as open as their stack
### Quick Facts

Related guides: [Ai Personalization Tools](/best/ai-personalization-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/flagsmith/#app",
    "name": "Flagsmith",
    "description": "Open-source feature flag and remote config platform with segment targeting",
    "image": "https://martechsignal.com/og/tools/flagsmith.png",
    "url": "https://martechsignal.com/tools/flagsmith/",
    "sameAs": [
      "https://www.flagsmith.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/flagsmith/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-28",
    "datePublished": "2026-09-25",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://www.flagsmith.com/pricing",
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
        "name": "Flagsmith",
        "item": "https://martechsignal.com/tools/flagsmith/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Flagsmith?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Open-source feature flag and remote config platform with segment targeting. It ships with MCP Server for natural-language flag management, 6,570 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Flagsmith cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Flagsmith is open source - BSD-3-Clause licensed and free to self-host; the public repository carries 6,570 stars; native integrations cover Datadog, Grafana, Jira. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Flagsmith worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A flag platform with the change-control story that regulated teams ask for, priced below the big names, and self-hosting keeps the exit open."
        }
      },
      {
        "@type": "Question",
        "name": "Can Flagsmith be self-hosted?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. The code is BSD-3-Clause on GitHub, and self-hosted and private cloud deployments are documented alongside the hosted cloud."
        }
      },
      {
        "@type": "Question",
        "name": "Does Flagsmith have an MCP server?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. It lets AI tools manage flags, create segments, schedule changes, and automate flag hygiene in natural language, with change requests and approvals still in the loop."
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
    "reviewBody": "Flagsmith is the open-source flag platform that grew an AI layer where it belongs: change workflows and prompt testing. BSD-3 licensing and a real free tier make the trial honest.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/flagsmith/#app",
      "name": "Flagsmith",
      "url": "https://martechsignal.com/tools/flagsmith/"
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
