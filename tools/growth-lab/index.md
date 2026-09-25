# Growth Lab | MartechSignal review

Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex

- Page: https://martechsignal.com/tools/growth-lab/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (Apache-2.0)
- Last verified: 2026-08-28

Growth Lab is an agent skill pack that turns Claude Code or OpenAI Codex into a growth operator. You clone the repo, open the folder in your agent, and describe the growth outcome you want. The agent reads your product (a codebase, a prototype, or just a URL), researches what people actually search for, creates SEO pages aimed at those queries, publishes them, pings IndexNow, then reads the performance data and decides what to do next. The pitch is that context stops leaking between five disconnected tools. One workspace holds the product, the research, the output, and the results.

Skills carry the method, and files carry the memory. Each capability is an observe-act-review loop with its own persistent memory, and the next run reads the previous results before it starts. The SEO loop maps user scenarios to live SERP research and generates pages that answer real queries. In the team's own test run, new pages got indexed within 1-2 days and page impressions and clicks both rose about 10x on a 7-day average. Average CTR dropped 50%, which they treated as input for the next iteration rather than a failure. The second loop targets Xiaohongshu: it collects high-performing posts in your niche, replicates the winning structure, writes the copy, generates images, runs a compliance check, and reviews the results. Their best test post drew 4,000+ likes and saves. Actual publishing on Xiaohongshu stays manual by design.

Setup is git clone plus a conversation. An onboarding skill audits what's missing: API keys, browser sessions, third-party clients. You fix gaps in plain language instead of editing a config file. Secrets and cookies stay outside the workspace and never enter memory. The repo is Apache 2.0 licensed, has about 308 stars, and was pushed within days of this writing.

The honest caveats: the project is roughly a week old. Only two loops actually work, and all the performance numbers come from a single run on the authors' own site. You need paid access to Claude Code or Codex, plus comfort working in a terminal with an agent. If your channels are X, LinkedIn, or TikTok, there's no loop for those yet.

Who it's for: technical founders and small teams already living in a coding agent who want the growth work done rather than another dashboard. Compared with Surfer or Semrush, it writes and publishes the page instead of handing you recommendations. Compared with doing it manually, the research-to-publish cycle becomes one conversation. Compared with most agent skill packs, which teach the agent marketing knowledge, this one runs the loop end to end, memory included.
