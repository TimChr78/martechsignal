# Apache Unomi review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Free self-hosted Apache project with no commercial cloud tier to price (tools.json, verified 2026-09-28). |
| Feature depth | 5/10 | Profile unification, segmentation and personalization rules cover the CDP baseline (tools.json deep_dive). |
| Integrations | 4/10 | Karaf, Elasticsearch, MongoDB and GraphQL documented (tools.json). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (tools.json ai_features is empty). |
| Openness | 10/10 | Apache-2.0 under Apache Foundation governance with 375 GitHub stars (tools.json). |
| Operational maturity | 6/10 | Apache Foundation project status gives it institutional durability (tools.json). |


| Pros | Cons |
| --- | --- |
| &#10003; Apache-2.0 licence with free self-hosting | &#10007; Young project (375 GitHub stars) - smaller community and plugin ecosystem |
| &#10003; The privacy REST API covers consent, anonymization, and profile deletion out of the box, with no paid tier in front of it. | &#10007; No commercial cloud tier and no paid support exist, so every operational problem belongs to your team. |
| &#10003; Running on Karaf as an OSGi bundle makes new conditions and actions pluggable without forking the core. | &#10007; The quick start is a discovery setup; production hardening is documented but manual, and there is no default UI for privacy or configuration. |
| &#10003; Elasticsearch or MongoDB for storage and REST with JSON everywhere keeps the integration surface conventional. | &#10007; 375 GitHub stars means a small contributor base and little third-party tooling around the core. |

**What is Apache Unomi?**
Apache&#x27;s open-source customer data platform and personalization engine. It ships with 375 GitHub stars, an API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Apache Unomi cost?**
Apache Unomi is open source - Apache-2.0 licensed and free to self-host; the public repository carries 375 stars; native integrations cover Apache Karaf, Elasticsearch, MongoDB. You pay in server time and maintenance, not licences.

**Is Apache Unomi a good self-hosted Personalization &amp; CDP tool in 2026?**
A real CDP with privacy controls that you fully own and fully operate. The price is Java operations work and a small ecosystem, measured in attention rather than dollars.

**Is Apache Unomi free?**
Yes. It is an Apache Software Foundation project under the Apache-2.0 licence. There is no commercial cloud tier, no paid plan, and no licence fee.

**What does Unomi need to run?**
Java and Apache Karaf, with Elasticsearch or MongoDB for storage. The documented quick start uses Docker Compose with Elasticsearch 7.10.2, and the site labels that setup as not suitable for production.

**Does Unomi have an admin UI?**
Not a marketer-facing one. Unomi is a REST server, and the privacy and configuration interfaces in particular are left to developers to expose, as the project documentation states.

- **Pricing:** Open Source
- **Category:** [Personalization &amp; CDP](/categories/personalization/)
- **GitHub:** ★ 375
- **HQ:** Apache Software Foundation (community-governed)
- **API:** Yes
- **Last verified:** 2026-09-25

**Verdict:** Apache Unomi is a tool in Personalization &amp; CDP with free and open source. The catalog documents 4 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

Tealium

Enterprise customer data platform with real-time data orchestration and AI

Clerk.io

AI-powered ecommerce personalization with search, recommendations, and email

Jitsu

Open-source Segment alternative for event capture and warehouse-first data pipelines

Snowplow

Customer context infrastructure: behavioral event pipeline for warehouses and AI agents

Nosto

AI-powered ecommerce personalization with product recommendations and merchandising

[More Personalization &amp; CDP Tools →](/categories/personalization/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [Personalization &amp; CDP](/categories/personalization/)
- Apache Unomi
## Apache Unomi review (2026): pricing, AI features, verdict

Apache&#x27;s open-source customer data platform and personalization engine

Personalization &amp; CDP · Open Source · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-25

[Visit Apache Unomi &#8594;](https://unomi.apache.org)

[How we review](/methodology/) · No affiliate links

[Visit Apache Unomi &#8594;](https://unomi.apache.org)

## MartechSignal Score: 36/60

Apache Unomi is the neutral CDP: Apache-governed, self-hosted, and no vendor upsell anywhere. What you save in licensing you spend in engineering.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Apache Unomi is a Java customer data platform and personalization engine governed by the Apache Software Foundation, licensed Apache-2.0, with 375 stars on the apache/unomi repository. It runs as an OSGi application inside Apache Karaf and speaks HTTP REST with JSON payloads, managing user profiles, the events attached to those profiles, segments, scoring plans, and a rule system that fires actions when matching events arrive. The privacy REST API is the differentiator: integrators can build interfaces that let visitors see what has been collected, withdraw consent, anonymize past and future data, or delete a profile entirely. Unomi is also the reference implementation of the OASIS Context Server (CXS) specification for exchanging profile data between systems. The documented quick start is a Docker Compose file pairing the apache/unomi image with Elasticsearch 7.10.2 and exposing ports 8181, 9443, and 8102 behind default karaf credentials. The site states plainly that this configuration is for discovery and not for production. The current stable release is 3.0.1, with 3.1.0 in development. Unomi is built to integrate with CMS, CRM, and mobile systems over its REST API, its storage layer works with Elasticsearch or MongoDB, and new conditions and actions are added as Karaf plugins rather than by forking the core. There is no commercial cloud tier and no vendor selling support. Teams run it themselves and own the operations work. The project carries no licence fee and no paid feature tier, and the trade is a small community and a Java-heavy skill profile for full control over profile data.

## Key Integrations

- Apache Karaf
- Elasticsearch
- MongoDB
- GraphQL
## Pricing

Apache Unomi is free to self-host under the Apache-2.0 licence.

Free self-hosted Apache project; no commercial cloud tier

## Best for

Organizations that need profile management and personalization on their own infrastructure, especially those with GDPR obligations and Java or OSGi skills in-house.

## Not for

Teams that want a hosted CDP with a marketer-facing admin UI, prebuilt integrations, or a vendor to call when something breaks.

## Review notes

Assessed from unomi.apache.org and the project manual in September 2026, not from a running deployment. The quick start is a Docker Compose file pairing apache/unomi with Elasticsearch 7.10.2, and the site warns that the configuration is meant for discovery rather than production. The stack underneath is Java, OSGi, and Apache Karaf, which sets the skill profile of whoever ends up running it.

The privacy story is the reason to look at Unomi at all. A privacy REST API backs consent management, data access requests, anonymization of past and future events, and full profile deletion, and none of it ships with a default UI. Teams get the endpoints and build the visitor-facing screens themselves. That is more work than a consent checkbox and more control than most CDPs hand over.

The project is the reference implementation of the OASIS Context Server specification, and extension happens by plugging new conditions and actions into Karaf. Version 3.0.1 is the current stable. The repository carries 375 stars, which is small for a CDP, so expect fewer third-party guides, fewer integrations off the shelf, and a narrower hiring pool than the commercial alternatives.

## Verdict

A real CDP with privacy controls that you fully own and fully operate. The price is Java operations work and a small ecosystem, measured in attention rather than dollars.

## Pros and cons

## Related concepts

- [Personalization](/glossary/personalization/)
- [CRO](/glossary/cro/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Apache&#x27;s open-source customer data platform and personalization engine. It ships with 375 GitHub stars, an API for custom integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Apache Unomi is open source - Apache-2.0 licensed and free to self-host; the public repository carries 375 stars; native integrations cover Apache Karaf, Elasticsearch, MongoDB. You pay in server time and maintenance, not licences.

A real CDP with privacy controls that you fully own and fully operate. The price is Java operations work and a small ecosystem, measured in attention rather than dollars.

Yes. It is an Apache Software Foundation project under the Apache-2.0 licence. There is no commercial cloud tier, no paid plan, and no licence fee.

Java and Apache Karaf, with Elasticsearch or MongoDB for storage. The documented quick start uses Docker Compose with Elasticsearch 7.10.2, and the site labels that setup as not suitable for production.

Not a marketer-facing one. Unomi is a REST server, and the privacy and configuration interfaces in particular are left to developers to expose, as the project documentation states.

## Similar Tools

## Related reading

- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
- [Salesforce Made Agentforce Free. What Marketing Ops Can Build With It.](/blog/salesforce-agentforce-free-marketing-ops/)
- [What a free SEO audit replaces in your Semrush stack, and what it does not](/blog/what-claude-seo-replaces/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/apache-unomi/#app",
    "name": "Apache Unomi",
    "description": "Apache's open-source customer data platform and personalization engine",
    "image": "https://martechsignal.com/og/tools/apache-unomi.png",
    "url": "https://martechsignal.com/tools/apache-unomi/",
    "sameAs": [
      "https://unomi.apache.org"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/apache-unomi/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-25",
    "datePublished": "2026-09-25",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://unomi.apache.org",
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
        "name": "Apache Unomi",
        "item": "https://martechsignal.com/tools/apache-unomi/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Apache Unomi?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Apache's open-source customer data platform and personalization engine. It ships with 375 GitHub stars, an API for custom integrations. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Apache Unomi cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Apache Unomi is open source - Apache-2.0 licensed and free to self-host; the public repository carries 375 stars; native integrations cover Apache Karaf, Elasticsearch, MongoDB. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Apache Unomi a good self-hosted Personalization & CDP tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A real CDP with privacy controls that you fully own and fully operate. The price is Java operations work and a small ecosystem, measured in attention rather than dollars."
        }
      },
      {
        "@type": "Question",
        "name": "Is Apache Unomi free?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. It is an Apache Software Foundation project under the Apache-2.0 licence. There is no commercial cloud tier, no paid plan, and no licence fee."
        }
      },
      {
        "@type": "Question",
        "name": "What does Unomi need to run?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Java and Apache Karaf, with Elasticsearch or MongoDB for storage. The documented quick start uses Docker Compose with Elasticsearch 7.10.2, and the site labels that setup as not suitable for production."
        }
      },
      {
        "@type": "Question",
        "name": "Does Unomi have an admin UI?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Not a marketer-facing one. Unomi is a REST server, and the privacy and configuration interfaces in particular are left to developers to expose, as the project documentation states."
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
    "reviewBody": "Apache Unomi is the neutral CDP: Apache-governed, self-hosted, and no vendor upsell anywhere. What you save in licensing you spend in engineering.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/apache-unomi/#app",
      "name": "Apache Unomi",
      "url": "https://martechsignal.com/tools/apache-unomi/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 36,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```
