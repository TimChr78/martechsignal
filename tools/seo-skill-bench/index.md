# SEO Skill Bench | MartechSignal review

Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects

- Page: https://martechsignal.com/tools/seo-skill-bench/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (MIT)
- Last verified: 2026-09-03

SEO Skill Bench answers the question every Claude Code SEO skill README can't: does the thing actually work once installed? It is an open benchmark that runs SEO skills for Claude Code and other coding agents against fixture websites with deliberately planted defects, then scores what they find. If you are choosing an SEO skill for your agent workflow, this is the closest thing to a published answer key.

The harness installs each entrant in a real headless Claude Code session (claude -p), not a simulation reconstructed from its README, and points it at the pivot-saas fixture site. Scoring follows a pre-registered 100-point rubric: 40 points for detecting planted defects, 25 for avoiding traps, meaning the skill never recommends fixing something that is already fine, 25 for blind-judged judgment calls, and 10 for execution. Scores are medians across runs. On the August 2026 board, SEOAgent led at 84.9 while the vanilla baseline with no skill scored 73.0. That spread tells you two things: skills can add real value, and some entrants score below doing nothing at all.

Setup needs Node and a Claude Code install. You run node harness/run.mjs with a skill id and fixture, then the score and judge scripts, and entrants register with a one-line entry in skills.json. The leaderboard also publishes what each skill costs, kept outside the composite on purpose: resident tokens the skill occupies in every system prompt, per-run cost, and median time. Runs on the board cost between $1.70 and $4.46 and took 405 to 779 seconds. Heavy skills like Corey Haines' Marketing Skills carry 8,770 resident tokens, which dilutes every other skill you have installed.

The big caveat is the maintainer's conflict of interest. SEOAgent, the company behind the benchmark, also ships the top-ranked entrant. The structural mitigations are real: published fixtures, deterministic answer keys, a frozen rubric, blind judging, and a harness anyone can re-run. Still, treat the leaderboard as a strong signal rather than gospel. The benchmark only measures technical on-site audit work against one fixture. It says nothing about content strategy, links, or your actual site. At about 50 stars the community is small, and the repo's value is its method more than its momentum.

Compared to picking a skill by GitHub stars or vibes, this is the most concrete public way to see detection rates and hallucination traps side by side. If you are building an agent-driven SEO workflow, run your candidate skill through this harness before you point it at a production site.
