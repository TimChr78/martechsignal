# Revive Adserver review (2026): pricing, AI features, verdict

- [Home](/)
- [Tools](/tools/)
- [Advertising & Paid Media](/categories/advertising/)
- Revive Adserver
## Revive Adserver review (2026): pricing, AI features, verdict

Free open source ad server for publishers, ad networks and advertisers

Advertising & Paid Media · Open Source Desk-reviewed

MartechSignal editorial review by [Tim Christensen](/authors/tim-christensen/)

[Visit Revive Adserver →](https://www.revive-adserver.com)

[How we review](/methodology/) · No affiliate links

[Visit Revive Adserver →](https://www.revive-adserver.com)

## MartechSignal Score: 27/60

Revive Adserver is the free ad server for publishers who want to own delivery. GPL-2.0 and self-hosted; the hosted Aqua Platform hides its price and the platform shows its PHP age.


| Pillar | Score | Evidence |
| --- | --- | --- |
| Pricing transparency | 5/10 | Self-hosted free (GPL-2.0); the hosted Aqua Platform sells with no public price (Sep 2026) (the vendor pricing page: [vendor site](https://www.revive-adserver.com), verified 2026-09-28). |
| Feature depth | 4/10 | Ad serving, targeting and reporting for publishers and networks cover the classic ad-server job (vendor documentation: [vendor site](https://www.revive-adserver.com), verified 2026-09-28). |
| Integrations | 3/10 | MaxMind GeoLite2, Google AdSense, MySQL and PHP documented; no API (vendor documentation: [vendor site](https://www.revive-adserver.com), verified 2026-09-28). |
| AI capability | 2/10 | No AI features are documented in the catalog as of 2026-09-28 (vendor documentation: [vendor site](https://www.revive-adserver.com), verified 2026-09-28). |
| Openness | 8/10 | GPL-2.0 with full self-hosting (the source repository: [repository](https://github.com/revive-adserver/revive-adserver), verified 2026-09-28). |
| Operational maturity | 5/10 | Long-lived open-source ad server with a hosted edition behind it (vendor documentation: [vendor site](https://www.revive-adserver.com), verified 2026-09-28). |

Scored 2026-09-28 against our published rubric: six pillars, 0-10 each. This is an editorial assessment from documentation and vendor materials, not a lab benchmark or a verified-buyer rating. The full rubric is on the [methodology page](/methodology/).

## Overview

Revive Adserver is a free, open source ad server for publishers, ad networks and advertisers who want to run their own ad serving. It is the direct descendant of PhpAdsNew and OpenX, maintained as a community project with backing from Aqua Platform. You install it on your own PHP and MySQL infrastructure, define advertisers, campaigns and banners, set up websites and zones, and paste invocation code into your pages. Ads can be served on websites, in apps and in video players. Delivery control covers the practical needs of direct-sold and house campaigns. Frequency capping, URL targeting and geotargeting decide who sees what. Geotargeting runs through a plugin that uses MaxMind GeoLite2 data, so accuracy depends on keeping that database current. Delivery rule sets apply reusable targeting across banners, which helps when one campaign runs across many zones. Reporting tracks requests, impressions, clicks and conversions, with CTR, conversion rates, revenue and eCPM broken out, plus conversion details like basket value and number of items purchased. Google AdSense can be served alongside your own inventory. The trade-off is operational. You run the servers, apply updates and handle security advisories yourself. The documentation lives in a wiki with user, admin and developer guides covering installation, upgrades, delivery rules and plugin development. There is no commercial cloud tier from the project itself. A separate Hosted edition is sold at revive-adserver.net by Aqua Platform, the company behind the software, for teams that want the same ad server without running it. For ad serving on infrastructure you control, with no license fee and no per-impression cost, Revive is the established option.

## Key Integrations

- MaxMind GeoLite2
- Google AdSense
- MySQL
- PHP
## Pricing

Revive Adserver is free to self-host under the GPL-2.0 licence.

Free self-hosted (GPL-2.0). A separate hosted edition is sold at revive-adserver.net (Aqua Platform); no public price (Sep 2026).

## Best for

Publishers, ad networks and developers who want control of delivery, data and infrastructure, and who have the PHP and MySQL ops skills to run the stack.

## Not for

Teams that want a managed ad platform with vendor support, built-in demand or header bidding. Revive is a direct-sold and house-ads server.

## Review notes

Setting up Revive follows the classic ad server path. Admins create advertisers, then campaigns and banners under them, then websites and zones for placements, and finally link campaigns to zones and paste the invocation code into pages. The hierarchy is fixed and familiar to anyone who has used OpenX or similar systems. Banner types cover images, HTML and text, and the same install delivers into websites, apps and video players.

Delivery rules do the day-to-day work: frequency capping, URL targeting and geotargeting. Geotargeting runs through a plugin using MaxMind GeoLite2 data, so operators who care about geo accuracy keep that database updated. Delivery rule sets are reusable across banners, which saves repetition when one campaign spans many zones.

Reporting is built for billing conversations. Requests, impressions, clicks and conversions are tracked, with CTR, conversion rates, revenue and eCPM available and conversion details down to basket value and item counts. Google AdSense can run next to house inventory as a banner source. What the project does not provide is operations. Patching, backups and security advisories belong to the operator, and the docs are a wiki rather than a vendor support desk. Assessed from vendor docs and the project README.

## Verdict

The dependable choice for ad serving on your own servers with no license fee and no per-impression cost. Expect to own the ops work.

## Pros and cons


| Pros | Cons |
| --- | --- |
| ✓ GPL-2.0 licence with free self-hosting | ✗ You run the servers, apply updates and watch security advisories yourself. |
| ✓ Active public repository (1,505 GitHub stars counted at last check) | ✗ Geotargeting quality depends on the MaxMind GeoLite2 plugin and its database updates. |
| ✓ GPL-2.0 with no license fee and no per-impression charges. | ✗ The interface is mature in the old sense; anyone expecting a current SaaS UI will notice its age. |
| ✓ Serves websites, apps and video players from one install. |  |
| ✓ A hosted edition at revive-adserver.net exists for teams that want the software without running it. |  |

## Related concepts

- [DSP](/glossary/dsp/)
- [DCO](/glossary/dco/)
- [Programmatic](/glossary/programmatic-advertising/)
- [CRO](/glossary/cro/)
Full definitions in the [martech glossary](/glossary/).

### Building your martech shortlist?

The weekly newsletter: one tool teardown, one workflow, no fluff. Free.

## Frequently asked questions

**What is Revive Adserver?**
Revive Adserver: Free open source ad server for publishers, ad networks and advertisers. The public repository carries 1,505 stars.

**How much does Revive Adserver cost?**
Revive Adserver is open source - GPL-2.0 licensed and free to self-host; the public repository carries 1,505 stars; native integrations cover MaxMind GeoLite2, Google AdSense, MySQL. You pay in server time and maintenance, not licences.

**Is Revive Adserver a good self-hosted Advertising & Paid Media tool in 2026?**
The dependable choice for ad serving on your own servers with no license fee and no per-impression cost. Expect to own the ops work.

**Is Revive Adserver free?**
Yes. The download edition is GPL-2.0 software with no license fee. A separate hosted edition is sold at revive-adserver.net by Aqua Platform, so you pay only if you want someone else to operate it.

**What do I need to run it?**
A PHP and MySQL stack. Installation, upgrade and configuration steps sit in the Administrator Guide on the project documentation site.

**Does it support geotargeting?**
Yes. Revive v5 geotargeting runs through a plugin that uses MaxMind GeoLite2 data; the project README lists GeoLite2 as a dependency.

## Similar Tools

- [Google Ads + Meta Ads + GA4 MCP](/tools/google-meta-ads-ga4-mcp/): MCP server giving AI agents read/write control of Google Ads, Meta Ads, and GA4
- [Albert AI](/tools/albert-ai/): Autonomous AI platform that manages and optimizes digital advertising campaigns
- [Line Harness](/tools/line-harness/): Open-source CRM for LINE Official Accounts with step delivery, scoring, and an MCP server for AI control
- [Nightwatch](/tools/nightwatch/): Rank tracking across Google and AI answers, priced by keyword with unlimited seats
- [AdCreative.ai](/tools/adcreative-ai/): AI platform generating high-converting ad creatives and social media post designs
## Related reading

- [Google Just Handed Your Ad Budget to AI Agents , and Kept You on the Hook](/blog/google-ad-agents-control-gap/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
- [The guardrails Google won't ship for your AI ad account](/blog/google-ads-ai-guardrails/)
### Quick Facts

- **Pricing:** Open Source
- **Category:** [Advertising & Paid Media](/categories/advertising/)
- **GitHub:** ★ 1505
- **API:** No
- **Repository checked:** 2026-10-02
- **Page updated:** 2026-09-25

## Get the next teardown

One email when a new tool review lands, nothing else.

© 2026 MARTECHSIGNAL · THE AI IN MARKETING AUTOMATION

[More Advertising & Paid Media Tools →](/categories/advertising/)

[HOME](/)[TOOLS](/tools/)[BEST](/best/)[VS](/vs/)[ALTERNATIVES](/alternatives/)[BLOG](/blog/)[GUIDES](/guides/)[TRENDING](/trending/)[GLOSSARY](/glossary/)[CHECKLIST](/checklist/)[AUTHOR](/authors/tim-christensen/)[ABOUT](/about/)[CONTACT](/contact/)[CORRECTIONS](/corrections/)[PRIVACY](/privacy/)[TERMS](/terms/)[AI POLICY](/ai-policy/)[METHODOLOGY](/methodology/)[RSS](/rss.xml)[AI CATALOG](/llms.txt)[SUBSCRIBE](/#subscribe)
