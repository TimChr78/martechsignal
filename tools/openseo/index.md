# OpenSEO | MartechSignal review

Open source alternative to Ahrefs and Semrush

- Page: https://martechsignal.com/tools/openseo/
- Category: SEO & Search
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-07

OpenSEO is an open-source, self-hosted SEO platform covering keyword research, rank tracking, competitor insights, backlink analysis, site audits, and AI search visibility, positioned as an alternative to Ahrefs and Semrush. The TypeScript project (repo every-app/open-seo) is MIT-licensed, held around 17,700 GitHub stars as of September 2026, and has moved quickly since its February 2026 debut: AI Visibility and Prompt Explorer landed in April, an MCP server in May, agent skills and multi-project support in June, Local SEO in August, and on-demand SERP depth on September 2. Two deployment paths are documented. Docker is described as best for testing: clone the repo, copy .env.example to .env, and run docker compose up -d, which serves on port 3001 with authentication disabled, so it belongs behind your own reverse proxy or private network. For an internet-facing or team install the README recommends the Cloudflare path, where pnpm deploy:selfhost provisions D1, KV, R2, and a Cloudflare Access gate on Cloudflare's free plan. Data is the real cost. OpenSEO is a front end over DataForSEO: you bring your own API key (the base64 of your DataForSEO email and password), pay that vendor directly for what you use, and add a separate OpenRouter key for AI features such as SAM, the in-app SEO agent. New DataForSEO accounts include $1 of credit and the minimum top-up is $50. The hosted service at openseo.so charges $10/month including $10 of usage, and the README states plainly that the hosted margin is a 28% surcharge on every DataForSEO request, so self-hosting is slightly cheaper. Rank tracking defaults to weekly, and the docs note that daily checks use seven times more credits. Google Search Console and Google Analytics data is free. The trade-off is the usual one: you own the interface, the scheduling, and your own database, not the crawl index.
