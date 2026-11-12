---
title: "OpenAI can block your site from its agents, and your logs will never show it"
seo_title: "OpenAI can block your site from its agents, invisibly"
slug: openai-aura-silent-agent-block
date: 2026-11-05
author: MartechSignal
tags: [AI Search, OpenAI, SEO, Monitoring]
categories: [seo]
excerpt: "OpenAI's Aura site-safety check can stop agents from opening your site before any request reaches you. No 403, no referrer, nothing to grep. The differential test that catches it, and the evidence that gets a review."
seo_description: "The Aura site-safety check from OpenAI can keep ChatGPT from opening your pages with nothing in your logs. A differential test and the evidence pack."
---

An international media publisher did everything the AI visibility playbook asks. robots.txt fully open to OpenAI's crawlers. Clean infrastructure. This autumn it even ran a 24-hour OpenAI ad campaign to evaluate the channel. And since May 2026, ChatGPT has been unable to open a single one of its pages.

No 403 in the logs. No WAF events, no challenge pages, no referrer naming the agent. Nothing to grep, because nothing arrived. The refusal happens inside OpenAI's infrastructure, before a request is ever sent, and the publisher only noticed because staff kept getting the same vague error when they asked ChatGPT to read the company's own articles.

The account comes from Dan Taylor, an agency partner who advises the publisher and [documented the case at Search Engine Journal](https://searchenginejournal.com/openais-aura-safety-check-can-block-your-site-from-chatgpt-browsing/594322) on October 29. It is the best field manual yet for a failure mode almost nobody monitors for: your site silently excluded from OpenAI's agents, with zero evidence on your side of the connection.

## The check that runs before robots.txt ever matters

OpenAI decides whether its browsing tools may connect to a site at all, using a central safety layer its systems refer to as Aura. Taylor found the check visible in network traffic as a call to chatgpt.com/backend-api/aura/site_status. When the answer comes back "blocked," tools like ChatGPT's live fetch and Codex's Browser Use refuse to open the site, regardless of the user's local settings and regardless of robots.txt, and the client caches that refusal for 24 hours.

This layer is separate from the crawlers everyone already monitors. GPTBot, OAI-SearchBot and ChatGPT-User [publish their IPs](https://developers.openai.com/api/docs/bots) and follow standard web rules. Aura sits above them as a guard, and it fails closed where it counts: an explicit block holds even when a company administrator sets explicit allow rules, and it overrides the user's own permissions. (Network glitches during the status check itself default to allowing access, which tells you OpenAI knows the difference between "cannot verify" and "verified bad.")

What nobody outside OpenAI knows is what puts a domain on the list. Because the status check sends chat context along with the URL, Taylor reports that some researchers suspect prompt history itself can trip a site-wide label. Whatever the mechanism, the publisher in his account is a mainstream news brand, and OpenAI's own support teams could not initially say whether the block was even intentional.

## Why nothing you own will catch this

Your entire observability stack keys on requests that arrive. A block at your edge leaves footprints everywhere: a status code, a WAF event, a challenge in the security console. A block at OpenAI leaves absence, and absence does not trigger alerts. It does not even dent your crawl graphs, because the training and search crawlers keep visiting. In Taylor's case the publisher served about 5,000 successful requests to OpenAI's crawlers over 30 days while Google's bots logged 477,000 and Anthropic's 564,000. The graph looks thin but healthy. The browsing layer was dead the whole time.

This is the same shape as the [silent failures we audited in marketing automations](/blog/silent-failure-audit/): the system reports the state it can see, and the failure lives one layer up where no instrument looks. Your [analytics cannot see AI search properly](/blog/dashboard-cant-see-ai-search-5-layer-fix/) even when agents can reach you. When they cannot, the blind spot is total.

| Signal | Blocked at your edge | Blocked inside OpenAI |
|---|---|---|
| What the user sees | 403, challenge page, timeout | Generic agent error naming "site-safety policy" |
| Your access logs | The failed request, with UA and status | Nothing at the timestamp of the failed attempt |
| WAF / bot management console | A traceable event | No event |
| GPTBot, OAI-SearchBot, ChatGPT-User | Usually blocked by the same rule | Still fetching, still getting 2xx |
| The fix | Change your rule, minutes | OpenAI-side review; no self-service path exists |

## The differential test

The only reliable instrument is a test you run yourself, and Taylor's method is worth copying exactly.

Ask ChatGPT to open a specific URL, and try the same URL through other surfaces: the ChatGPT cloud browser, Codex Browser Use, Computer Use. A site-safety block shows up on several surfaces at once, because the decision is upstream of all of them. In the same session, ask for two competitor pages. Competitors load while your site refuses, and your logs show no inbound request at that moment. That combination, refusal on the client plus silence on the server, is the signature.

Then test the edges. Subdomains and deep article URLs stay blocked when the label is on the hostname. The clincher in Taylor's case: a third-party newspaper running the publisher's own technology, on a different domain, loaded fine. Same stack, different hostname, no block. That pins the classification to the domain and rules out anything in the site's own setup.

Before you escalate, rule out your own stack, because sometimes the block really is yours: WAF and bot-management rules, including Cloudflare's AI bot settings, geo-blocking, rate limits, robots.txt. And capture the exact error wording with a timestamp and timezone.

::: callout
**Error strings worth a screenshot.** "The site-safety policy blocks this action." "Browser use is not permitted on [domain]." "URL cannot be opened (non-retryable error)." Each names the platform's policy, not your server. Record the wording, the surface it appeared on, and when.
:::

## What makes a review request credible

There is no self-service page for Aura classifications, so the evidence pack does the work. Taylor's version: error screenshots with timestamps, the same-session competitor controls, log extracts showing zero inbound agent requests, crawler analytics showing OpenAI's bots still getting 2xx, and your robots.txt. Open a support case, keep every case number, and if more than one product is affected, say so in each case and ask for them to be linked. Ask three questions: does the domain carry a site-safety classification, which surfaces does it affect, and what is the process for review.

Two things not to do. Do not attempt workarounds; the agent is explicitly instructed not to circumvent the policy, and OpenAI's usage policies prohibit bypassing safety mitigations, so a creative redirect is the fastest way to turn a false positive into a justified one. And do not assume one clean test means it is over. Retest on a schedule and log the results, because you will want to know when it clears and whether it comes back.

## Size the problem honestly

When an agent cannot open your site, it does not wait. It moves to the next source, and in Taylor's testing the competitors loaded in the same chats where the publisher refused. Answers about a blocked brand get assembled from secondary coverage, forum threads and old articles, which is its own reputation problem. There is a bitter detail for anyone paying OpenAI for ads: an advertiser can buy placement in ChatGPT while the browsing agents are blocked from opening the advertiser's links.

The channel is small enough today that some teams will shrug. OpenAI's own consumer lead says ChatGPT sees [about a fifth as many search-like queries as Google](https://searchenginejournal.com/googles-search-volume-is-about-5x-chatgpts-openai-says/595817), while Ahrefs' October referral tracker put ChatGPT at 0.36% of traffic across 118,671 sites versus Google's 24.74%. But agent traffic is precisely the kind that never becomes a pageview, so referral share understates it, and [the agents are the checkout now](/blog/chatgpt-isnt-search-anymore-its-checkout/), not the doorway. A site that is merely uncited can still be [reached through community signals](/blog/link-building-wont-get-you-into-ai-answers/). A site an agent cannot open does not exist.

One more blind spot while you are checking: the AI visibility trackers in our [GEO and LLM optimization category](/categories/geo-llm-visibility/), tools like [Profound](/tools/profound/) and [OtterlyAI](/tools/otterlyai/), measure whether you get cited. None of them alert when an agent cannot fetch you at all. That test is yours to run, alongside the [AEO work](/blog/aeo-for-seo-what-changes-when-buyers-ask/) you are probably already doing.

::: verdict warn
**The verdict: you cannot detect an OpenAI-side block from your own logs, ever.** The block fires before a request leaves OpenAI, your crawlers keep returning 2xx, and no dashboard reports the absence. Put a recurring agent-fetch test of your five most important URLs next to your synthetic uptime checks, and treat the results as the evidence base for any review request. Five minutes a week beats explaining a dead AI channel a quarter later.
:::

Crawlable is not openable. Search engines went opaque with penalties once, then built webmaster tools so site owners could at least see the wall. OpenAI has not built that yet. Until it does, the only detector for this failure mode is a test you schedule yourself.
