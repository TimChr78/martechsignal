# Matomo vs PostHog (2026): web analytics or product analytics

## Matomo vs PostHog (2026): web analytics or product analytics

Pick Matomo if you want web analytics depth with EU residency and raw data you own, self-hosted free. Pick PostHog if your questions are about product usage, with flags and experiments beside the funnel.

Matomo and PostHog get compared more than their categories suggest, because both answer the same executive question: what do people do on our thing? They answer it from opposite ends. Matomo is web analytics in the classic sense, built to replace Google Analytics with better privacy defaults. PostHog is product analytics with web numbers as one slice of the platform.

The numbers below come from each vendor's own published materials, catalogued and checked this month. For the privacy-first three-way including Plausible, start with the quick-decision table on Matomo vs Plausible.

Both products grew up open source and both still sell trust as much as features: one promises your analytics data stays yours, the other promises your product data answers questions without a data team. The trade-offs below follow from that split.

## Matomo vs PostHog: the quick decision


| Tool | Starts at | Pick it when |
| --- | --- | --- |
| Matomo | Open Source from €22/mo | You want web analytics depth, EU data residency and raw data you own outright. |
| PostHog | Freemium | Your real questions are about product usage, with flags and experiments beside the funnel. |

[Matomo assessment](/tools/matomo/) · [PostHog assessment](/tools/posthog/)

Matomo: [Official site](https://matomo.org) · [Pricing](https://matomo.org/pricing/) · [GitHub](https://github.com/matomo-org/matomo)

PostHog: [Official site](https://posthog.com) · [Pricing](https://posthog.com/pricing) · [GitHub](https://github.com/PostHog/posthog)

Matomo

PostHog


| Dimension | Matomo | PostHog |
| --- | --- | --- |
| Pricing | Open Source from €22/mo | Freemium |
| Open source | yes (gpl-3.0) | yes (mit) |
| Integrations listed | 8 listed: WordPress, Matomo Tag Manager, Google Tag Manager, Google Analytics Importer (+4 more) | 6 listed: Slack, GitHub, Zapier, Segment (+2 more) |
| Public API | yes | yes |

## Positioning

**Matomo:** Web analytics first: sessions, channels, campaigns and content performance, with heatmaps and session recording as paid modules. The mental model is the GA report suite, done with EU hosting and full raw data access.

**PostHog:** Product analytics first: events, funnels, retention, feature flags and experiments in one platform. Web traffic is a product surface like any other, and the pricing rewards the product team that goes deep.

## Pricing shape

**Matomo:** Self-hosted core is free under GPL. On-Premise premium bundles and Cloud subscriptions price by traffic, and the vendor publishes every tier. No data is used for anything but your reports.

**PostHog:** Usage-based with a free tier on every product every month: generous enough that many small products pay nothing. Costs arrive per event and per feature used, which rewards discipline with event design.

## Deployment and data residency

**Matomo:** Self-host on your own EU infrastructure for full control, or use EU-hosted Cloud. Data ownership is the product's core promise and the licence guarantees it.

**PostHog:** Cloud US by default with an EU cloud option, and a self-hosted open-source edition that carries usage-based billing above its free tier. Check which edition fits your compliance story before committing.

## Reporting depth

**Matomo:** Matomo's report suite is the deepest web-analytics surface in the comparison class: multi-channel attribution, cohort and segmentation engines, and content reports that map to how marketing teams actually work. The raw data sits in your database, so anything missing is a SQL query away.

**PostHog:** PostHog's dashboards are event-driven and lighter on classic channel reporting. Where it leads is behavioural depth: session replay, heatmap-adjacent tools and feature usage tied to the same events, with SQL access on paid plans for the gaps.

## Governance and the licence question

**Matomo:** GPL v3+ for the self-hosted core, with premium modules on a separate commercial licence. The governance story is stable and the vendor's business model is support and cloud, not data.

**PostHog:** The self-hosted edition carries an unusual twist: it is open core with usage-based billing past the free tier, so self-hosting does not mean free at scale. Read the licence terms against your growth curve before betting a compliance story on it.

## Getting data in and out

**Matomo:** Tag Manager ships with it, the tracking API covers server-side and mobile, and every table in the self-hosted schema is queryable. Exports run to raw CSV and scheduled archives, so leaving with your history is a script, not a negotiation.

**PostHog:** Ingestion is event-first: SDKs for the common stacks, a capture API for everything else, and batch export into a warehouse for teams that outgrow the built-in analysis. The reverse ETL story back into operational tools is stronger than Matomo's.

## What each looks like at month six

**Matomo:** At month six a Matomo setup looks like a tuned report suite: custom dimensions mapped to your business vocabulary, scheduled email reports for stakeholders, and maybe the heatmap module on the two pages that matter. The maintenance load is a person-hours a month on patching if self-hosted.

**PostHog:** At month six a PostHog setup looks like an event taxonomy with governance: naming conventions someone wrote down, flags replacing deploy-time risk, and experiments running against the funnels that justify them. The maintenance load is discipline, not servers: events rot if nobody owns the taxonomy.

## Scope

**Matomo:** If the question is 'how is the website performing', Matomo's report suite answers it without a data team. Campaign attribution and content reporting are deeper than anything in the product-analytics class.

**PostHog:** If the question is 'which feature retains users', PostHog answers it in one platform: flags, experiments and session replay sit next to the funnel that measures them.

## Migration cost

Matomo runs a GA importer for the common historical case, so the standard 'leaving Google' move is largely scripted. Moving the other way, into PostHog, means an event plan before data: PostHog reads events and properties, not pageviews, so a week of naming design precedes any import.

Historical parity is the trap in both directions. Matomo keeps raw data indefinitely while self-hosted; PostHog's retention varies by plan. Export what you must keep before any switch, in both vendors' own export formats, because that window closes with the old contract.

For teams moving from Matomo to PostHog, the one migration asset worth building first is the mapping from Matomo's pageview-centric reports to your new event names. Get that mapping reviewed by whoever owns the reporting today; the numbers will not reconcile during the overlap month unless the vocabulary matches.

## When neither is the right answer

If your question is purely commercial, 'which channel sells', a warehouse-native BI layer over your own order data beats both. And if the site is a brochure and the product is offline, neither tool earns its script tag.

## Who should pick which

- **Pick Matomo if:** you want web analytics depth, EU data residency and raw data you own outright.
- **Pick PostHog if:** the real questions are about product usage, and you want flags and experiments beside the funnel.

## Matomo or PostHog for a content site?

Matomo. Web analytics depth, EU data residency and raw data the team owns outright are its verdict. PostHog aims at product teams, not pageview reporting.

## When does PostHog win?

When the real questions are about product usage: funnels, retention, session replay, with flags and experiments beside the funnel. That is a product analytics job, not a traffic analytics job.

## Which one is simpler to start?

PostHog Cloud for teams that accept hosted product analytics, Plausible for teams whose needs stop at core traffic numbers. Matomo pays off once data residency or ecommerce depth enters the requirements.

Prices and features here come from each vendor's own published materials as catalogued on the tool pages. Read [how we evaluate](/methodology/) or download the [machine-readable catalog](/catalog-tools.json).

Last verified 2026-09-28.

## Browse the hubs behind this comparison

- [Analytics & Attribution](/categories/analytics/)
- [Open-Source Tools](/categories/open-source/)
## Open-source momentum, with receipts

Star counts we snapshot ourselves every morning - check any of them against GitHub in one click.

- Matomo - 21,923 stars, +118 in the 42-snapshot window to 2026-10-05 21,805→21,923 [verify on GitHub](https://github.com/matomo-org/matomo)
- PostHog - 40,141 stars, +201 in the 10-snapshot window to 2026-10-05 39,940→40,141 [verify on GitHub](https://github.com/PostHog/posthog)
[All movers on the trending page](/trending/).

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
