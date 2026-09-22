---
title: "AI visibility advice, audited against 775 logged citations"
seo_title: "AI visibility advice, audited against 775 logged citations"
slug: geo-experiments-vs-ai-visibility-playbook
date: 2026-09-22
author: Tim Christensen
tags: [AI Search, SEO, Automation]
categories: [seo]
---

775 logged AI citations just dismantled the standard GEO playbook. Two experiments, six AI platforms, months of hand-logged queries and no dashboards. The AI-visibility industry sells you a tool that counts how often ChatGPT mentions your brand. These results contradict what that count implies in three places, and confirm one part of the playbook that most people skip. The [full write-up is here](https://searchengineland.com/geo-experiments-challenge-conventional-ai-visibility-advice-488342); this is the ops audit.

## What was actually measured

Zeeshan Yaseen, an SEO consultant who runs a link-building agency, documented two back-to-back tests. The first, the "consultant test," tracked 15 commercial-intent keywords for an existing client brand across ChatGPT, Claude, Gemini, and Perplexity over several months, running every query manually with and without a VPN. Peak keyword presence hit 37.01% on April 29. Citations by platform: ChatGPT 148, Claude 96, Gemini 87, Perplexity 64.

The second, the "cold start test," ran the whole playbook from zero for a SaaS link-building agency with no measurable AI presence at baseline. Thirty days, May 30 to June 28, six platforms (adding Google AI Mode and Grok), 298 appearances from a standing start. Gemini led with 104, Google AI Mode followed with 95, ChatGPT managed 32.

Neither test used an API or a monitoring vendor. A human typed the queries and logged the citations. That is both the methodology's weakness and its credibility: nobody optimizing for a dashboard score would bother.

## Contradiction one: your own content is the weakest lever

The default GEO advice is to publish comprehensive owned resources and wait for the models to cite them. The cold-start data says the opposite. Of 437 source mentions, third-party listicles generated 85.8%. The brand's own listicle generated 14.0%. PR generated 0.2%.

Worse for the publish-and-pray crowd: the owned listicle was the slowest source in the entire test to get cited. Eighteen days, while two third-party placements were picked up overnight. In the consultant test, the same pattern showed up at scale. One comprehensive listicle on Indeed SEO, a site the models were already citing before anyone pitched it, generated 190 mentions, more than every other placement combined.

Yaseen revised his own conclusion on the record, which is rare in this industry: after experiment one he recommended owned listicles; after experiment two he calls them "a foundation, not a growth engine." The growth came from earning mentions on the small set of sources the models already trust for your category. He built his outreach list by logging which sources actually got cited for his 15 keywords, not by sorting prospects by domain rating. Five of eight targets landed in the final citation mix.

## Contradiction two: citations are rented, not owned

Here is the number that should worry anyone treating an AI citation like a page-one ranking: roughly half of all citing sources stopped being cited within 30 days. In both experiments.

One MEXC placement fell from 29 mentions to 11 week over week. A consistently cited listicle declined with no intervention at all. A page-one Google ranking can hold for years. An AI citation holds for weeks, and the model re-decides constantly.

This changes the budget math. A GEO program is not a set of placements you buy once; it is a subscription you keep paying, in outreach and maintenance, for as long as you want the visibility. Anyone quoting you a one-time "AI visibility package" is selling you an asset that depreciates in a month.

## Contradiction three: the citation count is not the outcome

This one connects directly to [the AI-search funnel map we built earlier this month](/blog/ai-search-funnel-map-ga4-wont-give-you/). The experiments logged citations and referral traffic separately, and the two lists barely overlap. Indie Hackers produced the most citations of any source and flat referral traffic. TechBullion produced fewer citations and grew sessions from 1 to 64. One low-volume Perplexity referral became a paying customer, on the platform with the fewest appearances in the entire test.

Across the 30-day window, 18.5% of new users arrived via referral traffic and another 3.25% through GA4's AI Assistant channel. Just over one fifth of new users, from a brand that did not exist in AI answers 30 days earlier. That is the number a CFO cares about. The citation count on your Semrush or Peec dashboard is, at best, a leading indicator of it, and these logs show how loose that leading indicator is.

## The finding that confirms the weird part of the playbook

Not everything inverted. Both tests found that the entities around your mention matter as much as the mention. In experiment one, a listicle that placed the brand alongside Lily Ray and Aleyda Solis performed well; when those names were removed, performance declined within days. In experiment two, the mirror image: updating the owned listicle on June 23 to include named competitors instead of promoting the brand alone lifted that source's mentions from 4 to 49, a 12.25x jump, with the same domain, author, and keyword target.

Comparative content beat advocacy content in both directions. The models appear to evaluate the whole neighborhood around a mention, not the mention in isolation. If you take one tactical thing from this article, take that: the page that ranks you next to your competitors out-cites the page that pretends you have none. It is also the finding that most damages the "publish more owned content" industry, because comparative content you control is precisely the content competitors can get you removed from or bury with their own updates.

## Now audit the audits

Before you reallocate budget on this, the honest caveats. The researcher runs an agency that sells link building and AI visibility work, so "earned placements beat owned content" is a conclusion his business model enjoys. Sample size is one brand per experiment, two niches, manual queries with no control group, and the platforms changed underneath both tests mid-flight. The 12.25x comparative-content jump comes from a single edit on a single page. The capitalization finding (capitalized vs lowercase queries returning different citations) failed replication three times and the author himself flags it as unvalidated.

None of that makes the data worthless. It makes it directional. Directional is still better than what the advice industry sells, which is theory and screenshots.

## What changes Monday morning

1. Build your outreach list from observed citations. Run your 15 commercial keywords through ChatGPT, Gemini, Claude, Perplexity, and AI Mode, log every source, rank by frequency, pitch that list. Ignore DR-sorted prospect spreadsheets.
2. Split your content budget toward earned placements. The agency covering these results moved 25-30% of client content budget from net-new owned posts to guest contributions and third-party comparison mentions.
3. Track citations monthly at minimum, expecting decay. Half your citing sources will be gone in 30 days. Treat it like rank tracking, not like a quarterly audit. The measurement layers in [our 5-layer dashboard fix](/blog/dashboard-cant-see-ai-search-5-layer-fix/) apply here unchanged: segment the AI referrals, treat counts as a floor, and reconcile against revenue, not citations.
4. Report referral sessions and pipeline, never citation volume, to whoever signs the checks. One Perplexity referral beat a thousand Indie Hackers mentions in the only currency that matters.

The AI-visibility dashboards will keep selling the count, because the count goes up when you do what they recommend. These logs suggest the count is the least interesting number in the room.
