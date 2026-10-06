# Apache Unomi review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Personalization & CDP](/categories/personalization/)
- Apache Unomi
## Apache Unomi review (2026): pricing, AI features, verdict

Apache's open-source customer data platform and personalization engine

Personalization & CDP · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Apache Unomi →](https://unomi.apache.org)

[How we review](/methodology/) · No affiliate links

**Verdict:** Apache Unomi is a tool in Personalization & CDP with free and open source. The catalog documents 4 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

[Visit Apache Unomi →](https://unomi.apache.org)

## MartechSignal Score: 36/60

Apache Unomi is the neutral CDP: Apache-governed, self-hosted, and no vendor upsell anywhere. What you save in licensing you spend in engineering.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Free self-hosted Apache project with no commercial cloud tier to price (the vendor pricing page: [vendor site](https://unomi.apache.org), verified 2026-09-25). |
| Feature depth | 5/10 | Profile unification, segmentation and personalization rules cover the CDP baseline (vendor documentation: [vendor site](https://unomi.apache.org), verified 2026-09-28). |
| Integrations | 4/10 | Karaf, Elasticsearch, MongoDB and GraphQL documented (vendor documentation: [vendor site](https://unomi.apache.org), verified 2026-09-28). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation: [vendor site](https://unomi.apache.org), verified 2026-09-28). |
| Openness | 10/10 | Apache-2.0 under Apache Foundation governance (the source repository: [repository](https://github.com/apache/unomi), verified 2026-09-28). |
| Operational maturity | 6/10 | Apache Foundation project status gives it institutional durability (vendor documentation: [vendor site](https://unomi.apache.org), verified 2026-09-28). |

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


| Pros | Cons |
| --- | --- |
| ✓ Apache-2.0 licence with free self-hosting | ✗ Young project (375 GitHub stars) - smaller community and plugin ecosystem |
| ✓ The privacy REST API covers consent, anonymization, and profile deletion out of the box, with no paid tier in front of it. | ✗ No commercial cloud tier and no paid support exist, so every operational problem belongs to your team. |
| ✓ Running on Karaf as an OSGi bundle makes new conditions and actions pluggable without forking the core. | ✗ The quick start is a discovery setup; production hardening is documented but manual, and there is no default UI for privacy or configuration. |
| ✓ Elasticsearch or MongoDB for storage and REST with JSON everywhere keeps the integration surface conventional. | ✗ 375 GitHub stars means a small contributor base and little third-party tooling around the core. |

## Related concepts

- [Personalization](/glossary/personalization/)
- [CRO](/glossary/cro/)
- [First-party data](/glossary/first-party-data/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Apache Unomi?**
Apache Unomi: Apache's open-source customer data platform and personalization engine. The public repository carries 375 stars. Apache Unomi offers a public API for custom integrations.

**How much does Apache Unomi cost?**
Apache Unomi is open source - Apache-2.0 licensed and free to self-host; the public repository carries 375 stars; native integrations cover Apache Karaf, Elasticsearch, MongoDB. You pay in server time and maintenance, not licences.

**Is Apache Unomi a good self-hosted Personalization & CDP tool in 2026?**
A real CDP with privacy controls that you fully own and fully operate. The price is Java operations work and a small ecosystem, measured in attention rather than dollars.

**Is Apache Unomi free?**
Yes. It is an Apache Software Foundation project under the Apache-2.0 licence. There is no commercial cloud tier, no paid plan, and no licence fee.

**What does Unomi need to run?**
Java and Apache Karaf, with Elasticsearch or MongoDB for storage. The documented quick start uses Docker Compose with Elasticsearch 7.10.2, and the site labels that setup as not suitable for production.

**Does Unomi have an admin UI?**
Not a marketer-facing one. Unomi is a REST server, and the privacy and configuration interfaces in particular are left to developers to expose, as the project documentation states.

## Similar Tools

- [Tealium](/tools/tealium/): Enterprise customer data platform with real-time data orchestration and AI
- [Clerk.io](/tools/clerk-io/): AI-powered ecommerce personalization with search, recommendations, and email
- [Jitsu](/tools/jitsu/): Open-source Segment alternative for event capture and warehouse-first data pipelines
- [RudderStack](/tools/rudderstack/): Warehouse-first CDP: open-source Go data plane plus managed routing
- [Nosto](/tools/nosto/): AI-powered ecommerce personalization with product recommendations and merchandising
## Related reading

- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
- [Competitive-Intel Tools Were the First Martech Category AI Killed](/blog/ci-tools-were-the-first-martech-category-ai-killed/)
- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
## Also featured in

- [Best Customer Data Platforms (2026): composable to self-hosted](/best/cdp/) — Best when data-residency rules and European-consent governance drive the architecture.
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Personalization & CDP](/categories/personalization/)
- **GitHub:** ★ 375
- **HQ:** Apache Software Foundation (community-governed)
- **API:** Yes
- **Repository checked:** 2026-09-29
- **Page updated:** 2026-09-25

Related guides: [Cdp](/best/cdp/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Personalization & CDP Tools →](/categories/personalization/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
