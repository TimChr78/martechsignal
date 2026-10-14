# Where manual work hides in marketing automation

MARKETING AUTOMATION · MARKETING OPS · 6 MIN

## Where the manual work still hides in your marketing automation

[How we review](/methodology/) · No affiliate links

[Home](/) · [Blog](/blog/) · Where the manual work still hides in your marketing automation

OCT 14, 2026

Filed under [Marketing Automation](/categories/marketing-automation/) · [Workflow Automation](/categories/workflow-automation/)

Building the campaign is the fast part. In a recent [r/MarketingAutomation thread](https://www.reddit.com/r/MarketingAutomation/comments/1x1t6re/where_does_the_manual_work_still_happen_in_your/), a CRM and lifecycle marketer put it plainly: "setting up the actual automation is rarely the part that takes the longest." Decide the trigger, decide the audience, and the flow itself takes an afternoon. Then the campaign still needs writing, design, images, links, personalization, testing, and a move into the platform. That is where the afternoons go.

The thread asked where the time goes between deciding to run a campaign and having it ready to schedule. Seven comments came back from six practitioners, and not one described slow flow building. The answers cluster in five places, and every one of them sits downstream of the automation everyone demos.

**About the source.** This is one Reddit thread, not survey data: seven visible comments, self-selected respondents, and no scores to weigh them by. The original poster also says they are building a small tool around the problem, so expect some market discovery mixed in with the scars. Direction, not statistics.

## Work hours and wait hours

The sharpest framing came from u/Brufacee: "Copy might take an hour but sit with reviewers for three days. Those need quite different fixes, even if both get called manual work." Both kinds of time look identical on a calendar, and most teams track only the first kind.


|  | Work hours | Wait hours |
| --- | --- | --- |
| **What it is** | Writing, building flows, running tests | Review queues, legal sign-off, asset requests |
| **Scales with** | Campaign complexity | Headcount and process, not complexity |
| **How to see it** | Time-tracking the build itself | Timestamps between status changes |
| **How to shrink it** | Templates, snippets, executable checklists | Fewer approvers, diff-based review, modular approval |

Fix the wrong column and nothing moves. A faster builder saves an hour for a team whose campaign spends three days in a review queue.

## The approval loop

u/squealingstocks38: "I can build the flow in an afternoon but then it sits for days while three different people leave comments on the email draft." And then, they add, "legal wants to see the final version even though nothing changed since the last one they approved." u/achakez has the same story at a different scale: "You can have the whole flow ready in an afternoon and then spend a week waiting for people to approve two lines nobody actually changed."

Three changes shrink this. Approve reusable modules once, so legal reviews a diff instead of a document. Cap the reviewer list to people whose comments change the send. Make re-review conditional on change, which requires the version proof in the last section. All three are process fixes, which is exactly why they survive the next tool change.

## QA

"The setup is easy; QA is the real bottleneck," as u/Curious_Bed_3361 puts it. The same commenter itemizes it: "Broken links, incorrect merge tags, and inconsistent rendering can turn a quick campaign into hours of testing." Add u/TowerSenior4427's mobile previews and dark mode, and you have the full Friday-afternoon ritual.

The fix is to make the checklist executable. Crawl every link in a finished build. Render the merge fields against a seed set of test profiles that includes empty values and worst-case-length names. Preview the top email clients plus dark mode on every send. A checklist a script can run stops being a ritual. The failures it catches are the quiet kind, the ones nothing logs until a customer hits them, and we laid out the audit pattern in [Check outputs, not logs](/blog/silent-failure-audit/).

The platform matters less than you would think. [HubSpot](/tools/hubspot-marketing-hub/), [Marketo](/tools/adobe-marketo/), and [Salesforce Marketing Cloud](/tools/salesforce-marketing-cloud/) all expose the same primitives: link tables, merge fields, preview modes. What differs is whether anyone bolted the checks together. Vendors have noticed the gap. [Braze](/tools/braze/) announced Agentic Standards at its Forge conference in September, which hands campaign QA to agents that audit journeys against brand and compliance rules and log what they find. We covered the details in [our piece on the announcement](/blog/braze-ai-campaign-operations/).

## Variants and the UTM tax

u/TowerSenior4427 names the sink most people skip over: "moving the same content between tools, keeping UTMs consistent, checking dynamic fields and links, previewing mobile and dark mode, and proving which version was approved." Their own proposed fix has the right shape: "A canonical draft that generates channel-ready variants, plus a QA checklist and approval log, would remove a lot of that friction."

One canonical source per campaign, with channel variants emitted from it, kills most of the copy-paste. Generate [UTM parameters](/glossary/utm-parameters/) from the campaign's metadata instead of typing them by hand; UTM drift is invisible until attribution breaks. The integration layer, [Zapier](/tools/zapier/), [Make](/tools/make/), or [n8n](/tools/n8n/), moves content between systems fine. The part it cannot do for you is the naming rules, and those belong in a validation step before export, not in a style guide nobody opens.

## Image hunting

u/squealingstocks38 again: "always hunting for something that doesn't look like every other stock photo we've used before." This one shrinks by subtraction. A small, rights-cleared, tagged library beats a large one, because the search space is the cost. Prune it yearly. If AI-generated imagery is in play and your industry has no rules for it yet, expect a new approval step to attach itself to this hunt too.

## Nobody can prove which version shipped

The thread's most underrated line is a clause: u/TowerSenior4427's "proving which version was approved." It shares a root cause with legal re-reviewing unchanged drafts. When nobody can diff the approved version against the current one, everything re-enters review, and the approval loop never closes.

Make the approval log an artifact the workflow emits, not a memory. Export the approved version with an ID and a date, archive it alongside the send record, and diff every re-review against it. This is the audit-trail argument we made about autonomous stacks: the [approval step is load-bearing](/blog/autonomous-stack-loophole-approval-step/), and an approval nobody can reconstruct afterwards is not.

## What to automate next

Order matters more than ambition. The deterministic checks come first: link validation, merge-tag tests against a seed profile set, UTM generation, rendering previews. They need no judgment, machines do them reliably, and every send benefits. The approval queue comes second: module-level sign-off, diff-based re-review, an emitted approval log. Content generation comes last, because it is already the cheapest step in the chain and the bottleneck sits downstream of it. Automating copy while the queue stays the same just feeds the queue.

That is also the argument against buying your way out with another assistant, which we made in [Why your marketing automation stack doesn't need another AI tool](/blog/why-your-marketing-automation-stack-doesnt-need-another-ai-tool/). The hours this thread describes are not where those tools look.

Automate the checks before the words. Link validation, merge-tag tests, UTM generation, and dark-mode previews need no judgment, so software runs them better than any reviewer and nobody waits. Rebuild the approval queue second: module-level sign-off and diff-based re-review attack the three-day sits the thread complains about. Generation comes last. It is the cheapest step already, and adding volume upstream of a slow queue lengthens the queue.

*Tools linked in this post:* [HubSpot](/tools/hubspot-marketing-hub/) | [Marketo](/tools/adobe-marketo/) | [Salesforce Marketing Cloud](/tools/salesforce-marketing-cloud/) | [Braze](/tools/braze/) | [Zapier](/tools/zapier/) | [Make](/tools/make/) | [n8n](/tools/n8n/) | [UTM parameters](/glossary/utm-parameters/)

## Related reading

- [Your autonomous stack's loophole is the approval step you deleted](/blog/autonomous-stack-loophole-approval-step/)
- [Check outputs, not logs: the silent-failure audit](/blog/silent-failure-audit/)
- [Your AI Marketing Agent Doesn't Need Better Prompts](/blog/ai-agents-need-campaign-state/)
## Related tools

- [Zapier GTM Cheat Codes](/tools/zapier-gtm-cheat-codes/) - Zapier's installable coding-agent skills for GTM: campaign planning, CRM context, customer proof
- [Persado](/tools/persado/) - AI content creation and optimization platform for regulated financial services marketing
- [Bloomreach](/tools/bloomreach/) - AI-powered commerce experience platform with search, personalization, and CDP
## Comparison guides

- [Best AI Marketing Automation tools (2026): 8 compared](/best/ai-marketing-automation-tools/)
- [ActiveCampaign vs HubSpot CRM (2026): pricing, automation](/vs/activecampaign-vs-hubspot/)
## Glossary terms

- [AI Agent](/glossary/ai-agent/)
### One email. Every Friday.

The AI tools, workflows, and vendor moves that actually matter for marketing automation. Five minutes, not an hour.

**MartechSignal**, written by [Tim Christensen](/authors/tim-christensen/)

✓ The order that works
