# Seonaut | MartechSignal review

Open-source SEO crawler in Go for technical audits, self-hosted or cloud

- Page: https://martechsignal.com/tools/seonaut/
- Category: SEO & Search
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-07

SEOnaut is an MIT-licensed SEO crawler written in Go, self-hosted with Docker and MySQL, and also offered as a hosted service with a free Lite tier (one project, 500 URLs per project) and a $9-per-month Growth plan (five projects, 10,000 URLs, recurring audits), billed through Stripe with one month free on annual plans; the site claims more than 3,000 professionals use it. The code defines 79 issue types across page-level and site-wide checks: broken links and redirects including loops, missing or duplicate meta tags, heading order, hreflang problems, image and alt-text audits for accessibility, content quality, canonical tags, orphan and dead-end pages, HTTPS checks, and TTFB and timeout detection. Documented crawl options include bypassing robots.txt, following nofollow links, crawling from sitemaps or subdomains, checking external links, basic-auth crawls, and WACZ archive creation. Results land in Apache ECharts dashboards with CSV, sitemap, and WACZ exports, and the crawler identifies itself as SEOnautBot/1.0. The honest limits shape who should adopt it: there is no JavaScript rendering, since no headless browser exists in the codebase, so client-rendered pages will audit badly; there is no API, because all routes are session-based web UI; there is no team or role model, with single-user projects in the schema; and no AI features appear anywhere in the product or its site. Maintenance is active but unhurried: 900-plus commits since 2022, the most recent in May 2026, and no tagged releases, so installs track the :latest container image. Source builds need Go 1.25 and the compose file runs MySQL 8.4, serving plain HTTP on port 9000 with signup rather than a default account. Against Screaming Frog the trade is direct: no license cost and repeatable self-hosted audits, in exchange for JS rendering and a commercial feature set.
