# Corrections

## Corrections

We make mistakes; when we find one, we fix it and say so here. This log is newest-first. If you spot an error we missed, the contact page has the channels - every accepted correction gets a public entry on this page.

## Snippet prices corrected and source fenced (October 5, second wave)

The pricing-snippet rewrite shipped the same day briefly showed Salesforce Marketing Cloud "from $25/mo" in the /vs/ comparison snippet; the page itself says $1,500/mo (the $25 figure is per-user, Starter tier). The snippet now says "enterprise from $1,500/mo", and a build-time test now fails any future snippet whose figures do not appear verbatim on the page. Money-leaf metas across the 34 comparison pages now carry verified entry prices (33 of 34; pages with no published price carry none). Also this wave: the /tools/ mirror now answers cost questions (prices on every card), the /best/ pages link their related comparisons, and changed pages now carry an honest dateModified so search engines can see the edit.

## Remediation wave logged: the 2026-10-02/03/05 audit fixes

The October audit remediation shipped across three deploys (October 2, 3 and 5) and touched most of the site's pages. The corrections a reader could have seen: Heap's page no longer shows an inferred $250/mo figure - Growth and Pro are custom-priced with no published entry price, so no paid figure is shown. The /alternatives/ Billing-model column now reads each tool's catalog pricing model instead of a mostly-empty notes field (Make and n8n no longer read "Contract"; only Tray.io and Workato do, correctly). A stray trailing quote is gone from pricing FAQ answers across 58 pages. Three new category hubs shipped (email marketing, content AI, personalization).

One earlier disposition on this page is reversed: we had declined the WebPage.breadcrumb edge as optional with no rich-result effect, and a later fix attempt deleted the edge entirely to satisfy a counter. That was the wrong fix. The edge is now restored on all pages with every breadcrumb node carrying its identifier, so the site's structured-data graph is connected again rather than merely unflagged.

Structural work with no visible change: the speakable markup property is corrected, and meta descriptions now cut on sentence boundaries instead of mid-clause.

## Disposition: chart PNGs stay PNG, SuiteCRM pounds become £

Two low-priority audit notes assessed with evidence. First, the six chart images under /og/charts/ are the only PNG srcsets in the corpus (three entries flagged). They stay PNG deliberately: the bar charts are PIL-rendered with 14-22px labels, and lossy WebP blurs small text at these sizes while optimized PNG keeps labels sharp. The photographic/illustrated OG corpus stays WebP. Second, SuiteCRM commercial-hosting figures were written as words ("50 pounds monthly"); they now render as £ figures (£50, £143/£198/£308 tiers, £2,520 Quick Start), matching house symbol form. The record keeps its USD typing because the self-hosted product itself is free - the sterling figures are third-party hosting, now explicitly symboled.

## Remediation waves logged: the 2026-09-29/30 fix batches

The September 29-30 remediation work shipped more than twenty fixes across two audit rounds without updating this log as each batch landed. Recorded now, in brief: three high-priority defects from the September 29 audit (a structural heading repeat on the homepage, an image payload serving desktop renditions to mobile, and homepage star counts that could drift from the catalog) were fixed the same day; the medium and low waves that followed covered split verification stamps on open-source pages, a free-tier claim gate on trial-only products, offer data corrections (freshsales trial-only at $9, Zoho Standard at EUR 14, warmbly Starter at $29), one-time license figures that wrongly carried a monthly suffix (IDURAR, Krayin), repeated-slash URL variants now 301ing to their canonical path, email-shaped strings removed from install commands, glossary entity and dating markup, a 1200w WebP rung for mobile screenshots, and FAQ answers on the GEO visibility page whose prices disagreed with the catalog (Trakkr $10 vs $100, Nimt/Writesonic EUR 7 vs EUR 79/$79, Evertune $89 vs $800). Where the audit flagged a link as unreachable that we could load fine, we re-checked it live and recorded the disposition rather than "fixing" it.

Going forward, each remediation batch gets an entry here when it ships, not after the next audit asks.

## Audit low-priority dispositions: four more findings assessed

Today's SEO audit low tail included four items we are deliberately not changing. (1) Homepage inline styles: the first block is the shared critical-inline pattern every page carries, and the second is homepage-only above-fold CSS - moving it to the shared sheet would tax every page view to save one. (2) Euro codes in prose ("Standard EUR 14/user/mo"): the pages are faithful to vendor-quoted records, and the site rule is that money prose must match record currency, which code-form satisfies. (3) ARD entry types stay text/plain for the .txt surfaces: labelling a text file application/ai-registry+json would chase a Lighthouse point with a false content type, and discovery works through the link relation plus .well-known. (4) No breadcrumb property on WebPage nodes: the audit itself marks this optional with no rich-result effect. Build-time checks cover the items we did fix.

## Audit medium-priority disposition: vendor links flagged unreachable were reachable

Today's SEO audit flagged three links to one vendor domain as returning 503 during its linkcheck. Both URLs we actually emit returned HTTP 200 on direct retry the same evening (0.09s and 0.24s), as did the domain root, so the 503 was transient bot-handling on the vendor side, not a dead link. No link changed. If the vendor's bot-handling hardens permanently we will replace the links with plain-text citations.

## Audit low-priority dispositions: four findings declined with evidence

Today’s SEO audit low tail included four items we are not changing, and we are recording why. (1) Retired-product records (former Autopilot, Drift) stay in the catalog with no public page: both were acquired, both carry a named successor, and the catalog is the paper trail. (2) Two spelling variants of one deny-listed bot name are cosmetic: both variants are denied, so crawlers are unaffected. (3) The IndexNow “deployment gap” probed key paths that never existed (/indexnow.txt, /indexnow-keys/, indexnow.json); both real key files return HTTP 200 and submissions are succeeding. (4) Screenshot srcsets capped at 800w while the source captures are 1280px masters; 1200w honest-downscale rungs were added on 2026-09-29 with a build-time check. Two sitewide build-time checks (token repetition, star-literal-vs-catalog) and per-finding checks for the items we did fix fail the build if any of this regresses.

## Correction to our own corrections entry: the star sync shipped incomplete

Our earlier entry today claimed older star literals in prose were refreshed to the synced values. That was premature: 19 doubled "GitHub stars GitHub stars" phrases and 14 stale star numbers survived in tool descriptions, score evidence, and stats cells - some predating the sync itself. All are now collapsed or refreshed to the synced catalog values, and two build-time checks (token repetition, star-literal-vs-catalog) fail the build if either class ever regresses.

## Homepage layout and analytics loss, introduced by our own deploy

Our Sep 29 stylesheet sweep deleted the homepage's hand-maintained layout block (about 6.5 KB of CSS) and dropped the privacy-friendly analytics loader from the homepage and about page. The result shipped unverified: the tool index rendered as a run-on paragraph and visits went unmeasured. Both are restored, and build-time checks now fail if a sweep ever removes scripts or layout styles again.

## Star counts disagreed between pages

Momentum figures on comparison pages were read from our daily snapshot pipeline while tool pages quoted older catalog numbers, so fast-moving repositories showed different star counts on different pages (40 claims checked, all divergent). Both now draw from one synced source with one date. Older star literals in prose were refreshed to the synced values.

## Duplicate verdicts and a currency render bug

Three comparison pages shipped byte-identical verdict sentences for different tools wherever a per-tool verdict was missing; the fallback is removed and the build now fails on duplicates. Separately, seven tool pages rendered dollar signs on euro prices because the price template ignored each record's currency field; symbols now render from the record. HubSpot's schema showed only a paid tier while the page says free; the structured data now carries both tiers.

## Claude SEO ownership disclosure, founding date, and star count

Our Claude SEO page claimed "we built Claude SEO" and excluded the page from review markup on that basis. The claim was false: Claude SEO is a third-party MIT project by AgriciDaniel, and we have no affiliation with its author. The page now states the actual relationship (we run the tool on our own sites and depend on it in our audit pipeline, which is the real reason it carries no Review markup). Its founding date is corrected from 2025 to February 2026, and its GitHub figures from 16,675 stars and 2,443 forks to 17,737 and 2,599 with a verification date. Found by our own Claude SEO audit on 2026-09-26.

## SendGrid free-tier claim

Our SendGrid page claimed a permanent free tier of 100 emails per day. Twilio's pricing page lists that as a 60-day trial. The page now states the trial terms and notes that SendGrid has no permanent free tier. Found while gathering evidence for the MartechSignal Score pilot.

## FAQ answers on the checklist page

The checklist page carried structured data for 12 question-and-answer pairs that did not exist as visible content on the page. The answers had been generated by a pipeline with no written source copy behind them. The fabricated answers are removed; the page now carries markup that describes only what it actually shows.

## Open-source tool count on the trending page

The trending page claimed 69 open-source tools in the catalog while the catalog held 138 tools at the time (a total, not an open-source count). The page had a hard-coded number. It now states the count derived from the catalog data at build time. Counts elsewhere on the site now carry their denominator explicitly: the canonical open-source count is every catalog tool whose data is flagged open source (a public repository under an open or source-available license), currently 80 of the 160 active catalog tools as of 2026-09-27, and the /trending/ tracker states that it charts the subset with a public GitHub repository and enough snapshot history.

## Tool count on the front page

The front page said 133 tools while the catalog held 158. The number was written by hand and went stale. All headline counts on the front page are now generated from the catalog and the published post list at build time.

## Claude SEO review

Removed a hands-on paragraph from our Semrush review that described testing we did not perform. Our own disclosure on the same page said the opposite. Caught by our v2.3.1 audit; the page now states plainly that the tool was not run.

## Star counts on tool pages

A formatting defect inserted a space into thousands-separated figures on 76 tool pages ('150, 000' became '150,000'). All corrected at the data level.

## n8n GitHub star count

Prose on the n8n page said 'more than 198,000 stars' while the facts box said 203,890. Prose now carries the verified figure with its verification date.

## Unapproved posts taken down

Three Claude SEO comparison posts were published without approval by a pipeline bug and were removed the same day. Publishing now requires explicit approval; this page exists so that every future correction is public too.

## Review markup on this site's own tool page

Our Claude SEO review carried review-structured data for our own product. We removed the markup; the editorial text remains, clearly labelled.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

2026-10-05

2026-10-05

2026-09-30

2026-09-30

2026-09-29

2026-09-29

2026-09-29

2026-09-29

2026-09-29

2026-09-29

2026-09-29

2026-09-26

2026-09-26

2026-09-26

2026-09-26

2026-09-26

2026-09-16

2026-09-16

2026-09-14

2026-09-13

2026-09-16

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[SUBSCRIBE](/#subscribe)
