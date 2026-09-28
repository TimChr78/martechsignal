# Tim Christensen

[TOOLS](/tools/) [BLOG](/blog/) [GLOSSARY](/glossary/) [CHECKLIST](/checklist/) [ABOUT](/about/)

## Tim Christensen

Writer and reviewer behind MartechSignal

## What this site is

MartechSignal is an independent review and teardown of AI marketing automation tools. I read the documentation, the pricing pages, and the source, and write up what the marketing rarely says: what the tool actually does, what it costs, and where it falls short. No sponsored rankings, no affiliate links, no paid placement. The pages carry dates because the facts move. When a number goes stale past its window, the page says so until someone checks it again.

## Background

I work as a martech product owner at a Nordic insurer, which means the reviews here come from running marketing technology in production rather than writing about it from a distance. The day job shapes the questions: does this tool hold up at scale, does the pricing survive contact with a real renewal, can our team operate it without a dedicated specialist.

## How I test

Each tool page starts with the vendor's own documentation, source repository, and pricing pages. Hands-on checks happen only where a page says so on its face, with the exact method stated next to the claim. Where a tool needs credentials I do not have, the review says so instead of guessing. Every page carries the date it was last verified.

## Reading the badges

Three labels do most of the honesty work on this site. The desk-research badge means the page was assembled from documentation, source, and pricing pages with dated sources, not from a login. The verification date on a tool page tells you when its numbers were last checked at the source. The hands-on block, where one exists, names the environment and the method so the claim can be repeated. If a page carries none of those, read its numbers as vendor claims and check them yourself before signing anything.

The goal is simple: every claim here should carry a date or a source, and the pages that fail that test get fixed rather than defended.

## Verification log

Short, dated, and checkable:

- **2026-09-27:** pricing re-checked at the source for ActiveCampaign, Adobe Marketo, HubSpot, n8n, and claude-seo. Three corrections landed: a missing Marketo package, HubSpot annual rates, and n8n's billing currency.
- **2026-09-26 to 2026-09-27:** claude-seo run repeatedly against martechsignal.com itself. A 170-page audit surfaced 96 findings in about five minutes at roughly six dollars of API tokens per run. The method and numbers are on the tool page and in the benchmark post.
Pages with hands-on claims say so on their face and name the method. Everything else in the directory is desk research, and the badge says that too.

## How this site is built

The directory is generated from structured catalog records rather than typed page by page, which is why the same fields show up in the same order everywhere: pricing model, real entry cost, integrations, licence, verification date. Comparisons pull the same numbers, so a source check that changes a record changes every page quoting it in the same build. The pages carry machine-readable twins as well, because agents read review sites too.

## Contact

Found an error or a tool that deserves a teardown? Open an issue on the [site repository](https://github.com/timchr78/martechsignal) or connect on [LinkedIn](https://www.linkedin.com/in/tchristensen78).

### About

MartechSignal lives on [an explicit editorial policy](/about/): independent, no sponsorships, verified dates on every page.

## Why the day job stays unnamed

I do martech product ownership for an employer this site will never name. Naming the company would make every review read like vendor advocacy or internal politics. The arrangement is strict: the employer has no stake, no say, and no sight line into what gets published here. When a tool I have used at work shows up in the directory, the write-up is still desk research with dated sources, and the desk-review badge says so.

Bylined on [40 posts](/blog/) so far, and every tool page in the directory carries the verification date behind its numbers. The research rules are public on the [methodology](/methodology/) page, including the source-claim rule.


```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
      "description": "Tim Christensen researches and writes the AI marketing tool catalog at MartechSignal: tool pages, pricing verification, comparisons, and the methodology behind them.",
    "@id": "https://martechsignal.com/authors/tim-christensen/#person",
    "name": "Tim Christensen",
    "url": "https://martechsignal.com/authors/tim-christensen/",
    "jobTitle": "Martech Product Owner",
  "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "knowsAbout": ["martech tools", "marketing automation", "AI search visibility", "workflow automation", "open-source marketing software"],
  "worksFor": {"@id": "https://martechsignal.com/#organization"},
    "sameAs": [
      "https://www.linkedin.com/in/tchristensen78",
      "https://github.com/timchr78"
    ]
  }
}
```

```json
{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://martechsignal.com/"}, {"@type": "ListItem", "position": 2, "name": "Authors", "item": "https://martechsignal.com/authors/"}, {"@type": "ListItem", "position": 3, "name": "Tim Christensen", "item": "https://martechsignal.com/authors/tim-christensen/"}]}
```

```json
{"@context": "https://schema.org", "@type": "WebPage", "@id": "https://martechsignal.com/authors/tim-christensen/#webpage", "dateModified": "2026-09-27"}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
