---
title: "Your agent's price quote is a snapshot of a page you stopped updating"
seo_description: "An agent quoted a Kindle at its launch price years later, matching live prices on 2 of 15 products. Why grounding and caching decide if a quote is true."
seo_title: "Your Agent's Price Quote Is a Stale Snapshot"
slug: agent-price-quotes-are-stale-snapshots
date: 2026-11-06
author: MartechSignal
tags: [AI Agents, Data Grounding, Pricing, LLM]
categories: [geo-llm-visibility]
---
Ask an AI agent with no tools what a Kindle Paperwhite costs, and there is a good chance it answers $159.99. That was the launch price. When [Apify ran the check](https://blog.apify.com/llm-grounding-with-live-data) on November 3, the live price was $199.99. The model was not broken. It quoted a memory, the memory was years old, and nothing in the answer flagged the difference.

Apify turned that failure into a full grounding tutorial this month, and it is worth reading past the title, because the failure it documents is now a routine part of how agents answer questions about money. In their tests, GPT-6 Luna and Claude Opus 5.5, asked with no tools, each matched the live price for exactly 2 of 15 products. The median error was 12 percent for one model and 17 for the other. Both models also produced confident prices for products whose store page showed no price at all. A prompt begging them to answer UNKNOWN instead did work, technically: 21 of 21 answers came back UNKNOWN. A prompt alone buys you either a guess or nothing, with no setting in between.

## Search does not fix it

Turning on built-in web search raised the hit rate to 9 to 11 of 15 exact prices for GPT-6 Luna and 7 to 9 for Claude. Every run still contained wrong prices, and here is the part that should worry anyone shipping an agent: each wrong price arrived with a source link. In one answer, Claude quoted $629.99 for a Dyson V15 Detect whose live price was $899.99, and cited a Best Buy URL. The link opened a different vacuum, the V15 Detect Extra. Other bad citations went to price tracker sites and store search pages. A citation makes a wrong number more convincing, not more correct. Whatever reads that answer downstream, agent code or a human skimming, will trust the link.

## What grounding actually means

The fix Apify builds in the tutorial is called grounding, and the word has drifted into enough marketing that it is worth pinning down. In practice it is three commitments:

::: callout
Fetch at answer time. The agent answers only from data it fetched for this question, not from training memory and not from a page it read last week.

Cite the fetch, not just a URL. Every number carries where it came from and when it was checked.

Code writes the price. The model never types the number into the answer. It leaves a placeholder, and code that just fetched the price fills it in.
:::

That last part sounds fussy until you see the failure it prevents. A preprint titled ["Fabrication after tool failure"](https://arxiv.org/abs/2609.14758), shared before peer review, tested what models do when a tool hands back bad data. When the tool reported "ok" alongside empty or outdated results, up to 45.3 percent of answers hid the failure. When the tool returned a clear error instead, dishonest answers dropped to zero. For anything quoting prices, an honest "no price" is worth more than a plausible one, and the plumbing has to make honesty the easy path.

## We run this failure mode ourselves

MartechSignal maintains a directory of 174 active marketing tools, and price is the field we watch most closely, because it is the field agents read most and vendors change most. We recount the catalog as a hygiene check. The method, so you can repeat it: on November 6 we counted records in tools.json with status active (174), then those carrying a listed entry price (155), then those whose last edit is older than September 7, meaning no touch of any kind, price re-check included, in more than 60 days.

The count: 46 of 155 priced records, just under a third, sit in that window. All 46 are between 60 and 90 days old, and none are older, because a weekly re-verification job exists and eventually reaches everything. That is the honest finding. A deliberately maintained catalog with a pipeline whose entire job is price accuracy still carries a two month lagging tail.

Four of the paid ones:

<table class="cmp">
<tr><th>Tool</th><th>Listed at</th><th>Record last touched</th></tr>
<tr><td><a href="/tools/semrush/">Semrush</a></td><td>from $117/mo</td><td>August 28</td></tr>
<tr><td><a href="/tools/sendgrid/">Twilio SendGrid</a></td><td>from $19.95/mo</td><td>August 28</td></tr>
<tr><td><a href="/tools/surfer-seo/">Surfer SEO</a></td><td>from $49/mo</td><td>August 28</td></tr>
<tr><td><a href="/tools/hypotenuse-ai/">Hypotenuse AI</a></td><td>from $56/mo</td><td>August 28</td></tr>
</table>

Those figures are probably right. Semrush does not move its entry price every week. The point is what the record admits: each tool page shows the date it was last touched, on its face, so a reader or an agent can see the age of the number before trusting it. That is the whole difference between a record and a stale quote. The record knows how old it is.

## When caching turns into a stale quote

None of this says an agent must fetch every price on every question. Apify's own pipeline draws the line cleanly: one fetch is enough to fill a cache for an entire catalog, but a live answer gets its own fetch, per product, at answer time. Caching is legitimate while the answer carries the age of the data. Past that point the cache stops being an optimization, because the answer is hiding how old the number is, and that is the moment a cached price becomes a stale quote.

Prices move faster than most people assume. In the Apify tests, the AirPods Pro 3 at Best Buy went from $199.99 to $249.99 in the three days before the models were asked, so a price fetched the previous Tuesday could already be wrong by Friday. The useful question is not whether a number is fresh. It is whether the answer can tell you when it looked.

## How to spot a snapshot answer

The tells are consistent, and they apply to agents you build and agents you buy:

- No fetched-at time near the number. If the answer cannot say when it looked, it did not look.
- Identical prices across sessions or days. Live prices drift. Snapshots do not.
- Country, seller, or variant mismatches. Apify's scraper tests caught a US product served in Indian rupees and a used "other sellers" price standing in for the main offer. One store link redirected to a different bottle size, and the new page's price then answered for the original.
- Sources that are not the product page. Price trackers, search result pages, or a similar product mean the number came from somewhere other than where the answer claims.

## What we do about it, and what still drifts

The [methodology page](/methodology/) describes the machinery: a weekly job re-fetches vendor pricing pages, ranked by traffic and by how load-bearing the figure is, because hammering 155 vendor pages on a fixed schedule mostly gets you blocked. Vendors deny robots, paywall their pricing, or serve a different country's page, and the job's honest output is often "could not verify". That status ships with the record; the job never quietly swaps in the last known number.

We still drift, 46 records deep, and we can name exactly which 46, because the age is part of the data. An agent quoting a months-old crawl has no such list. That gap between a grounded answer and a confident one has nothing to do with model quality: a weaker model that fetched the price at answer time and told you when beats a stronger one reciting its training data with a straight face.
