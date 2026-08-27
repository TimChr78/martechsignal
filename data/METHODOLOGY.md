# Data artifacts — methodology

These files back the numbers cited in MartechSignal posts. Each file states its window and source so you can rerun the query yourself.

## gsc-query-distribution-2026-05-29_2026-08-26.csv

- **Source:** Google Search Console API (searchAnalytics.query), property sc-domain:martechsignal.com, webmasters scope, service-account auth.
- **Window:** 2026-05-29 through 2026-08-26 (90 days).
- **Dimensions:** query-level rows, no filters, up to 1,000 rows (417 returned; GSC omits ultra-low-impression queries).
- **Headline numbers cited on the site:** 417 queries, 1,737 total impressions, 0 clicks site-wide in the window; 1,492 impressions (85.9%) at average position 51+.
- **Caveat:** avg_position is Google's mean over impressions in the window; day-by-day rank volatility is not visible here. Anonymized queries ("anonymized queries" rows) are excluded by Google from the API response.

How to reproduce: any GSC performance export filtered to the same dates produces the same shape. The exact per-query table above is reproducible via the API with the parameters listed.
