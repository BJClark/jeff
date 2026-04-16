# jeff-hypothesis — Anti-Patterns & Edge Cases

## Non-falsifiable hypothesis

**Detection.** The hypothesis describes a directional improvement with no threshold, or talks about feelings with no measurement ("users will be happier").

**Why it's bad.** Any result can be spun as a win. The experiment confirms the belief regardless of outcome.

**Redirect.** "What numerical result would make you say 'no, this is wrong'?" If they can't answer, park the hypothesis until they can.

## Vanity-metric threshold

**Detection.** Metric is a vanity number (total signups, pageviews) that moves with seasonality, marketing spend, or launch bumps unrelated to the change.

**Why it's bad.** You can't attribute movement to the change. The test doesn't isolate the variable.

**Redirect.** Prefer conversion rates, cohort retention, per-user behaviours. "What rate or ratio are we actually changing?"

## A/B test on low-risk hypothesis

**Detection.** Risk: Low, method: A/B. Threshold: "any improvement."

**Why it's bad.** Weeks of traffic for a decision that doesn't need weeks of rigour. Opportunity cost: the engineering/analysis time is better spent on higher-risk hypotheses.

**Redirect.** Fake door or prototype. If the hypothesis is genuinely "Low risk," a week of qualitative signal is enough.

## Prototype on high-risk pricing or monetisation hypothesis

**Detection.** Risk: High, method: Prototype. Hypothesis involves willingness to pay, plan migration, or churn.

**Why it's bad.** Prototypes give qualitative, small-N signal. Pricing decisions need behavioural signal with N in the hundreds.

**Redirect.** Escalate to fake door (with pretend checkout) or A/B test. Prototypes are useful for usability, not economics.

## Invalidated hypothesis resurrected without new evidence

**Detection.** User proposes a new hypothesis that matches the text of a prior `Invalidated` entry.

**Why it's bad.** Running the same experiment twice wastes the same amount of time twice. Unless something genuinely changed (market, users, product state), the result will repeat.

**Redirect.** Ask: "What's different this time? New audience, new product state, new metric?" If nothing, point at the prior invalidation and stop.

## Hypothesis with no link to an opportunity or outcome

**Detection.** Hypothesis exists in `HYPOTHESES.md` but cites no `OPPORTUNITIES.md` ID or business outcome.

**Why it's bad.** Even if validated, it won't connect to anything. The team will run the experiment and then not know what to do with the result.

**Redirect.** "Which opportunity does this hypothesis come from? What outcome does moving this metric serve?" If neither exists, park the hypothesis until the OST catches up.

## Running five experiments at once

**Detection.** `## Active Hypotheses` has five or more untested entries.

**Why it's bad.** Teams that run many experiments in parallel often run none well. Results collide (two experiments on the same user cohort), ownership blurs, follow-through slips.

**Redirect.** Prioritise: which two experiments would teach the most this month? Deprioritise the rest.

## Stale active list

**Detection.** Hypothesis has been `Untested` for >30 days and no instrumentation or experiment is in progress.

**Why it's bad.** A hypothesis that's been stale for a month is either solved in the team's head without being recorded, or forgotten. Either way the list is lying.

**Redirect.** For each stale entry: "Are we still testing this, or is it effectively deprecated?" If deprecated, move to an `## Abandoned` section with a note about why.
