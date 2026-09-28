# Claude SEO benchmark: the living score tracker


| Date | Grader | Score | What it measured |
| --- | --- | --- | --- |
| Aug 24 | v2.2.4 | 83 | First full audit of our own production domain |
| Aug 26 | v2.2.5 | 61 | Same site, stricter gates, a 22-point drop |
| Aug 27 | v2.2.5 | 74.6 | One day of remediation, same grader |
| Sep 8 | v2.2.6 | 80 | Two more weeks of fixes, re-scored |
| Sep 18 | v2.3.1 | 76.6 | Four graders on one site, plus a 5/100 that mattered more |
| Sep 25-27 | v2.4.0 | 79.7, 79, 80, 80 | One run per remediation cycle; the latest breaks 92 technical / 82 content |

TC **[Tim Christensen](/authors/tim-christensen/)**

AI · SEO · 3 MIN

## Claude SEO benchmark: every score we have earned, and what each one measured

We make this: Claude SEO is MartechSignal's own free SEO audit skill. Coverage here is held to the same verification standard as third-party tools.

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Claude SEO benchmark: every score we have earned, and what each one measured

SEP 27, 2026 · Updated SEP 28, 2026

Filed under [SEO & Search](/categories/seo/)

Five grader generations have scored martechsignal.com since August. This page is the living record: every score, the grader that produced it, and the one thing each run actually measured. It replaces three earlier posts on the same thread, which now point here.

## The score timeline

Numbers only compare within a grader generation. The 22-point drop between Aug 24 and Aug 26 is not decay; it is v2.2.5 measuring surfaces v2.2.4 never looked at. Both audits were right about their own scope.

## What the first run caught that our pipeline missed

The headline was 83/100 with the damage concentrated in content and schema surfaces our own tests treated as green. The strangest receipt: the schema category score went down between two runs, from 90 to 88, while we were actively fixing it. The grader had widened its schema checks between versions. That pattern repeats so reliably that the score movement is now read as metadata about the grader before it is read as news about the site.

## The grader-parity lesson

v2.2.5 re-scored the same unchanged pages at 61 against a 92 the week before. The lesson that survived into our own audit tooling: scores are only comparable when the skill version and the model behind it are identical. We now pin both for every run, and the site's methodology page says so. If you run AI audit skills on your own properties, pin the grader or your trend line is fiction.

## The four-grader experiment

Five graders, one site, one week. The spread between the harshest and the most generous was wider than any single remediation cycle we have run. Underneath the spread sat one score that mattered more than any headline: a 5/100 on a single structural check that every other grader had waved through. Finding that check is the entire argument for running more than one grader. The disagreement is not noise; it is coverage.

## How to read this page

This is a living document. Each new remediation cycle adds a row with its date, grader version, and score, and the previous rows never move. The score is a mirror with a date stamp: useful for direction, useless as a verdict. The things worth copying are the fixes, not the numbers, and the three original write-ups now redirect here so the thread has one home.

## The receipts

The audit artifacts are archived with their raw finding tables, the site's [methodology](/methodology/) documents the verification rules these numbers live under, and the [corrections page](/corrections/) logs every published error we have made about them. For the pairwise questions this page deliberately does not answer, see [Claude SEO vs Semrush](/vs/claude-seo-vs-semrush/) and its siblings under [/vs/](/vs/).

This post is part of the hub for this topic: [ai seo tooling](/guides/ai-seo-tooling/).

## Related reading

- [Google Doesn't Need Your Site Anymore. You Taught It Everything It Knows.](/blog/google-doesnt-need-your-site-anymore-you-taught-it-everything-it-knows/)
- [Check outputs, not logs: the silent-failure audit](/blog/silent-failure-audit/)
- [The AI-search funnel map GA4 won't give you](/blog/ai-search-funnel-map-ga4-wont-give-you/)
## Related tools

- [Frase](/tools/frase/) - AI-powered SEO content platform for research, writing, and AI visibility tracking
- [MarketMuse](/tools/marketmuse/) - AI-powered content strategy and optimization platform for SEO content teams
- [Semrush](/tools/semrush/) - All-in-one SEO and digital marketing platform with AI-powered insights and tools
## Comparison guides

- [Best AI SEO tools (2026): 8 compared](/best/ai-seo-tools/)
- [Claude SEO vs Semrush (2026): pricing, AI features, verdict](/vs/claude-seo-vs-semrush/)
## Glossary terms

- [SEO](/glossary/seo/)
- [CDP](/glossary/cdp/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: [Ever Gauzy](/tools/ever-gauzy/)

**MartechSignal**, written by [Tim Christensen](/authors/tim-christensen/)


```json
{
  "@context": "https://schema.org",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelectors": [
      "h1",
      "article h2"
    ]
  },
  "@type": "BlogPosting",
  "headline": "Claude SEO benchmark: every score we have earned, and what each one measured",
  "description": "Five grader generations have scored martechsignal.com since August. This page is the living record: every score, the grader that produced it, and the one.",
  "author": {
    "@type": "Person",
    "name": "Tim Christensen",
    "url": "https://martechsignal.com/authors/tim-christensen/",
    "@id": "https://martechsignal.com/authors/tim-christensen/#person",
    "sameAs": [
      "https://www.linkedin.com/in/tchristensen78",
      "https://github.com/timchr78"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "@id": "https://martechsignal.com/#organization",
    "name": "MartechSignal",
    "url": "https://martechsignal.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://martechsignal.com/logo.png"
    }
  },
  "datePublished": "2026-09-27",
  "dateModified": "2026-09-28",
  "mainEntityOfPage": "https://martechsignal.com/blog/claude-seo-benchmark/",
  "image": {
    "@type": "ImageObject",
    "url": "https://martechsignal.com/og/claude-seo-benchmark.png",
    "width": 1200,
    "height": 630
  },
  "citation": [
    {
      "@type": "CreativeWork",
      "name": "Claude SEO skill repository",
      "url": "https://github.com/claude-seo/claude-seo"
    }
  ],
  "isPartOf": {
    "@type": "Blog",
    "@id": "https://martechsignal.com/blog/#blog"
  },
  "inLanguage": "en",
  "wordCount": 631,
  "articleSection": "seo"
}
```

```json
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
      "name": "Blog",
      "item": "https://martechsignal.com/blog/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Claude SEO benchmark: every score we have earned, and what each one measured",
      "item": "https://martechsignal.com/blog/claude-seo-benchmark/"
    }
  ]
}
```

```json
{"@context": "https://schema.org", "@graph": [{"@type": "Organization", "@id": "https://martechsignal.com/#organization", "name": "MartechSignal", "url": "https://martechsignal.com/", "logo": {"@type": "ImageObject", "@id": "https://martechsignal.com/#logo", "url": "https://martechsignal.com/logo.png"}, "sameAs": ["https://github.com/timchr78"]}, {"@type": "Person", "@id": "https://martechsignal.com/authors/tim-christensen/#person", "name": "Tim Christensen", "url": "https://martechsignal.com/authors/tim-christensen/", "image": "https://martechsignal.com/authors/tim-christensen/avatar.png", "worksFor": {"@id": "https://martechsignal.com/#organization"}, "sameAs": ["https://github.com/timchr78"]}]}
```
