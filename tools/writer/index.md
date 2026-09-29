# Writer review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 2/10 | Quote-based: writer.com serves no public price table to anonymous visitors (verified Sep 2026: [vendor site](https://writer.com), verified 2026-09-28). |
| Feature depth | 8/10 | Brand governance, Knowledge Graph grounding and 100+ prebuilt agents in the Agent Library make it a platform (vendor documentation: [vendor site](https://writer.com), verified 2026-09-28). |
| Integrations | 8/10 | Slack, Google Workspace, Microsoft 365, Salesforce, HubSpot, Contentful, Figma, Snowflake and Databricks documented plus an API (vendor documentation: [vendor site](https://writer.com), verified 2026-09-28). |
| AI capability | 8/10 | Its own Palmyra model family plus Knowledge Graph grounding and agent tooling go past wrapper territory (vendor documentation: [vendor site](https://writer.com), verified 2026-09-28). |
| Openness | 3/10 | Closed platform, though the Palmyra models and API keep some portability (the source repository: [repository](https://writer.com), verified 2026-09-28). |
| Operational maturity | 7/10 | Founded 2020 with enterprise governance features and named compliance posture (vendor documentation: [vendor site](https://writer.com), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| &#10003; AI capabilities: AI content generation | &#10007; Closed source - no self-hosting option |
| &#10003; Native integrations include Slack, Google Workspace, Microsoft 365 (12 listed) |  |
| &#10003; API access for custom integrations |  |

**What is Writer?**
Writer: Enterprise AI platform with Palmyra models, brand governance, and agents. Writer ships with AI content generation. This page documents 12 integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Writer cost?**
Writer uses paid pricing, so the number depends on your volume and contract. Quote-based. Writer.com serves no public price table to anonymous visitors (verified Sep 2026). Our last verified read of the pricing model was 2026-09-25; the vendor&#x27;s pricing page carries the current quote criteria.

**Is Writer worth paying for in 2026?**
A governed enterprise AI platform with its own models and a real compliance story; the writing tool inside it is now the smallest part, and the price tag is whatever sales says it is.

**Does Writer train its models on my company&#x27;s data?**
The company says no. The plans page states that you retain full ownership of your data and that Writer takes a zero data retention approach and does not train or improve models on customer data by default, and the trust page repeats that data shared with Writer is not used to create, modify, or train models. Organization-wide data controls, including an automated deletion schedule, are documented, and enterprise buyers can request SOC 2 Type II and HIPAA reports and a BAA.

**What is included in Writer&#x27;s Starter plan and what are its limits?**
Starter is the self-serve tier: a 14-day free trial with no credit card, up to 5 users, the WRITER Agent interface, up to 5 Playbooks, 1 team Personality profile, basic connectors, and a limited Knowledge Graph. The comparison table caps scheduled routines at 3, active connectors at 3, and graph storage at 50 GB, and roles are limited to one team. No per-seat price is published on the page.

**How much do the Palmyra models cost via the API?**
Published in the developer docs: Palmyra X6 at $2 per million input tokens and $8 per million output tokens with a 1M context window, Palmyra X5 at $0.60 and $6.00 with the same window, and Palmyra X4 at $2.50 and $10.00 with 128k context and a documented deprecation date of November 18, 2026. X5 is also available on Amazon Bedrock; the docs quote X6 at $0.12 of average cost per finished task.

- **Pricing:** Paid
- **Category:** [AI Content &amp; Copywriting](/categories/content-ai/)
- **Founded:** 2020
- **HQ:** San Francisco, CA, USA
- **API:** Yes
- **Last verified:** 2026-09-25

**Verdict:** Writer is a tool in AI Content &amp; Copywriting with custom pricing. The catalog documents 5 AI features, 12 integrations and a public API. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

Tealium

Enterprise customer data platform with real-time data orchestration and AI

Workato

Enterprise AI governance plus integration and automation on one platform

Jasper

AI marketing content platform for creating on-brand copy, images, and campaigns

Intercom

AI-first customer service platform with Fin AI agent and omnichannel messaging

LanguageTool

Open-source writing assistant and grammar checker with AI style and tone suggestions for 30+ languages

[More AI Content &amp; Copywriting Tools →](/categories/content-ai/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [AI Content &amp; Copywriting](/categories/content-ai/)
- Writer
## Writer review (2026): pricing, AI features, verdict

Enterprise AI platform with Palmyra models, brand governance, and agents

AI Content &amp; Copywriting · Paid Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-25

[Visit Writer &#8594;](https://writer.com)

[How we review](/methodology/) · No affiliate links

[Visit Writer &#8594;](https://writer.com)

## MartechSignal Score: 36/60

Writer is the enterprise content platform with its own Palmyra models and brand governance that legal teams can read. With no public prices, it competes on trust and procurement comfort.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Writer is an enterprise AI platform built around its own Palmyra model family rather than a wrapped third-party LLM, and its positioning has shifted from AI writing assistant to governed agent platform. The Palmyra lineup is now X4, X5, and X6: X6 is described as the default agentic model with a 1M-token context window, published API pricing of $2 per million input tokens and $8 per million output tokens, and a claimed 8 hours of unsupervised task persistence, while X4 carries a documented deprecation date of November 18, 2026. Smaller Palmyra variants have been released as open weights on Hugging Face, including palmyra-mini and two thinking variants under Apache 2.0 in September 2025. On the application layer, WRITER Agent plans and executes work, an Agent Library lists more than 100 prebuilt agents, and AI Studio acts as the control plane for building and governing them. Governance is the real product: voice profiles, terminology lists, style guides, and Skills encode brand rules, and the company states that language is enforced before any reviewer sees a draft. Security posture is unusually explicit: no training on customer data, zero data retention by default, SOC 2 Type II plus ISO 27001, 27701, and 42001, HIPAA and PCI badges, and customer-managed encryption keys. Pricing changed materially in 2026: the plans page now shows a self-serve Starter tier with a 14-day trial capped at 5 users and no published per-seat price, plus quote-based Enterprise with Pro and Lite seat types. Founded in 2020 in San Francisco by May Habib and Waseem AlShikh, Writer reports $326M raised at a $1.9B valuation, and names KPMG, Intuit, Mars, Uber, Vanguard, and Salesforce among customers. Connectors reach into Salesforce, Snowflake, Databricks, Contentful, and Microsoft 365, so agents and answers ground in company data rather than general model knowledge, and the dev docs list LangChain and Amazon Bedrock entry points for engineering teams.

Writer homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- AI content generation
- Brand governance (voice profiles, terminology lists, style guides)
- Knowledge Graph grounding
- AI agents (100+ prebuilt Agent Library)
- Palmyra LLMs (X4, X5, X6)
## Key Integrations

- Slack
- Google Workspace
- Microsoft 365
- Salesforce
- HubSpot
- Contentful
- Chrome extension
- Microsoft Word
- Figma
- Snowflake
- Databricks
- Webflow
## Pricing

Writer is sold on paid plans.

Quote-based. Writer.com serves no public price table to anonymous visitors (verified Sep 2026).

Current plans and limits live on the [Writer pricing page](https://writer.com/plans/).

## How to install

- No install: Writer is hosted SaaS. Start with the 14-day free trial on the plans page, which the page states needs no credit card.
- Starter is capped at 5 users and includes WRITER Agent, up to 5 Playbooks, 1 team Personality profile, basic connectors, and a limited Knowledge Graph.
- Connect your data through the connectors catalog (Salesforce, Snowflake, Databricks, Contentful, Slack, Microsoft 365, Google Workspace, and others) so agents and answers are grounded in company context.
- For editor use, install Writer for Chrome from the Chrome Web Store, or the Word add-in; the support centre documents Chrome, Word, Figma, Outlook, Teams, and Slack surfaces.
- API and agent work happens at dev.writer.com: Palmyra models are callable directly (X5 also available on Amazon Bedrock as us.writer.palmyra-x5-v1:0) with Python and Node SDKs at v3.0.0.
## Requirements

A browser for the app and, for API use, an account with model access; Starter is limited to 5 users and 3 active connectors, so anything past a pilot means Enterprise procurement. Regulated deployments should confirm the BAA and DPA paperwork, which Writer says is available on request for Enterprise plans.

## Best for

Enterprise content and go-to-market teams that need AI output to obey brand and terminology rules by default, and platform teams that want to build governed agents on their own data with a model family they can also call directly.

## Not for

Solo writers and small teams: Starter caps at 5 users and the published price is gone, so there is no cheap individual entry point any more. Teams wanting a model-agnostic tool that sits on top of OpenAI or Anthropic models will also find Writer opinionated about running its own.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

Researched from writer.com, dev.writer.com, the support centre, and the Hugging Face model index (September 2026). Not a hands-on review. Direct fetches of writer.com pages are Cloudflare-gated, so quotes here come from the rendered pages and the developer docs.

The pricing correction is the biggest one. Our record carried Team at $18-25 per user per month and Starter at $29-39, and both are gone: the current plans page contains no dollar figure and no per-seat or per-user string at all. It shows Starter (self-serve, 14-day trial, up to 5 users, 5 Playbooks, 3 scheduled routines, 3 active connectors, 50 GB in a single graph) and Enterprise (quote-based, Pro and Lite seats, 20% discount for nonprofits and educational institutions). We have therefore removed the $18 figure from our structured data rather than publish a number the vendor no longer states.

Two framing corrections follow. AI Studio is no longer fairly described as a no-code app builder for business users; Writer now positions it as a single control plane for agents, and the phrase without writing code appears nowhere on the pages we fetched. And our customer list was stale: L&#x27;Oreal and Deloitte appear on no page we could fetch, while KPMG, Intuit, Mars, Uber, Vanguard, Salesforce, and Dropbox do.

The model story is real and checkable. Palmyra X6 shipped August 13, 2026 with published per-token pricing and a 1M context window, X4 is documented as deprecated on November 18, 2026, and the palmyra-mini and mini-thinking models were released as open weights under Apache 2.0 in September 2025. Benchmark claims on the marketing site (capability scores, cost per finished task) are the vendor&#x27;s own and the dev docs caveat that scores measure the model inside the combined system.

Governance claims are the ones to test in a pilot: voice profiles, terminology lists, and style guides are documented as enforced before review, and the trust page states plainly that customer data is not used to train models, with SOC 2 Type II, ISO 27001, 27701, and 42001, HIPAA and PCI badges, and an option to bring your own encryption keys.

## Verdict

A governed enterprise AI platform with its own models and a real compliance story; the writing tool inside it is now the smallest part, and the price tag is whatever sales says it is.

## Pros and cons

## Related concepts

- [AI content](/glossary/ai-content-generation/)
- [Agentic Marketing](/glossary/agentic-marketing/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Writer: Enterprise AI platform with Palmyra models, brand governance, and agents. Writer ships with AI content generation. This page documents 12 integrations. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Writer uses paid pricing, so the number depends on your volume and contract. Quote-based. Writer.com serves no public price table to anonymous visitors (verified Sep 2026). Our last verified read of the pricing model was 2026-09-25; the vendor&#x27;s pricing page carries the current quote criteria.

A governed enterprise AI platform with its own models and a real compliance story; the writing tool inside it is now the smallest part, and the price tag is whatever sales says it is.

The company says no. The plans page states that you retain full ownership of your data and that Writer takes a zero data retention approach and does not train or improve models on customer data by default, and the trust page repeats that data shared with Writer is not used to create, modify, or train models. Organization-wide data controls, including an automated deletion schedule, are documented, and enterprise buyers can request SOC 2 Type II and HIPAA reports and a BAA.

Starter is the self-serve tier: a 14-day free trial with no credit card, up to 5 users, the WRITER Agent interface, up to 5 Playbooks, 1 team Personality profile, basic connectors, and a limited Knowledge Graph. The comparison table caps scheduled routines at 3, active connectors at 3, and graph storage at 50 GB, and roles are limited to one team. No per-seat price is published on the page.

Published in the developer docs: Palmyra X6 at $2 per million input tokens and $8 per million output tokens with a 1M context window, Palmyra X5 at $0.60 and $6.00 with the same window, and Palmyra X4 at $2.50 and $10.00 with 128k context and a documented deprecation date of November 18, 2026. X5 is also available on Amazon Bedrock; the docs quote X6 at $0.12 of average cost per finished task.

## Similar Tools

## Related reading

- [Your Agents Are Only as Smart as Your Identity Debt](/blog/agents-identity-debt/)
- [Most of your marketing AI agents should be if/then](/blog/determinism-audit/)
- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
## Also featured in

- [Best AI Content &amp; Copywriting tools (2026): 8 compared](/best/ai-content-copywriting-tools/) &mdash; Enterprises that put brand governance ahead of raw output
- [Jasper vs Writer (2026): pricing, AI features, verdict](/vs/jasper-vs-writer/) &mdash; Pick Writer if you want a hosted platform the vendor runs for you, and ai content generation and knowledge graph grounding matters to your team.
### Quick Facts

Related guides: [Ai Content Copywriting Tools](/best/ai-content-copywriting-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/writer/#app",
    "name": "Writer",
    "description": "Enterprise AI platform with Palmyra models, brand governance, and agents",
    "image": "https://martechsignal.com/og/tools/writer.png",
    "url": "https://martechsignal.com/tools/writer/",
    "sameAs": [
      "https://writer.com"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/writer/",
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
        "name": "AI Content & Copywriting",
        "item": "https://martechsignal.com/categories/content-ai/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Writer",
        "item": "https://martechsignal.com/tools/writer/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Writer?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Writer: Enterprise AI platform with Palmyra models, brand governance, and agents. Writer ships with AI content generation. This page documents 12 integrations. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Writer cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Writer uses paid pricing, so the number depends on your volume and contract. Quote-based. Writer.com serves no public price table to anonymous visitors (verified Sep 2026). Our last verified read of the pricing model was 2026-09-25; the vendor's pricing page carries the current quote criteria."
        }
      },
      {
        "@type": "Question",
        "name": "Is Writer worth paying for in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A governed enterprise AI platform with its own models and a real compliance story; the writing tool inside it is now the smallest part, and the price tag is whatever sales says it is."
        }
      },
      {
        "@type": "Question",
        "name": "Does Writer train its models on my company's data?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The company says no. The plans page states that you retain full ownership of your data and that Writer takes a zero data retention approach and does not train or improve models on customer data by default, and the trust page repeats that data shared with Writer is not used to create, modify, or train models. Organization-wide data controls, including an automated deletion schedule, are documented, and enterprise buyers can request SOC 2 Type II and HIPAA reports and a BAA."
        }
      },
      {
        "@type": "Question",
        "name": "What is included in Writer's Starter plan and what are its limits?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Starter is the self-serve tier: a 14-day free trial with no credit card, up to 5 users, the WRITER Agent interface, up to 5 Playbooks, 1 team Personality profile, basic connectors, and a limited Knowledge Graph. The comparison table caps scheduled routines at 3, active connectors at 3, and graph storage at 50 GB, and roles are limited to one team. No per-seat price is published on the page."
        }
      },
      {
        "@type": "Question",
        "name": "How much do the Palmyra models cost via the API?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Published in the developer docs: Palmyra X6 at $2 per million input tokens and $8 per million output tokens with a 1M context window, Palmyra X5 at $0.60 and $6.00 with the same window, and Palmyra X4 at $2.50 and $10.00 with 128k context and a documented deprecation date of November 18, 2026. X5 is also available on Amazon Bedrock; the docs quote X6 at $0.12 of average cost per finished task."
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
    "reviewBody": "Writer is the enterprise content platform with its own Palmyra models and brand governance that legal teams can read. With no public prices, it competes on trust and procurement comfort.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/writer/#app",
      "name": "Writer",
      "url": "https://martechsignal.com/tools/writer/"
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

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
