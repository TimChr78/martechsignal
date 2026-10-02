# Open-source martech momentum: the agent-skills layer wins

OPEN SOURCE · DATA · 7 MIN

## Where open-source martech momentum actually lives

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Where open-source martech momentum actually lives

SEP 26, 2026

Filed under [Agent Skills](/categories/agent-skills/)

The fastest-accumulating open-source projects in our catalog are not platforms. They are packs of agent skills, and the gap is widening.

We track 79 active open-source tools in the [directory](/tools/). Sixteen of them name a public GitHub repository, and those sixteen now have a [published momentum dataset](/oss-momentum.json) behind them. Every number below is a snapshot or a snapshot-bounded delta as of 26 September 2026. Nothing is estimated.

## The top of the board

[claude-ads](/tools/claude-ads/) leads with 9,576 stars and 1,857 of them arrived in the last 57 days. [google-meta-ads-ga4-mcp](/tools/google-meta-ads-ga4-mcp/) is the sharper curve: 2,635 stars total, 1,577 of them inside a 40-day window. [ai-marketing-claude](/tools/ai-marketing-claude/) added 442 over 57 days to reach 2,684, and [aaron-marketing-skills](/tools/aaron-marketing-skills/) added 361 to reach 2,843.

Read those four together and the shape is hard to miss. All four are agent skill repositories: collections of instructions, prompts, and small tools that teach a coding or marketing agent to run campaigns, audit accounts, or interpret ad data. None of them is a platform you deploy. They are the layer you install into an agent you already run.

*The twelve fastest movers by percentage star growth across the full window. The table below carries every repository with its exact numbers.*

## The full board

Here is the complete tracked set. Growth windows differ per row because each one is bounded by the catalog snapshots we actually hold, never by interpolation. Stars are totals as of 26 September 2026.


| Project | Stars | Change | Window | Latest release |
| --- | --- | --- | --- | --- |
| [claude-ads](/tools/claude-ads/) | 9,576 | +1,857 | 57 days | 2026-09-10 |
| [aaron-marketing-skills](/tools/aaron-marketing-skills/) | 2,843 | +361 | 57 days | 2026-09-02 |
| [ai-marketing-claude](/tools/ai-marketing-claude/) | 2,684 | +442 | 57 days | none recorded |
| [google-meta-ads-ga4-mcp](/tools/google-meta-ads-ga4-mcp/) | 2,635 | +1,577 | 40 days | none recorded |
| [openclaw-marketing-skills](/tools/openclaw-marketing-skills/) | 1,045 | -30 | 57 days | none recorded |
| [digital-marketing-pro](/tools/digital-marketing-pro/) | 835 | +165 | 57 days | 2026-07-29 |
| [ai-business-skills](/tools/ai-business-skills/) | 593 | +80 | 57 days | 2026-05-25 |
| [eve-marketing-team](/tools/eve-marketing-team/) | 444 | +13 | 26 days | none recorded |
| [zapier-gtm-cheat-codes](/tools/zapier-gtm-cheat-codes/) | 339 | +7 | 26 days | none recorded |
| [email-marketing-bible](/tools/email-marketing-bible/) | 319 | +68 | 57 days | 2026-03-10 |
| [marketing-studio](/tools/marketing-studio/) | 248 | +28 | 28 days | none recorded |
| [prospectos](/tools/prospectos/) | 226 | +20 | 28 days | 2026-07-27 |
| [alphone](/tools/alphone/) | 177 | -2 | 28 days | 2026-09-25 |
| [n8n-marketing-flows](/tools/n8n-marketing-flows/) | 177 | +3 | 26 days | none recorded |
| [potato-ai-visibility](/tools/potato-ai-visibility/) | 168 | +1 | 26 days | 2026-06-22 |
| [diffmode-growth-tactics](/tools/diffmode-growth-tactics/) | 162 | +3 | 26 days | 2026-06-05 |

A note on release dates: "none recorded" means the repository has no GitHub release objects, not that nothing shipped. Several of these projects commit daily and simply never cut a release. We report what the API returns and do not read intent into the gap.

## The rest is quiet

The remaining projects in the tracked set moved slowly or not at all. Several sat within a few dozen stars of their earlier snapshot across the full window. One went backwards: [openclaw-marketing-skills](/tools/openclaw-marketing-skills/) dropped 30 stars over 57 days, from 1,075 to 1,045. Un-starring is real data, so it stays in the tracker.

## Why the skill layer wins the attention

Three properties of agent skill repositories explain the pattern, and none of them is about quality.

They install in a minute. A platform asks for a deployment, a database, and a migration path. A skills pack asks for a folder. The distance between hearing about a project and running it is near zero, and stars accumulate in that distance.

They ride an existing habit. People who install agent skills already live in a coding or agent environment all day. The install happens where their hands already are. Marketing platforms ask the same people to open a new tab, create an account, and connect billing.

They are cheap to try and cheap to leave. No contract, no seat count, no data migration. That cuts both ways, which is exactly what the openclaw row shows. A skills pack that stops being useful loses its stars as quickly as it gained them.

None of this says the platform layer is in trouble. The tracked platforms quietly hold their numbers, and one harden-and-ship cycle later they still hold the durable part of the stack: the data model, the sending infrastructure, the audit trail. Attention flows to what is new and cheap to try. Value accumulates in what is hard to replace. Two different curves, and conflating them is how teams end up with forty skills and no CRM.

## Is the growth rate holding

The history column carries middle snapshots for the leading repositories, so we can split their windows into two segments and check direction. The comparison is crude with one middle point per repo, but crude and real beats smooth and invented.

claude-ads added 1,424 stars between 31 July and 10 September, about 35 a day, then 433 in the following 16 days, about 27 a day. Decelerating. It remains the fastest absolute grower on the board and the curve is bending down at the same time.

google-meta-ads-ga4-mcp shows the opposite shape. Its entire 1,577-star window sits inside 40 days with no earlier snapshot to compare against, which means we joined its story mid-flight. Roughly 39 stars a day from a repository that had 1,058 in mid-August is a steeper relative climb than claude-ads even at its peak rate.

aaron-marketing-skills added 276 stars in 41 days and 85 in the 16 after, around 6.7 stars a day falling to 5.3. A steady, quiet accumulation with no wave to ride.

Read the direction, not just the totals. Two of the three leaders are decelerating from a high base while the newest curve is still steep. That is the normal shape of attention moving through a layer: the first movers hold the volume, the newest entrant holds the slope, and the totals keep looking impressive right up until the month-over-month change says otherwise. Watch the next snapshot before treating any of these three as a trend.

## What would change this picture

A thesis you cannot lose is not worth publishing, so here is what would break this one.

If the next snapshot shows one of the four leading skill repos flat or negative over a window of 60 days or more, the wave has crested and this post becomes the record of a peak. If platform repositories start adding stars at the same rate as skill packs while keeping their release cadence, the attention argument is wrong and something else is driving adoption. And if the 63 catalog entries that record no repository URL turn out to hold the real momentum, our coverage gap is the story and this table is a biased sample.

We will publish the next run even if it contradicts this one. The dataset history is append-only and the negative numbers stay in it.

That contrast is the finding. The platform layer of open-source martech, tools that store contacts, send campaigns, or analyze traffic, is where the durable value lives. It is not where the attention flows. In 2026 the adoption wave shows up as agent capability first.

## What we publish and how

The [dataset](/oss-momentum.json) gives, per repository: current stars, latest release date, a per-row growth figure with its own window, and the full snapshot history we measured. Two real sources back it. GitHub's repository API provided the fresh totals and release dates. The measurement series comes from the [git history of our own public catalog](https://github.com/TimChr78/martechsignal): every committed snapshot of the tools file, dated by its commit. Anyone can rerun that extraction and get the same series.

Two limits, stated plainly. GitHub's star-timestamp endpoints are not accessible to this project, so growth windows are bounded by our snapshot dates and each row says which window it covers. And only repositories named in a catalog entry are tracked; 63 open-source entries do not record a repository URL and sit outside the dataset rather than being guessed at.

One more mechanic worth knowing. The growth series is stitched from dated snapshots of our own public tools file, committed to the catalog repository as the work happened. Six snapshot dates sit behind the rows above, between 31 July and 26 September. A row whose window says 26 days simply has no earlier snapshot to measure against. We would rather give you a short honest window than a long invented one.

We will refresh the tracker as the catalog snapshots accumulate. If a project in your stack is missing its repository URL, that is a fix worth sending us through the [contact page](/contact/).

## Related reading

- [Fifty days of open-source MarTech, audited](/blog/oss-martech-50-day-checkin/)
- [Autonomous Marketing Platforms Are Real. The Name Is Wrong.](/blog/autonomous-marketing-platform-label-contest/)
- [You Don't Need a New Data Stack for AI. Fivetran Just Proved It](/blog/you-dont-need-new-data-stack-fivetran/)
## Related tools

- [Growth Lab](/tools/growth-lab/) - Open-source skills that run SEO and Xiaohongshu growth loops in Claude Code and Codex
- [SEO Skill Bench](/tools/seo-skill-bench/) - Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects
- [n8n](/tools/n8n/) - Open-source workflow automation platform with AI agent capabilities and 400+ nodes
## Comparison guides

- [Best Agent Skills tools (2026): 8 compared](/best/agent-skills-tools/)
- [Best AI Personalization &amp; CDP tools (2026): 8 compared](/best/ai-personalization-tools/)
## Glossary terms

- [DMP](/glossary/dmp/)
- [DSP](/glossary/dsp/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

**MartechSignal**, written by [Tim Christensen](/authors/tim-christensen/)
