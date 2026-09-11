---
title: "Check outputs, not logs: the silent-failure audit"
seo_title: "Check outputs, not logs: the silent-failure audit"
slug: silent-failure-audit
date: 2026-09-10
author: Tim Christensen
tags: [Automation, AI Agents]
categories: [workflow-automation, agent-skills]
---
An n8n user who goes by Salman94157 ran WhatsApp automations in production for months before [posting what went wrong](https://www.reddit.com/r/n8n/comments/1vr6pcf/my_whatsapp_automation_ran_green_for_3_weeks/) in r/n8n last month. The headline of his post says it all: "My WhatsApp automation ran green for 3 weeks while quietly dying." His bot had been "replying" to expired conversations for days. WhatsApp's 24-hour window had closed on those chats, so the platform refused free-form replies and only accepted pre-approved templates. Every single n8n execution showed success, because the send request itself went through fine. WhatsApp was silently not delivering, and the delivery failure (error code 131047, which [Meta's docs define](https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes) as "more than 24 hours have passed since the recipient last replied") arrived later on a status webhook that nobody had wired up.

Three weeks of a customer-facing channel, dead. Not one red light.

The comments under that post are the most useful practitioner thread on silent automation failure I have read this year, and they converge on one uncomfortable point: none of these failures are errors, so none of your error handling is even connected to them. This post turns that into a repeatable audit. It is also the missing second half of [this week's blast-radius audit](/blog/automation-blast-radius-audit/), which sorted your automations into four quadrants and told you where detection has to exist. This one tells you how to build the detection.

## "Success" is a word the platform defines

Before the procedure, be clear about what green actually means on the major platforms, because the vendors document it honestly and almost nobody reads it.

Make's [Skip error handler](https://help.make.com/skip-error-handler) documentation (updated September 8, 2026) says the quiet part out loud: the handler "prevents turning off the scenario when there's an error and marks the scenario run as a success even in case of errors." Make even tells you when that trade is fair: use Skip "when incorrect data in your scenario has no impact on your processes and occasional data loss is acceptable." Someone made that judgment the day the scenario was built, usually under deadline pressure, usually about one field. The audit asks whether it is still true for every bundle the handler will ever swallow.

Zapier's [run status documentation](https://help.zapier.com/hc/en-us/articles/20505304170637-Review-run-statuses-in-Zap-workflows) lists eleven statuses, and the interesting ones are not errors either. `Filtered` means a filter step stopped the run, so no subsequent steps executed at all. `Handled error` means an error handler caught a failure and ran an alternative path, and Zapier notes that a Zap with a handled error "will not turn off automatically" no matter how many times it happens. A Zap can run wrong every day for a month and its history stays free of anything you would notice while scrolling.

In n8n, the mechanism is a node setting called "continue on fail." One commenter in the thread, Ok-Category2729, diagnosed a customer's broken WhatsApp integration to exactly that: "every execution showed green because it never threw, but the send message step was silently failing." He then stated the mental model the whole audit rests on: n8n success means the execution finished, not that the intended thing happened.

| Platform | What "success" certifies | What it can hide |
|---|---|---|
| Make (Skip handler) | The run completed; failed bundles were dropped | Any data loss the builder once called acceptable |
| Zapier | The run completed or an error was handled | Filtered runs where nothing executed; errors handled forever without escalation |
| n8n | The execution finished | Nodes with "continue on fail"; steps whose API call succeeded but whose effect didn't |
| WhatsApp Cloud API (any tool) | The POST returned 200 | Delivery failures like 131047 that arrive later, on a webhook you may not subscribe to |

A 200 response is a receipt for the request. The outcome shows up later, somewhere else, or never.

## The audit: five automations, five steps

The blast-radius audit sorted your stack into quadrants using two questions: can you undo it, and can customers see it. The two right-hand quadrants, "fires, then tells someone" and "fires, but has to shout," both assume something tells you when a run does the wrong thing. For failures that produce no error, nothing will tell you unless you build it. Five automations, five steps, one working session.

::: wf-step
**Step 1: Pick your five highest-blast-radius automations.** Pull your quadrant sheet from the blast-radius audit. Take every row marked not-undoable, plus any row where the gate/siren column says "none." Rank those by what a wrong run costs over a week: a misfire that emails customers beats one that dirties an internal sheet. Take the top five and ignore the rest for now. Five is the cap because fifteen audits get started and none get finished.
:::

::: wf-step
**Step 2: Write the expected outcome per run, as a checkable fact.** One line per automation, and it must be a noun or a number, not a verb. "Syncs form data" is useless. "Adds exactly one row to the Responses sheet per form submission" is checkable. "Emails only contacts whose newsletter_opt_in is true and whose signup is less than 90 days old" is checkable. If you cannot write the expected outcome for an automation, you do not fully understand what it does, and that is the audit's first finding.
:::

::: wf-step
**Step 3: Instrument a verification step that reads the destination, not the workflow.** The log lives inside the system that already believes it succeeded. The check has to live downstream, in the place the automation was supposed to affect. Three patterns from the thread, cheapest first:

- **The canary.** Commenter OkOpposite8159 built this after his inbound path died for days while outbound stayed green and every webhook test he ran manually still passed: a second phone number messages the bot every morning, and an alert fires if nothing comes back. One scheduled probe per direction of every two-way automation. Dumber than any monitoring product and it catches what monitoring products miss, because it tests the outcome the way a customer would.
- **The outcome count.** Commenter catchleak's fix was "to stop watching executions and start watching outcomes": one scheduled workflow that asks a question whose answer is a number. How many inbound messages did we store in the last 24 hours? How many rows did the sync add? How many messages did the send API accept, and how many does the delivery report say landed? Compare against the expected fact from step 2 and alert on any gap. This is the pattern that would have caught the original 3-week failure on day one.
- **The inline assertion.** Ok-Category2729's rule: after each external API call, an IF node validates that the response contains what you expect (for a WhatsApp send, that `messages[0].id` exists) and throws deliberately if not. Then turn off "continue on fail," Skip handlers, and error handlers everywhere except where you consciously want fallback behavior, and make every one you keep send a notification. A Skip handler that silently drops bundles and a Skip handler that pings a channel on every drop are different tools with the same name.
:::

::: wf-step
**Step 4: Subscribe to the platform's truth channel.** Every platform that can fail after accepting your work publishes the failure somewhere other than the run log. For WhatsApp, commenter slunkeh listed the set: subscribe to the message status webhooks plus `message_template_status_update` and `account_update` on the business account, poll the phone number's quality rating once a day, and alert if it drops off GREEN. One caveat from commenter ManufacturerLast7833 worth internalizing: the quality rating is a trailing signal. "By the time your number drops off GREEN, Meta has already decided." The leading signals are reply rates, read rates, and blocks on recent sends. The same shape exists everywhere: email has bounce and complaint webhooks, CRMs have field history, ad platforms have change history. Write down the truth channel next to each of your five automations, or write "none found," which is also a finding.
:::

::: wf-step
**Step 5: Record it and break something on purpose.** One sheet: automation, expected outcome, verification pattern, truth channel, last checked, last mismatch found. Then test one check by causing the failure it watches for: pause the webhook receiver, corrupt one row, send from the canary number with the bot switched off. A verification step that has never fired on a real mismatch has never been tested. It might be watching the wrong field, the same way the original thread's team watched execution logs that could not see their problem.
:::

One disclosure, same as last time. The thread is mixed: one commenter uses it to plug their own inbox product, so read that reply accordingly. The failure reports and the fix patterns come from several independent practitioners who run production WhatsApp and n8n stacks, and they agree with each other in the details (specific error codes, specific node settings), which is the part that is hard to fake.

## What this does not do

Two honest limits. First, the audit catches wrongness you can describe. If you cannot write the expected outcome in step 2, no verification step will save you, and the real problem is that the automation encodes a decision nobody wrote down. Second, a canary tells you the pipe is broken, not that what flows through it is good. The original poster's worst failure, sending 500 messages to a list that was never properly opted in, would pass every mechanical check in this post. Delivery checks catch delivery failures. Consent and judgment stay human, which is exactly where the blast-radius quadrant put them.

::: verdict warn
**The verdict: a green run certifies that the execution finished, and nothing more.** Make marks skipped errors as success, Zapier keeps handled-error Zaps running forever, n8n greens any run with "continue on fail," and WhatsApp returns 200 for messages it will never deliver. Pick your five highest-blast-radius automations, write the expected outcome for each as a checkable fact, verify it downstream in the destination system, and subscribe to whatever truth channel the platform publishes. Then break something on purpose to prove the check works. The whole procedure costs an afternoon, which is less than three weeks of a dead channel.
:::

<div class="cta-strip">
<h3>Compare automation platforms on observability</h3>
<p>Our directory reviews workflow and marketing automation tools on what happens after "success": error-handler behavior, status webhooks, run history you can query, and whether the platform tells you when a delivered thing was the wrong thing.</p>
<a class="btn" href="/categories/workflow-automation/">BROWSE WORKFLOW AUTOMATION →</a>
</div>

**Sources:** [r/n8n: My WhatsApp automation ran green for 3 weeks while quietly dying (retrieved Sep 11, 2026)](https://www.reddit.com/r/n8n/comments/1vr6pcf/my_whatsapp_automation_ran_green_for_3_weeks/) · [Make Help Center: Skip error handler (updated Sep 8, 2026)](https://help.make.com/skip-error-handler) · [Zapier Help Center: Review run statuses in Zap workflows](https://help.zapier.com/hc/en-us/articles/20505304170637-Review-run-statuses-in-Zap-workflows) · [Meta for Developers: WhatsApp error codes](https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes)
