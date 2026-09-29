# Potato review (2026): pricing, AI features, verdict


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 9/10 | Free under MIT, 100% local with a $0 mock mode; real runs use your own Anthropic key, stated plainly (the vendor pricing page: [vendor site](https://github.com/onism1767-creator/potato), verified 2026-08-31). |
| Feature depth | 4/10 | Mention coverage, citation validity and owned-versus-earned citation splits cover one measurement loop (vendor documentation: [vendor site](https://github.com/onism1767-creator/potato), verified 2026-09-28). |
| Integrations | 3/10 | Anthropic Claude and a CLI with a local GUI wizard documented (vendor documentation: [vendor site](https://github.com/onism1767-creator/potato), verified 2026-09-28). |
| AI capability | 5/10 | Measuring Claude's web-search answers with citation validity checks is applied AI measurement (vendor documentation: [vendor site](https://github.com/onism1767-creator/potato), verified 2026-09-28). |
| Openness | 9/10 | MIT-licensed with 168 GitHub stars and fully local execution (the source repository: [repository](https://github.com/onism1767-creator/potato), verified 2026-09-28). |
| Operational maturity | 2/10 | Founded 2026 at 168 stars as a focused local tool (vendor documentation: [vendor site](https://github.com/onism1767-creator/potato), verified 2026-09-28). |


| Pros | Cons |
| --- | --- |
| ✓ MIT licence with free self-hosting | ✗ Young project (168 GitHub stars) - smaller community and plugin ecosystem |
| ✓ AI capabilities: measures brand mention coverage in Claude web-search answers |  |
| ✓ Native integrations include Anthropic Claude, CLI, Local GUI wizard (3 listed) |  |

**What is Potato?**
Potato: Free local tool that measures brand mentions and citations in Claude's web-search answers. Potato ships with measures brand mention coverage in Claude web-search answers. The public repository carries 168 stars. MartechSignal's review covers features, pricing, and how it compares to alternatives.

**How much does Potato cost?**
Potato is open source - MIT licensed and free to self-host; the public repository carries 168 stars; native integrations cover Anthropic Claude, CLI, Local GUI wizard. You pay in server time and maintenance, not licences.

**Is Potato a good self-hosted SEO & Search tool in 2026?**
The most methodologically honest AI-visibility tool in this directory: scoped claims, deterministic scoring, cost-capped runs, and a reproducible method. Use it to track your Claude-answer presence over time; do not mistake it for a full AI-search measurement.

- **Pricing:** Open Source
- **Category:** [SEO & Search](/categories/seo/)
- **GitHub:** ★ 168
- **Founded:** 2026
- **API:** Yes
- **Last verified:** 2026-08-31

**Verdict:** Potato is a tool in SEO & Search with free and open source. The catalog documents 5 AI features, 3 integrations, a public API and a self-hosting path. We reviewed it from vendor documentation on 2026-08-31. This is a desk review, not a hands-on test. Desk-reviewed

OtterlyAI

AI search monitoring for brand mentions and citations across ChatGPT and AI Overviews

Nightwatch

Rank tracking across Google and AI answers, priced by keyword with unlimited seats

Ahrefs

Brand Radar tracks brand mentions and citations across AI answers, YouTube and Reddit

Nimt.ai

AI search tracking across 8 models with an agent that writes, fixes, and outreaches

[More SEO & Search Tools →](/categories/seo/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)

- [Home](/)
- [Tools](/tools/)
- [SEO & Search](/categories/seo/)
- Potato
Re-check pending: pricing last verified 2026-08-31 (29 days ago).

KIND: Utility (not an end-to-end platform)

## Potato review (2026): pricing, AI features, verdict

Free local tool that measures brand mentions and citations in Claude's web-search answers

SEO & Search · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/) · updated 2026-08-31

[Visit Potato →](https://github.com/onism1767-creator/potato)

[How we review](/methodology/) · No affiliate links

[Visit Potato →](https://github.com/onism1767-creator/potato)

## MartechSignal Score: 32/60

Potato measures one thing locally: whether Claude's web-search answers mention and cite your brand, with link-rot checking. MIT and 168 stars; the $0 mock mode makes it testable before you spend a cent.

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Potato measures how visible your brand is inside Claude's web-search answers, which is a specific corner of the AI search optimization (GEO) problem. It asks Claude a fixed set of frozen questions, collects every brand mention and source citation in the answers, and scores them with deterministic rules. No AI judge, no guesswork. Every number in the report carries a confidence interval, and the whole thing runs locally so results are reproducible and auditable. The output is a single-file offline HTML report covering mention coverage, citation validity, and the split between citations from your own domain versus third-party pages. The report is honest about its limits: it measures one engine, Claude, under one exact configuration, and it says so in the output. It is a proxy measurement, not a ranking truth detector. A free mock preview mode runs with no API key so you can see the report shape before spending anything. Setup is the friendliest of any tool in this batch. Windows users download a portable zip and double-click a batch file. Developers can pip install the package and run the CLI or the local GUI wizard. Real runs against Claude need your own Anthropic API key, which is also the only cost. The closest directory entry is Claude SEO, which audits your whole site for citability. Potato is narrower and complementary: it measures what Claude actually says about you today, repeatedly, so you can track whether fixes move the numbers. It fits brands that care specifically about Claude citations, analysts who want reproducible measurement, and teams that refuse to send brand data to a third-party monitoring SaaS. If you need cross-engine coverage of ChatGPT, Gemini, and Perplexity too, the commercial AI visibility platforms in this category are the broader option.

Potato homepage, captured September 2026. Vendor page shown as a dated reference capture; all site content belongs to its owner.

## AI Capabilities

- Measures brand mention coverage in Claude web-search answers
- Citation validity checking (are cited links reachable)
- Owned vs earned citation split
- Deterministic scoring with confidence intervals, no AI judge
- Offline single-file HTML report
## Key Integrations

- Anthropic Claude
- CLI
- Local GUI wizard
## Pricing

Potato is free to self-host under the MIT licence.

Free, MIT-licensed. Runs 100% locally. $0 mock preview mode; real Claude runs use your own Anthropic API key.

## Review notes

Researched from public documentation, the source repository, and vendor materials. Not a hands-on test.

The README's own framing is refreshingly honest: not a crawler, not an AI-ranking truth detector, a reproducible proxy measurement of how visible your brand is inside Claude's web-search answers, with a fixed set of frozen questions, deterministic scoring rules, no AI judge, and confidence intervals on every number. Distribution is unusually accessible: a Windows zip with no Python needed, plus a standard Python install for everyone else. 254 passing tests are claimed in the repo. Everything here comes from the repository documentation.

The cost model is clean: the tool is MIT with zero author fees, a free mock preview needs no API key, and real runs use your own Anthropic key, hard-capped to a budget you set, typically around $5 or less on the Haiku tier, with the estimate shown before it starts. Security posture is documented concretely: runs on 127.0.0.1, the key stays in memory, zero telemetry. The limitation is scope: it measures Claude answers only, under a fixed question set, so treat results as one engine's proxy signal rather than an industry-wide AI-visibility metric.

## Verdict

The most methodologically honest AI-visibility tool in this directory: scoped claims, deterministic scoring, cost-capped runs, and a reproducible method. Use it to track your Claude-answer presence over time; do not mistake it for a full AI-search measurement.

## Pros and cons

## Related concepts

- [SEO](/glossary/seo/)
- [AEO](/glossary/aeo/)
- [AI Visibility](/glossary/ai-search-visibility/)
- [UTM parameters](/glossary/utm-parameters/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

Potato: Free local tool that measures brand mentions and citations in Claude's web-search answers. Potato ships with measures brand mention coverage in Claude web-search answers. The public repository carries 168 stars. MartechSignal's review covers features, pricing, and how it compares to alternatives.

Potato is open source - MIT licensed and free to self-host; the public repository carries 168 stars; native integrations cover Anthropic Claude, CLI, Local GUI wizard. You pay in server time and maintenance, not licences.

The most methodologically honest AI-visibility tool in this directory: scoped claims, deterministic scoring, cost-capped runs, and a reproducible method. Use it to track your Claude-answer presence over time; do not mistake it for a full AI-search measurement.

## Similar Tools

## Related reading

- [Claude SEO vs Seonaut: which free SEO checker should you run](/blog/claude-seo-vs-seonaut/)
- [Your insertion orders were written for humans: the IAB's agentic buying rules land before your ad stack can honor them](/blog/iab-agentic-buying-rules-insertion-orders/)
- [Two ways to buy the same workflow debt: task-metered and operations-metered](/blog/zapier-vs-make-two-ways-to-buy-the-same-workflow-debt/)
### Quick Facts

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION


```json
[
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "@id": "https://martechsignal.com/tools/potato-ai-visibility/#app",
    "name": "Potato",
    "description": "Free local tool that measures brand mentions and citations in Claude's web-search answers",
    "image": "https://martechsignal.com/og/tools/potato-ai-visibility.png",
    "url": "https://martechsignal.com/tools/potato-ai-visibility/",
    "sameAs": [
      "https://github.com/onism1767-creator/potato"
    ],
    "mainEntityOfPage": "https://martechsignal.com/tools/potato-ai-visibility/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "dateModified": "2026-09-27",
    "datePublished": "2026-08-31"
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
        "name": "SEO & Search",
        "item": "https://martechsignal.com/categories/seo/"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "Potato",
        "item": "https://martechsignal.com/tools/potato-ai-visibility/"
      }
    ]
  },
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is Potato?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Potato: Free local tool that measures brand mentions and citations in Claude's web-search answers. Potato ships with measures brand mention coverage in Claude web-search answers. The public repository carries 168 stars. MartechSignal's review covers features, pricing, and how it compares to alternatives."
        }
      },
      {
        "@type": "Question",
        "name": "How much does Potato cost?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Potato is open source - MIT licensed and free to self-host; the public repository carries 168 stars; native integrations cover Anthropic Claude, CLI, Local GUI wizard. You pay in server time and maintenance, not licences."
        }
      },
      {
        "@type": "Question",
        "name": "Is Potato a good self-hosted SEO & Search tool in 2026?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The most methodologically honest AI-visibility tool in this directory: scoped claims, deterministic scoring, cost-capped runs, and a reproducible method. Use it to track your Claude-answer presence over time; do not mistake it for a full AI-search measurement."
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
    "reviewBody": "Potato measures one thing locally: whether Claude's web-search answers mention and cite your brand, with link-rot checking. MIT and 168 stars; the $0 mock mode makes it testable before you spend a cent.",
    "itemReviewed": {
      "@type": "SoftwareApplication",
      "@id": "https://martechsignal.com/tools/potato-ai-visibility/#app",
      "name": "Potato",
      "url": "https://martechsignal.com/tools/potato-ai-visibility/"
    },
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": 32,
      "bestRating": 60,
      "worstRating": 0
    }
  }
]
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
