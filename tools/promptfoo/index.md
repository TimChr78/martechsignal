# Promptfoo review (2026): pricing, AI features, verdict


| Pros | Cons |
| --- | --- |
| &#10003; MIT licence with free self-hosting | &#10007; GEO tracking is assembled from eval primitives; no packaged GEO dashboard ships with it. |
| &#10003; AI capabilities: model-graded evals where one LLM scores another&#x27;s answers | &#10007; The 10k probes per month limit shown for hosted red teaming constrains large attack suites. |
| &#10003; Established community (25,453 GitHub stars) | &#10007; Cloud and enterprise pricing has no public numbers as of September 2026, so buyers end up in a sales conversation. |
| &#10003; Native integrations include OpenAI, Anthropic, Azure OpenAI (5 listed) |  |
| &#10003; MIT license with a large open-source repo, so the eval engine can run fully local. |  |
| &#10003; One tool covers prompt evals, model comparison and red teaming. |  |
| &#10003; Assertion-based grading makes brand-answer checks repeatable and diffable across runs. |  |

**What is Promptfoo?**
Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming. It ships with model-graded evals where one LLM scores another&#x27;s answers, 25,453 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

**How much does Promptfoo cost?**
Promptfoo is open source - MIT licensed and free to self-host; the public repository carries 25,453 stars; native integrations cover OpenAI, Anthropic, Azure OpenAI. You pay in server time and maintenance, not licences.

**Is Promptfoo worth it past the free tier?**
An eval framework that can double as GEO prompt tracking for teams willing to write YAML and grading rules. Not a substitute for a visibility dashboard.

**Is Promptfoo free?**
The core is MIT licensed and free to run locally. Promptfoo also sells cloud and enterprise tiers at promptfoo.dev, which listed no public price numbers as of September 2026.

**Is Promptfoo a GEO tool?**
It is an LLM eval toolkit. Marketers use it for GEO-style work by running fixed question sets across ChatGPT, Perplexity and other models and scoring brand mentions in the answers, but it does not ship a dedicated GEO dashboard.

**What does red teaming include?**
The CLI generates attack probes against an application and reports findings. The hosted red team product shows a 10k probes per month limit.

- **Pricing:** Freemium
- **Category:** [GEO &amp; LLM Optimization](/categories/geo-llm-visibility/)
- **GitHub:** ★ 25453
- **API:** Yes
- **Last verified:** 2026-09-25

**Verdict:** Promptfoo is a tool in GEO &amp; LLM Optimization with free and open source. The catalog documents 3 AI features, 5 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-09-25. This is a desk review, not a hands-on test. Desk-reviewed

Nightwatch

Rank tracking across Google and AI answers, priced by keyword with unlimited seats

Profound

Enterprise AI marketing platform: answer-engine visibility plus drafting agents

OtterlyAI

AI search monitoring for brand mentions and citations across ChatGPT and AI Overviews

Evertune

GEO visibility measurement with content activation and a ChatGPT Ad Agent

Adobe LLM Optimizer

Adobe&#x27;s enterprise GEO system for AI visibility, CDN-edge fixes, and revenue attribution

[More GEO &amp; LLM Optimization Tools →](/categories/geo-llm-visibility/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [GEO &amp; LLM Optimization](/categories/geo-llm-visibility/)
- Promptfoo
## Promptfoo review (2026): pricing, AI features, verdict

Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming

GEO &amp; LLM Optimization · Freemium · OPEN SOURCE Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-09-25

[Visit Promptfoo &#8594;](https://promptfoo.dev)

[How we review](/methodology/) · No affiliate links

[Visit Promptfoo &#8594;](https://promptfoo.dev)

Not yet scored against the rubric; scored pages show six pillars.

## Overview

Promptfoo is an open source LLM evaluation toolkit, used by developers to test prompts and models and by marketing teams to track brand answers in AI search. The core is a CLI and a TypeScript library, both MIT licensed. You define prompt sets, providers and grading rules in YAML, run everything in one command, and get a comparison of how each model answered each prompt. Outputs are scored with assertions: exact match, contains, regex, similarity, and model-graded checks where one model grades another&#x27;s answer. Results open in a local web viewer. For generative engine optimization, Promptfoo is not a dedicated GEO dashboard and does not pretend to be one. What teams do is write a fixed set of buyer questions, run that set across ChatGPT, Perplexity and other models on a schedule, and grade whether their brand appears in each answer and what the answer claims. That yields prompt-level brand-answer tracking with developer tooling: versioned, repeatable and diffable between runs. There is no share-of-voice index or rank chart out of the box; tracking is only as good as the prompt set and grading rules you write. The second major mode is red teaming. The CLI generates attack probes against an application and reports findings. Guardrails, an MCP proxy, model security and code scanning are separate products on the cloud side, and the hosted red team product shows a 10k probes per month limit. Everything so far runs locally at no cost. Promptfoo&#x27;s cloud adds team and enterprise features, and as of September 2026 the pricing page lists no public price numbers.

## AI Capabilities

- Model-graded evals where one LLM scores another&#x27;s answers
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

## Related concepts

- [GEO](/glossary/geo/)
- [AI Visibility](/glossary/ai-search-visibility/)
- [SEO](/glossary/seo/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming. It ships with model-graded evals where one LLM scores another&#x27;s answers, 25,453 GitHub stars. MartechSignal&#x27;s review covers features, pricing, and how it compares to alternatives.

Promptfoo is open source - MIT licensed and free to self-host; the public repository carries 25,453 stars; native integrations cover OpenAI, Anthropic, Azure OpenAI. You pay in server time and maintenance, not licences.

An eval framework that can double as GEO prompt tracking for teams willing to write YAML and grading rules. Not a substitute for a visibility dashboard.

The core is MIT licensed and free to run locally. Promptfoo also sells cloud and enterprise tiers at promptfoo.dev, which listed no public price numbers as of September 2026.

It is an LLM eval toolkit. Marketers use it for GEO-style work by running fixed question sets across ChatGPT, Perplexity and other models and scoring brand mentions in the answers, but it does not ship a dedicated GEO dashboard.

The CLI generates attack probes against an application and reports findings. The hosted red team product shows a 10k probes per month limit.

## Similar Tools

## Related reading

- [ChatGPT Isn't Search Anymore, It's Checkout](/blog/chatgpt-isnt-search-anymore-its-checkout/)
- [Salesforce's third no-code promise, audited](/blog/salesforce-third-no-code-promise/)
- [Your Dashboard Can't See AI Search, Here's the 5-Layer Fix](/blog/dashboard-cant-see-ai-search-5-layer-fix/)
### Quick Facts

Related guides: [Ai Seo Tools](/best/ai-seo-tools)

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


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
    "dateModified": "2026-09-25",
    "datePublished": "2026-09-25",
    "offers": {
      "@type": "Offer",
      "price": 0,
      "priceCurrency": "USD",
      "url": "https://www.promptfoo.dev/pricing/",
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
        "name": "GEO & LLM Optimization",
        "item": "https://martechsignal.com/categories/geo-llm-visibility/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Promptfoo",
        "item": "https://martechsignal.com/tools/promptfoo/"
      }
    ]
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
          "text": "Open source LLM eval toolkit for prompt testing, brand-answer tracking and red teaming. It ships with model-graded evals where one LLM scores another's answers, 25,453 GitHub stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Promptfoo cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Promptfoo is open source - MIT licensed and free to self-host; the public repository carries 25,453 stars; native integrations cover OpenAI, Anthropic, Azure OpenAI. You pay in server time and maintenance, not licences."
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
  }
]
```
