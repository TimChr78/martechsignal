# Promptfoo review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [GEO & LLM Optimization](/categories/geo-llm-visibility/)
- Promptfoo
## Promptfoo review (2026): pricing, AI features, verdict

Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming

GEO & LLM Optimization · Freemium · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Promptfoo →](https://promptfoo.dev)

[How we review](/methodology/) · No affiliate links

[Visit Promptfoo →](https://promptfoo.dev)

## MartechSignal Score: 42/60

Promptfoo is the one in this category you can run tonight and read end to end: MIT evals and red teaming with tens of thousands of stars. The cloud tiers price quietly, which does not matter much when the core is free.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 6/10 | The open-source CLI is free and clear; cloud and enterprise tiers exist on promptfoo.dev with no public numbers extracted (the vendor pricing page, verified Sep 2026: [pricing page](https://www.promptfoo.dev/pricing/), verified 2026-09-28). |
| Feature depth | 7/10 | Model-graded evals, automated red team probe generation and multi-provider prompt runs make a real test bench (vendor documentation: [vendor site](https://promptfoo.dev), verified 2026-09-28). |
| Integrations | 6/10 | OpenAI, Anthropic, Azure OpenAI, Amazon Bedrock and GitHub Actions cover the evaluation pipeline (vendor documentation: [vendor site](https://promptfoo.dev), verified 2026-09-28). |
| AI capability | 8/10 | One LLM grading another's answers plus automated red team probe generation are meta-AI capabilities with real teeth (vendor documentation: [vendor site](https://promptfoo.dev), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with a CLI-first design you can run anywhere (the source repository: [repository](https://github.com/promptfoo/promptfoo), verified 2026-09-28). |
| Operational maturity | 6/10 | Plus a commercial entity behind the cloud tiers give it both community and runway (vendor documentation: [vendor site](https://promptfoo.dev), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Promptfoo is an open source LLM evaluation toolkit, used by developers to test prompts and models and by marketing teams to track brand answers in AI search. The core is a CLI and a TypeScript library, both MIT licensed. You define prompt sets, providers and grading rules in YAML, run everything in one command, and get a comparison of how each model answered each prompt. Outputs are scored with assertions: exact match, contains, regex, similarity, and model-graded checks where one model grades another's answer. Results open in a local web viewer. For generative engine optimization, Promptfoo is not a dedicated GEO dashboard and does not pretend to be one. What teams do is write a fixed set of buyer questions, run that set across ChatGPT, Perplexity and other models on a schedule, and grade whether their brand appears in each answer and what the answer claims. That yields prompt-level brand-answer tracking with developer tooling: versioned, repeatable and diffable between runs. There is no share-of-voice index or rank chart out of the box; tracking is only as good as the prompt set and grading rules you write. The second major mode is red teaming. The CLI generates attack probes against an application and reports findings. Guardrails, an MCP proxy, model security and code scanning are separate products on the cloud side, and the hosted red team product shows a 10k probes per month limit. Everything so far runs locally at no cost. Promptfoo's cloud adds team and enterprise features, and as of September 2026 the pricing page lists no public price numbers.

## AI Capabilities

- Model-graded evals where one LLM scores another's answers
- Automated red team probe generation against AI applications
- Prompt runs across ChatGPT, Perplexity and other models with side-by-side comparison
## Key Integrations

- OpenAI
- Anthropic
- Azure OpenAI
- Amazon Bedrock
- GitHub Actions
## Pricing

Promptfoo is freemium, with a free tier to start.

Free open-source CLI; cloud/enterprise tiers on promptfoo.dev, no public numbers extracted (Sep 2026)

Current plans and limits live on the [Promptfoo pricing page](https://www.promptfoo.dev/pricing/).

## Best for

Developer-led teams and technical marketers who want prompt-level brand-answer tracking, model comparisons and red teaming in one toolkit.

## Not for

Marketers who want a no-code GEO dashboard with rank tracking, share-of-voice charts and scheduled reports.

## Review notes

Promptfoo is a developer eval toolkit, and the workflow shows it. Prompt sets, providers and grading rules live in YAML. One command runs every prompt against every model and grades the outputs with assertions: exact match, contains, regex, similarity, and model-graded checks where a judge model scores the answer. Results open in a local web viewer where answers can be compared side by side.

The GEO use case is a repurposing rather than a packaged feature. A marketing team writes a fixed set of buyer questions, runs them across ChatGPT, Perplexity and other models on a schedule, and scores whether the brand appears in each answer and what the answer says. That is prompt-level brand-answer tracking built on the same primitives developers use for regression tests. It is not a dedicated GEO dashboard. There is no rank index or share-of-voice UI out of the box, and the tracking is only as good as the prompt set and grading rules you write. Assessed from vendor docs.

Red teaming is the other big mode. The CLI generates attack probes against an application and reports vulnerabilities. The hosted red team product shows a 10k probes per month limit, and guardrails, an MCP proxy, model security and code scanning sit as separate cloud products. The eval engine itself runs locally under the MIT license; the cloud at promptfoo.dev adds team and enterprise features with no public price numbers listed as of September 2026.

## Verdict

An eval framework that can double as GEO prompt tracking for teams willing to write YAML and grading rules. Not a substitute for a visibility dashboard.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ GEO tracking is assembled from eval primitives; no packaged GEO dashboard ships with it. |
| ✓ AI capabilities: model-graded evals where one LLM scores another's answers | ✗ The 10k probes per month limit shown for hosted red teaming constrains large attack suites. |
| ✓ Active public repository (25,631 GitHub stars counted at last check) | ✗ Cloud and enterprise pricing has no public numbers as of September 2026, so buyers end up in a sales conversation. |
| ✓ Native integrations include OpenAI, Anthropic, Azure OpenAI (5 listed) |  |
| ✓ MIT license with a large open-source repo, so the eval engine can run fully local. |  |
| ✓ One tool covers prompt evals, model comparison and red teaming. |  |
| ✓ Assertion-based grading makes brand-answer checks repeatable and diffable across runs. |  |

## Related concepts

- [GEO](/glossary/geo/)
- [AI Visibility](/glossary/ai-search-visibility/)
- [SEO](/glossary/seo/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Promptfoo?**
Promptfoo: Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming. Promptfoo ships with model-graded evals where one LLM scores another's answers. The public repository carries 25,631 stars.

**How much does Promptfoo cost?**
Promptfoo is open source - MIT licensed and free to self-host; the public repository carries 25,631 stars; native integrations cover OpenAI, Anthropic, Azure OpenAI. You pay in server time and maintenance, not licences.

**Is Promptfoo worth it past the free tier?**
An eval framework that can double as GEO prompt tracking for teams willing to write YAML and grading rules. Not a substitute for a visibility dashboard.

**Is Promptfoo free?**
The core is MIT licensed and free to run locally. Promptfoo also sells cloud and enterprise tiers at promptfoo.dev, which listed no public price numbers as of September 2026.

**Is Promptfoo a GEO tool?**
It is an LLM eval toolkit. Marketers use it for GEO-style work by running fixed question sets across ChatGPT, Perplexity and other models and scoring brand mentions in the answers, but it does not ship a dedicated GEO dashboard.

**What does red teaming include?**
The CLI generates attack probes against an application and reports findings. The hosted red team product shows a 10k probes per month limit.

## Similar Tools

- [Nightwatch](/tools/nightwatch/): Rank tracking across Google and AI answers, priced by keyword with unlimited seats
- [Profound](/tools/profound/): Enterprise AI marketing platform: answer-engine visibility plus drafting agents
- [OtterlyAI](/tools/otterlyai/): AI search monitoring for brand mentions and citations across ChatGPT and AI Overviews
- [Evertune](/tools/evertune/): GEO visibility measurement with content activation and a ChatGPT Ad Agent
- [Adobe LLM Optimizer](/tools/adobe-llm-optimizer/): Adobe's enterprise GEO system for AI visibility, CDN-edge fixes, and revenue attribution
## Related reading

- [ChatGPT Isn't Search Anymore, It's Checkout](/blog/chatgpt-isnt-search-anymore-its-checkout/)
- [SQREEM is betting the behavioral model beats the LLM: if it's right, your AI media budget bought the wrong thing](/blog/sqreem-behavioral-model-vs-llm/)
- [Open-Source Martech Stack vs $5K/mo Subscriptions](/blog/open-source-martech-stack/)
## Also featured in

- [Best AI SEO tools (2026): 8 compared](/best/ai-seo-tools/) — Best free entry point, provided someone on the team can run a CLI.
### Quick Facts

- **Pricing:** Freemium
- **Category:** [GEO & LLM Optimization](/categories/geo-llm-visibility/)
- **GitHub:** ★ 25631
- **API:** Yes
- **Repository checked:** 2026-10-02
- **Page updated:** 2026-09-25

Related guides: [Ai Seo Tools](/best/ai-seo-tools/)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

**Verdict:** Promptfoo is a tool in GEO & LLM Optimization with free and open source. The catalog documents 3 AI features, 5 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

Nightwatch

Rank tracking across Google and AI answers, priced by keyword with unlimited seats

Profound

Enterprise AI marketing platform: answer-engine visibility plus drafting agents

OtterlyAI

AI search monitoring for brand mentions and citations across ChatGPT and AI Overviews

Evertune

GEO visibility measurement with content activation and a ChatGPT Ad Agent

Adobe LLM Optimizer

Adobe's enterprise GEO system for AI visibility, CDN-edge fixes, and revenue attribution

[More GEO & LLM Optimization Tools →](/categories/geo-llm-visibility/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/promptfoo/#app",
    "name": "Promptfoo",
    "description": "Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming",
    "image": "https://martechsignal.com/og/tools/promptfoo.png",
    "url": "https://martechsignal.com/tools/promptfoo/",
    "sameAs": [
      "https://promptfoo.dev"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/promptfoo/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-10-02",
    "datePublished": "2026-09-25",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://www.promptfoo.dev/pricing/",
      "priceValidUntil": "2026-12-24"
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
        "name": "GEO & LLM Optimization",
        "item": "https://martechsignal.com/categories/geo-llm-visibility/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Promptfoo",
        "item": "https://martechsignal.com/tools/promptfoo/"
      }
    ],
    "@id": "https://martechsignal.com/tools/promptfoo/#breadcrumb"
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Promptfoo?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Promptfoo: Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming. Promptfoo ships with model-graded evals where one LLM scores another's answers. The public repository carries 25,631 stars."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Promptfoo cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Promptfoo is open source - MIT licensed and free to self-host; the public repository carries 25,631 stars; native integrations cover OpenAI, Anthropic, Azure OpenAI. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Promptfoo worth it past the free tier?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "An eval framework that can double as GEO prompt tracking for teams willing to write YAML and grading rules. Not a substitute for a visibility dashboard."
        }
      },
      {
        "@type": "Question",
        "name": "Is Promptfoo free?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The core is MIT licensed and free to run locally. Promptfoo also sells cloud and enterprise tiers at promptfoo.dev, which listed no public price numbers as of September 2026."
        }
      },
      {
        "@type": "Question",
        "name": "Is Promptfoo a GEO tool?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "It is an LLM eval toolkit. Marketers use it for GEO-style work by running fixed question sets across ChatGPT, Perplexity and other models and scoring brand mentions in the answers, but it does not ship a dedicated GEO dashboard."
        }
      },
      {
        "@type": "Question",
        "name": "What does red teaming include?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The CLI generates attack probes against an application and reports findings. The hosted red team product shows a 10k probes per month limit."
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
    "reviewBody": "Promptfoo is the one in this category you can run tonight and read end to end: MIT evals and red teaming with tens of thousands of stars. The cloud tiers price quietly, which does not matter much when the core is free.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/promptfoo/#app",
      "name": "Promptfoo",
      "url": "https://martechsignal.com/tools/promptfoo/"
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

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/tools/promptfoo/", "breadcrumb": {"@id": "https://martechsignal.com/tools/promptfoo/#breadcrumb"}, "dateModified": "2026-10-02"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "jobTitle": "Martech Product Owner", "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"], "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://www.linkedin.com/in/tchristensen78", "https://github.com/timchr78"]}, {"@type": "WebSite", "@id": "https://martechsignal.com/#website", "name": "MartechSignal", "url": "https://martechsignal.com/"}]}
```
