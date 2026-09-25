# Diffmode Growth Tactics | MartechSignal review

Free Claude Code/Codex pipeline that mines case studies and rejects obvious growth plays

- Page: https://martechsignal.com/tools/diffmode-growth-tactics/
- Category: Agent Skills
- Pricing: Open Source
- Open source: yes (Apache-2.0)
- Last verified: 2026-08-31

Diffmode Growth Tactics is a free skill pack for Claude Code and Codex that runs a growth-strategy pipeline for startups that cannot outspend competitors. Give it your product URL and it researches who you compete with, maps your buyers by the job they hire you for, mines 12 to 20 real case studies for why each growth play worked, and produces 7 to 9 unconventional tactics with execution plans. A run takes about 90 minutes and everything runs locally.

The mechanism is the interesting part. The pipeline never asks the model to invent a tactic. It asks it to research, mine, and combine. Mechanisms are paired blind, before analysis, so the model cannot reverse-engineer its way back to the obvious answer. Then four gates reject output: if an average B2B marketer would recommend it, it dies. If stripping the adjectives leaves a conventional action, it dies. If a single mechanism could have produced it alone, it dies. Ten tactics that all say write content die. What survives gets a day-1, day-7, day-30 plan and a can-a-competitor-copy-this-in-30-days check. One documented run mined 24 mechanisms from 18 case studies and kept 6 unconventional tactics.

Setup is a Claude Code or Codex install plus an LLM API key. No account, no SaaS. The run produces a styled report in your browser and everything is reusable, competitor read, buyer map, tactic cards. The skills are plain markdown files, so you can read exactly what the pipeline does and audit it.

It will not run itself. The output is strategy on a page, not executed campaigns, and the quality depends on your market having enough public case studies to mine. A brand-new niche with no documented growth stories will produce thinner results. It is aimed at technical founders and growth people who already use coding agents. If you want a managed growth consultant instead of a 90-minute local run, the SaaS planning tools in this directory are the alternative.
