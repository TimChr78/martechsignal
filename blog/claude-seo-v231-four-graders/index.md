# Five Claude SEO Scores, Four Graders: None Compare

AI · SEO · 7 MIN

Home · Blog · Four Graders, One Site: What Five Claude SEO Scores Measure

SEP 18, 2026 · Updated SEP 25, 2026

Filed under Agent Skills

We have pointed the open-source Claude SEO skill at martechsignal.com five times since August. Scores: 83, 61, 74.6, 80, 76.6. None of them compare.

That last sentence is the whole argument, so here is the defense. Four grading setups produced those five numbers: v2.2.4, v2.2.5, the September R2 re-audit, and v2.3.1. Claude SEO rewrites its gates, specialists, and rubric weights with most releases, so every version bump changes what the number means. Treat the score like a credit rating and you will read a tool upgrade as your site getting worse. We made that mistake publicly in August. Five audits later, we have a cleaner model: the score is an instrument reading, and instruments get recalibrated.

## The five scores, and which grader produced them

(v2.2.4 also scored us 92 and then 96 across two August re-runs as we fixed what it found. That run-up, and the 61 that followed the upgrade, are covered in the 61-vs-92 post. The first audit itself is in the original teardown.)

Only one pair in that table shares a grader: 61 and 74.6, both v2.2.5, one day apart. That delta is real. We fixed things and the same instrument measured the improvement. Every other step mixes site changes with rubric changes, and nobody can decompose that after the fact.

The 80 to 76.6 step is the sneaky one. Between September 8 and September 16 we shipped fixes, not regressions, yet the number went down because v2.3.1 grades differently and brought a new specialist that found something ugly. If we had been watching only the aggregate, we would have spent that week hunting for damage that did not exist.

## What v2.3.1 actually said

Category scores from the September 16 run:

The E-E-A-T breakdown: Expertise 82, Trust 76, Experience 62, Authoritativeness 48.

Authoritativeness is the ceiling holding the rest down. The tool can verify our markup, our page speed, and our content structure from the crawl. It cannot verify that anyone else considers this site worth citing, and 48 is its way of saying there is no external evidence yet.

## The 5/100 that mattered more than the 76.6

v2.3.1 added a Backlinks specialist. Ours found five referring domains, traced all five to a single spam network, and counted zero legitimate links in the site's first five months. The category is unweighted in the aggregate, so the 76.6 barely moved. We think that weighting choice is wrong for a site our age, because it let the headline number bury the most consequential finding in the report.

Five months live and zero real links is a distribution problem, not a technical SEO problem. No amount of schema repair fixes it. The aggregate had been flattering us for a month, and the one number that got no weight was the one we keep thinking about.

## v2.2.6 through v2.3.1: fixes self-hosters should read

Between our August and September audits the project shipped three releases of security work. If you run audits on a cloud VM, some of these were credential-theft paths, not theoretical bugs.

The proxy fix is the one to underline. Before v2.3.0, if that environment variable pointed at a hostile value on the machine where you audit, the tool itself became the SSRF payload. Update before the next run, not after.

## What we fixed on our own site within a day

The September 16 report produced four changes we shipped inside 24 hours.

1. Our tool pages emitted AggregateRating schema with reviewCount: 0. Star ratings with no reviews behind them are a manual-action risk under Google's structured data policy. The template now gates that markup so it cannot ship again.

2. Our Semrush review contained a paragraph describing hands-on use of Semrush. We have never run it. The audit flagged the claim as unsupported, we deleted the paragraph, and the review now states what we did and did not test. This is the second time the grader caught something our own editorial pass missed, and the first time what it caught was a fabrication. Publishing that admission is the point of this site.

3. Seventy-six pages rendered large numbers as "150, 000", with a stray space after the comma. A locale artifact in the generator, fixed at the source.

4. We dropped self-serving Review schema from our own pages. Marking up our directory's reviews as if they were third-party endorsements is the kind of thing Google's guidelines name explicitly.

## Why graders disagree, and why that is the finding

Four graders, one audit, and a spread wide enough to change decisions. The disagreement is not a scandal. It is what happens when three things vary at once. The rubric differs: what each grader weights as a category, and how it treats the same measured fact. The weights differ: the same sub-scores produce different totals when a rubric values links or schema differently. And the model behind the grade differs, because a reasoning grade is a judgment call with a temperature whether or not anyone names it.

The useful reading of the spread is the uncertainty band. A tool that reports one number without its band is not more accurate than four graders. It is less honest. When the same site scores meaningfully differently depending on the instrument, the policy decision should not hinge on which instrument you happened to run, and any fix list worth acting on should be stable across the band. Ours mostly was, which is the part of the experiment that actually mattered.

## Who should run this tool

Run Claude SEO if you want a prioritized, evidence-linked audit and can treat each grader version as a new baseline. Pin your comparisons: re-run within one version to measure your fixes, and when the tool upgrades, do not diff the new score against the old one. Read the unweighted specialists, since the aggregate buried our worst number for a month. Skip it if you need a single score that stays comparable across quarters; that is a job for a deterministic crawler with fixed rules, not a judgment grader.

Five audits in, the pattern is consistent: the findings keep giving us work we act on, and the score keeps being the least dependable part of the report.

One sourcing note. Every score in this post comes from an audit we ran against our own production site, and the category and E-E-A-T figures are from the saved September 16 v2.3.1 report.

## Related reading

- Claude SEO v2.2.5 Re-Scored Us 61. Both Audits Were Right.
- I Ran Claude SEO on My Own Site. It Found What Our Pipeline Missed.
- Claude SEO vs Seonaut: which free SEO checker should you run
## Related tools

- SEO Skill Bench - Open benchmark that scores Claude Code SEO skills against fixture sites with planted defects
- Claude Ads - Paid-media operations skill for Claude Code covering 12 ad platforms
- Nightwatch - Rank tracking across Google and AI answers, priced by keyword with unlimited seats
## Comparison guides

- Best workflow automation tools (2026)
- n8n vs Zapier (2026): self-hosted depth or catalog breadth
## Glossary terms

### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

More from the directory: GrowthBook
