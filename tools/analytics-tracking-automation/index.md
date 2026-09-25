# Analytics Tracking Automation | MartechSignal review

AI skill for GA4 + GTM event tracking: site analysis, schema design, and go-live

- Page: https://martechsignal.com/tools/analytics-tracking-automation/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (Apache-2.0)
- Last verified: 2026-08-28

Analytics Tracking Automation solves a specific, annoying problem: setting up GA4 and GTM event tracking correctly. Most marketing teams either skip proper tracking setup or pay a consultant $2,000 to do it. This skill automates the workflow from site analysis to go-live. You give it a URL, and it analyzes the site, groups pages by business purpose, designs a GA4 event schema, produces GTM-ready outputs, and walks you through verification before publishing. It handles both generic websites and Shopify storefronts.

The workflow is artifact-backed, meaning each step produces a reviewable file you can inspect before moving on. The site analysis groups pages into business categories (product, checkout, blog, support) so the event schema maps to actual user journeys rather than generic pageview tracking. The GTM output includes the container configuration, trigger definitions, and variable setup. Verification guidance tells you what to check in GTM preview mode before you publish. If you stop halfway through, the artifacts let you resume where you left off.

Installation is npm-based: clone the repo and run npm run install:skills, or use npx skills add jtrackingai/analytics-tracking-automation for a no-clone install. It works on Cursor, Codex, and any agent that reads the skill format. The ClawHub publish path strips executable runtime files for marketplace safety.

This is the narrowest tool in this batch, and that's its strength. It doesn't try to be a full marketing suite. It does one thing that every marketing team needs and few do well. At 134 stars, it's the smallest repo here, and the last push was April 2026, so it's not getting weekly updates. But the problem it solves doesn't change often. GA4's event model is stable, GTM's container format is stable, and the workflow from "we need tracking" to "tracking is live and verified" is well-defined. If you're setting up analytics for a new site or auditing an existing GTM mess, this saves you a day of spreadsheet work and a week of "is this firing correctly?" anxiety.
