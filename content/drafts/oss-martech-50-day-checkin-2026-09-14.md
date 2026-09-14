---
title: "Fifty days of open-source MarTech, audited"
seo_title: "Fifty days of open-source MarTech, audited"
slug: oss-martech-50-day-checkin
date: 2026-09-14
author: Tim Christensen
tags: [Open Source, MarTech]
categories: [open-source, workflow-automation]
---
Fifty days after [the open-source MarTech stack](/blog/open-source-martech-stack/) piece, this is the first re-check: what shipped, what stalled, and where the energy went.

The original argument was that every layer of a marketing stack, from automation to analytics to CRM, now has a self-hosted option good enough to run production work on. The reasonable response to that piece is the one I have been testing since. Stacks age. Tools stall. Maintainers burn out. So for the last 50 days (July 26 to September 14) I have been taking daily snapshots of the GitHub repos behind that piece, and this is the full check: fifty days of releases, pushes, and star movement across everything we track.

The short version: nothing stalled. The automation layer shipped at a pace SaaS vendors rarely match, the CRM category turned into the most crowded shelf in open source, Matomo tagged its first 6.0 beta of the 5.x era, and agent tooling started growing its own supply chain. Stars only corroborate what follows; the releases are the story.

::: callout
Release counts come from the GitHub releases API between July 26 and September 14, 2026. Star figures come from our own daily snapshots, which begin on August 25, so star movement covers the final 21 days of the window. That is too short for trend claims, so stars appear here only as corroboration of something already visible in the release log.
:::

## The window at a glance

<table class="cmp">
<tr><th>Project</th><th>Releases since Jul 26</th><th>The notable one</th></tr>
<tr><td><a href="/tools/n8n/">n8n</a></td><td class="oss-price">41</td><td>Crossed 200,000 stars; 2.39 line</td></tr>
<tr><td><a href="/tools/ghost/">Ghost</a></td><td class="oss-price">11</td><td>v6.63.0, Node 24 support</td></tr>
<tr><td><a href="/tools/strapi/">Strapi</a></td><td class="oss-price">7</td><td>v5.53.0</td></tr>
<tr><td><a href="/tools/twenty/">Twenty</a></td><td class="oss-price">~10</td><td>v2.39.0, workflow error handling</td></tr>
<tr><td><a href="/tools/frappe-crm/">Frappe CRM</a></td><td class="oss-price">6</td><td>v1.83.0</td></tr>
<tr><td><a href="/tools/chatwoot/">Chatwoot</a></td><td class="oss-price">3</td><td>v4.17.0, WhatsApp deep-dive</td></tr>
<tr><td><a href="/tools/mautic/">Mautic</a></td><td class="oss-price">1</td><td>7.2.0 Lynx Edition</td></tr>
<tr><td><a href="/tools/matomo/">Matomo</a></td><td class="oss-price">1 beta</td><td>6.0.0-b1, first major since 5.0</td></tr>
</table>

## The CRM shelf got crowded

If one category defined the window, it was CRM. [Mautic](/tools/mautic/) shipped 7.2.0 "Lynx Edition" on September 2, and the changelog reads like a team that has been listening to campaign builders: an infinite canvas in the campaign builder, spacebar-drag for moving around it, and the ability to stop a campaign from sending past a chosen date and time. They are small features aimed at real operator pain. Mautic remains the closest thing open source has to a marketing automation suite with CRM built in.

[Twenty](/tools/twenty/), which bills itself on GitHub as "the open alternative to Salesforce, designed for AI", cut roughly ten tagged releases in the window and closed it on v2.39.0. It added 1,190 stars in the final 21 days, the largest gain of anything we track outside the automation repos. [Frappe CRM](/tools/frappe-crm/) shipped six releases, v1.80.0 through v1.83.0, and passed 3,500 stars on the way.

Then there is the bottom of the market, which is where the energy sits. [WACRM](/tools/wacrm/), a self-hosted CRM template for WhatsApp with a shared inbox, contacts, and sales pipelines, went from a first commit in April to roughly 2,300 stars by mid-September. Cordys CRM, an AI-first CRM from the team behind the 1Panel hosting panel, crossed 2,700 stars with private deployment as the headline feature. Ten of the thirteen CRM and ERP-adjacent repos we track pushed code in the window's final week alone.

That last number is the tell. In July, Twenty was a proof-of-scale mention at 53,000 stars. Fifty days later it is the flag bearer of a contested category with entrants attacking from every direction: WhatsApp-first, AI-first, suite-first. Nobody has consolidated the shelf, which is why it deserves a shortlist instead of a default.

## Matomo finally moved

The analytics layer supplied the quiet surprise. Matomo tagged 6.0.0-b1 on September 7, its first major version since 5.0 arrived in December 2023, and pushed 5.14 alphas almost daily around it. Major versions on analytics infrastructure rarely make headlines, but they matter more than feature posts. A 6.0 means schema changes, extension authors retesting their plugins, and an upgrade path that self-hosters need to plan for. Anyone running [Matomo](/tools/matomo/) on their own hardware should read the beta notes before the stable release lands, not after.

The rest of the analytics pack moved too. [Umami](/tools/umami/) shipped v3.3.0 and v3.3.1 in August. [Plausible](/tools/plausible/) cut no release in fifty days and still added around 300 stars, a reminder that in this layer an empty release log is not the same as a dead project. The contrast with SaaS analytics, where the pricing page changes quarterly and the changelog is a marketing page, keeps getting harder to ignore.

## n8n treats shipping as a habit

[n8n](/tools/n8n/) published 41 releases between July 26 and September 14, closing the window on the 2.39 line. It crossed 200,000 GitHub stars somewhere between our July post (198,000) and the first snapshot on August 25. Per-release notes are mostly fixes, and that is the point. Forty-one releases in fifty days is a cadence, and cadence is what your deployment inherits: bug fixes for the nodes you depend on arrive in days, not quarters.

The habit is spreading. [Ghost](/tools/ghost/) shipped 11 releases, including Node 24 support in v6.63.0. [Strapi](/tools/strapi/) cut 7 releases up to v5.53.0. [Chatwoot](/tools/chatwoot/) used v4.17.0 to go deep on WhatsApp: Cloud API and Twilio template management, campaign delivery tracking, and a Freshdesk importer for teams migrating off that platform. For the stack argument from July, this section is the load-bearing one. Cadence is the difference between adopting a project and adopting a liability.

## The agent layer built a supply chain

The newest shelf is also the fastest moving. [claude-seo](/tools/claude-seo/), a universal SEO skill for Claude Code, grew from 15,100 to nearly 16,900 stars in the final 21 days, and its sibling [claude-ads](/tools/claude-ads/) added another 700. The same maintainer added roughly 2,500 stars across the two repos in three weeks. [google-meta-ads-ga4-mcp](/tools/google-meta-ads-ga4-mcp/), an MCP server that puts Google Ads, Meta Ads, and GA4 behind one interface for agents, grew 66 percent in the same 21 days, from about 1,100 to 1,800 stars. New to our tracking this month: [openseo](/tools/openseo/), an open-source alternative to Semrush and Ahrefs that arrived at 18,600 stars.

Underneath it, [langchain](/tools/langchain/) worked through a run of alphas in late August and shipped langchain 1.4.0 stable on September 3. And [Open Mercato](/tools/open-mercato/) used its v0.7.0 release on August 26 to describe something I have not seen from a CRM project before: a development harness where AI agents build, test, and judge applications end to end, with enforced spec phases, generated locale validation, and privacy-gated session sharing. The framing is agent-native CRM. At 1,700 stars it is early, but the release notes read like the team is building for a buyer who never opens the UI. I covered the adjacent platform shift, agent tooling eating the edges of the martech stack, in [the Claude Cowork piece](/blog/claude-cowork-is-eating-the-edges-of-your-martech-stack/); this window is what the same shift looks like from the open-source side.

I remain genuinely unsure how much of the agent-skills boom is durable infrastructure and how much is the current fashion. The star curves say people care. The fastest mover being an ads-data MCP suggests the near-term value is boring and real: agents pulling campaign data without a human copy-pasting CSVs between platforms.

## What I would do with this

The July stack argument holds, with one amendment: the CRM line item has become a shortlist decision. WhatsApp-heavy sales teams should look at [WACRM](/tools/wacrm/). Teams escaping Salesforce pricing should keep [Twenty](/tools/twenty/) at the top of the list. Marketing-automation-first teams should stay on [Mautic](/tools/mautic/), which just shipped its strongest release in a while. If you want to see where CRMs go when agents are the primary user, [Open Mercato](/tools/open-mercato/) is the most interesting experiment running.

Wait for the Matomo 6 stable tag before touching production analytics, but read the beta notes now. Everything else in the window is housekeeping you can adopt on your own schedule. The full tool-by-tool version of the stack argument lives in [the original piece](/blog/open-source-martech-stack/), everything from this beat is filed under [open source](/categories/open-source/) and [workflow automation](/categories/workflow-automation/), and the CRM contenders sit in [the CRM directory](/categories/crm/).

::: verdict win
<div class="verdict-label">✓ The July stack bet held</div>

Every layer we recommended shipped during the window. CRM and agent tooling, the least settled layers, moved fastest of all.
:::

Tools linked in this post: [n8n](/tools/n8n/) · [Mautic](/tools/mautic/) · [Twenty](/tools/twenty/) · [Frappe CRM](/tools/frappe-crm/) · [WACRM](/tools/wacrm/) · [Matomo](/tools/matomo/) · [Umami](/tools/umami/) · [Plausible](/tools/plausible/) · [Ghost](/tools/ghost/) · [Strapi](/tools/strapi/) · [Chatwoot](/tools/chatwoot/) · [claude-seo](/tools/claude-seo/) · [claude-ads](/tools/claude-ads/) · [google-meta-ads-ga4-mcp](/tools/google-meta-ads-ga4-mcp/) · [openseo](/tools/openseo/) · [langchain](/tools/langchain/) · [Open Mercato](/tools/open-mercato/)
