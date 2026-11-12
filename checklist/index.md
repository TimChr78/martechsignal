# Marketing Automation Checklist: 12 questions, 2 phases

## Marketing Automation Rollout Readiness Checklist

Twelve questions, two phases: get Phase 1 right before you deploy anything, Phase 2 before you plug AI agents into what you deployed. Tick what is true today - the score is yours alone; nothing is submitted.

*Prefer paper?* Use your browser's print (Ctrl/Cmd-P) - this page prints as a clean one-sheet checklist. Or copy your results below.

Score one point for every statement that is true today. There is no partial credit and no weighting: a box is either true or it is not, and "we are migrating in Q3" counts as a no. The two phases are ordered on purpose. Phase 1 covers the plumbing any deployment depends on. Phase 2 covers what an agent needs before it can act on that plumbing without supervision.

## Phase 1 - Rollout readiness

Answer these before you buy or deploy anything.

## Phase 2 - Agent readiness

Answer these before you hand the keys to an agent.

Interactive scoring needs JavaScript - the printed page works without it.

Want the fixes, not just the score? The MartechSignal newsletter covers exactly the gaps you just checked, one tool at a time. Free.

Send me the weekly newsletter. Unsubscribe any time.

## How the 12 questions are scored

Each question is worth one point, and the total is the number of statements that are true right now. That is the whole mechanic. The rest of this section explains what the number does and does not tell you.

- **One point per true statement.** A half-answer is a no. If you can export some journeys from one tool but not the rest, the answer to question 1 is no.
- **No weighting.** The list does not rank one question above another, because all twelve are prerequisites rather than preferences. A weighted score would imply you can trade a consent gap against a template win, and you cannot.
- **Today, not the roadmap.** Tick only what is already working in production. Intentions score nothing, and a plan to fix something is exactly the gap the checklist is trying to surface.
- **Two phases, one count.** Questions 1 to 7 are rollout readiness and questions 8 to 12 are agent readiness, but the score adds them together. Read the total first, then read which phase the missing points sit in. A 9 that is missing a Phase 1 safety question is a worse position than an 8 with all of Phase 1 and only two Phase 2 items.
- **Nothing is submitted.** Your ticks stay in the browser, and the URL fragment records which boxes are ticked, so a reload or a shared link keeps your state. The only thing that leaves is the email address you choose to type into the newsletter box.
## What each score band means

The bands below are reading guidance, not a certification. They describe what a count usually implies about where to spend the next month.

### 0 to 4: foundation gaps

Most of the plumbing is missing or undocumented. Buy nothing and automate nothing yet. Start with the questions whose absence can cause an incident rather than an inconvenience: consent and suppression access, approval workflows for automated sends, and cost guardrails on ad platforms. Export, UTM discipline, and a single source of truth can follow once the safety items are true.

### 5 to 8: partial plumbing

Some of the stack is ready and some of it is being held together by habit. The useful move is to finish Phase 1 before starting Phase 2 work. A team at this level often wants to pilot an agent because the pilot is visible and the plumbing is not. Resist that until the unchecked Phase 1 boxes are closed, then re-score.

### 9 to 11: nearly ready

The foundation holds and the remaining gaps are narrow. Read them individually, because at this level the count hides more than it shows. Missing version control is a different problem from missing programmatic segmentation, and a safety gap inside Phase 1 still outranks a convenience gap inside Phase 2.

### 12: ready as far as this list goes

Every statement is true today. That is a floor, not a certificate. The checklist tests whether the pieces exist, not whether they are good, current, or exercised under load. Re-score after any platform migration, reorg, or change of agency, because every one of those can quietly turn a yes back into a no.

## Two worked examples

Both teams below are hypothetical. The counts are illustrative, and the point is the reading order, not the arithmetic.

### A team at 7 out of 12

This team can segment programmatically, has APIs, a single source of truth, cost guardrails, modular templates, version control, and cross-dashboard reporting. It cannot export its full journey as structured data, its UTM convention is undocumented, automated sends have no approval workflow, consent and suppression are not reachable by API, and a campaign cannot yet run end to end without opening a browser.

The count says partial plumbing. The phase split says stop. Two of the missing Phase 1 items are safety-relevant: consent access and approval for automated sends. Fix those first, then the export, then UTM discipline. The missing browser-free run can wait, because an agent that cannot reach suppression or approvals should not be sending at all, however well the templates are built.

### A team at 10 out of 12

This team is missing two Phase 2 items: automation logic is not version-controlled, and a campaign cannot run end to end without opening a browser. Everything in Phase 1 is true.

The band says nearly ready, and the phase split agrees. The two gaps are the pair that decides whether an agent can work unattended. Version control comes first, because an agent editing logic you cannot diff is a change you cannot review or roll back. The browser-free run is the last box to earn: pilot it with a human approving the send, and only remove that person once the run is boring.

0/12

Tick what applies today.
