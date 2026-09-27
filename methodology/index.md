# Methodology

By Tim Christensen · updated 2026-09-26

Everything on MartechSignal follows one evidence standard and one scoring rubric. Both are published here so you can check our work.

## How we evaluate

Every assessment is researched from public documentation, the source repository when the product is open, and vendor materials including pricing pages. Running the tools is not our default and we do not claim it. Where a page does report hands-on work, that page says exactly what was run and discloses any relationship to the product on its face. Where a page depends on a specific fact (a price, an integration count, a release cadence), the fact is stated with its source and its verification date.

What that standard gives us: prices only as the vendor publishes them, statistics only from the named source, and no synthetic performance data. What it costs us: we cannot tell you how a tool feels to use day to day. Where a question only hands-on testing can answer, the page says so.

Corrections are public. When a published claim is wrong, the fix ships with an entry on the corrections page in the same change.

## The MartechSignal Score

Each evaluated tool receives a 0-10 score on six pillars. The total is the sum of the six, reported out of 60. Every pillar score on a tool page carries a one-line evidence statement naming its source. A score without evidence is a defect.

The score is an editorial assessment against published anchors. It is not a lab benchmark, not a verified-buyer rating, and not influenced by vendors: we take no vendor money, run no affiliate links, and accept no payment for placement or scoring. Tools we cover include products we built ourselves; those pages say so on their face.

The pilot covers the 20 most-searched tools on the site. The rollout to the full catalog follows the same rubric.

## Data artifacts

When a post cites a number we computed, the underlying artifact is published with its window and source so the query can be rerun.

gsc-query-distribution-2026-05-29_2026-08-26.csv. Source: Google Search Console API (searchAnalytics.query), property sc-domain:martechsignal.com, webmasters scope, service-account auth. Window: 2026-05-29 through 2026-08-26 (90 days). Dimensions: query-level rows, no filters, up to 1,000 rows (417 returned; the API omits ultra-low-impression queries). Headline numbers cited on the site: 417 queries, 1,737 total impressions, 0 clicks site-wide in the window; 1,492 impressions (85.9%) at average position 51+. Caveat: average position is Google's mean over impressions in the window; day-by-day rank volatility is not visible in the export. Any GSC performance export filtered to the same dates produces the same shape.

## OSS Momentum Tracker

The momentum dataset covers every catalog entry that names a public GitHub repository. Two real sources back it: fresh GitHub repository totals and release dates, and the measurement series from the git history of our public catalog (every committed snapshot of the tools file, dated by its commit). GitHub's star-timestamp endpoints are not accessible to this project, so each growth figure states its own snapshot-bounded window and snapshots are never interpolated. Entries without a recorded repository URL are listed as out of scope, never estimated.

Published errors get public entries. See the corrections page for the running log.
