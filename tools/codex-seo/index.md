# Codex SEO | MartechSignal review

Codex-first SEO skill suite with 26 workflows, 24 TOML agents, and API integrations

- Page: https://martechsignal.com/tools/codex-seo/
- Category: Agent Skills
- Pricing: Free
- Open source: no
- Last verified: 2026-08-28

Codex SEO is the OpenAI Codex port of Claude SEO, built by the same author (AgriciDaniel). It covers the same SEO surface: technical audits, on-page analysis, E-E-A-T content quality, schema markup, Core Web Vitals, GEO/AEO for AI search, backlinks, local SEO, ecommerce SEO, hreflang, and semantic clustering. The difference is the runtime. Instead of Claude Code's subagent model, Codex SEO uses 24 TOML agent profiles, deterministic headless runners, and a Python virtualenv at ~/.codex/skills/seo/.venv/. If your team runs Codex instead of Claude Code, this is the same workflow adapted to your platform.

The integration surface is wider than Claude SEO's. Codex SEO connects to DataForSEO for keyword and SERP data, Google Search Console for performance metrics, Firecrawl for page crawling, and Gemini for image analysis workflows. The headless runners mean you can script audits in CI or run them on a schedule without an interactive terminal. 52 tests pass, and the installer handles dependency setup, capability groups, and runtime verification.

Installation is a one-line curl (or PowerShell on Windows). The installer copies skills into ~/.codex/skills/, agents into ~/.codex/agents/, creates the virtualenv, and installs dependencies. Current release is v1.9.6-codex.5, synchronized to Claude SEO upstream at commit a9cf338.

If you're choosing between this and Claude SEO, the decision is simple: use whichever matches your agent platform. The SEO methodology is the same. Codex SEO adds the DataForSEO and Firecrawl integrations that Claude SEO handles through its own extension system. For teams already paying for OpenAI's Codex, this avoids the cost of switching to Claude Code just for SEO audits. The star count (534) is lower than Claude SEO's 12,873, which reflects the smaller Codex user base, not a quality gap.
