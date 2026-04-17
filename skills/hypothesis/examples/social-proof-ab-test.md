# Example: Creating a falsifiable hypothesis from a vague belief

**User says:** "I want to track a hypothesis that adding social proof on the pricing page will increase conversion."

**Context:** `.jeff/HYPOTHESES.md` has two prior hypotheses, both validated. `.jeff/OPPORTUNITIES.md` has an opportunity O4 about "visitors don't trust the product is used by real teams."

**Claude's turn 1:** Ask for specificity.

> "Good starting point. Three things to pin down:
> - **What** specifically counts as 'social proof' here — logos, quotes, numbers, something else?
> - **Who** are we targeting — all visitors, paid-traffic visitors, returning visitors?
> - **What** metric are we moving — signup conversion, paid-plan selection, something else?"

**User:** "Customer logos, first-time visitors from paid traffic, signup conversion rate."

**Claude's turn 2:** Ask for a threshold.

> "What signup conversion lift would count as 'yes this worked'? If we saw +2%, would that be enough, or does it need to be +15%?"

**User:** "15% minimum. Anything less and it's noise."

**Claude's turn 3:** Confirm falsifiability.

> "Good — and that makes the hypothesis falsifiable. If we see +5%, we say 'no, social proof alone doesn't move conversion enough to matter,' and we move on. Confirming: **risk level**? If we're wrong and ship it anyway, what's the cost?"

**User:** "Feature-level, easy to revert. Medium risk."

**Claude's turn 4:** Propose a method proportionate to risk, push back on over-engineering.

> "Medium risk, measurable metric, real traffic needed — an A/B test fits. But before we commit: could a prototype or fake door teach us anything cheaper first? Probably not here — social proof's effect is behavioural and needs real traffic. A/B it is.
>
> Statement: _We believe that **adding customer logos above the pricing table** will result in **higher signup conversion** for **first-time visitors from paid traffic**, which we'll measure by **signup conversion rate** with a threshold of **+15% vs. control**._
>
> Recording as **H3**, status **Untested**, linked to O4."

**Claude's turn 5:** Pin down *how to run it* before writing the entry.

> "Before I record this, let's spell out the run plan so whoever picks it up can execute without guessing:
> - **Setup** — logo strip (6 customer logos, grayscale) above pricing table, behind `pricing_social_proof` flag, 50/50 split on first-time paid-traffic visitors. Amplitude event `pricing_page_viewed` already exists; confirm `signup_completed` fires with `experiment_arm` property.
> - **Run conditions** — 50/50 traffic, run until 5,000 signups per arm or 14 days, whichever first. Stop early only if p < 0.01 against the treatment (guardrail against shipping a loss).
> - **Measurement** — Amplitude funnel `pricing_page_viewed → signup_completed`, segmented by `experiment_arm`, paid-traffic cohort only. Pull at stop; record both arms' conversion and the lift.
>
> That looks runnable. Writing it up."

**Claude writes to `.jeff/HYPOTHESES.md`:**

```markdown
## H3 — Customer logos on pricing page increase signup conversion
- **From opportunity**: O4 (visitor trust)
- **Statement**: We believe that adding customer logos above the pricing table will result in higher signup conversion for first-time visitors from paid traffic, which we'll measure by signup conversion rate with a threshold of +15% vs. control.
- **Metric**: signup conversion rate (paid-traffic cohort)
- **Threshold**: +15% lift, p < 0.05
- **Risk**: M (feature-level, easily reverted)
- **Method**: A/B test
- **Experiment plan**:
  - **Setup**: grayscale customer-logo strip above pricing table, behind `pricing_social_proof` flag. Confirm `signup_completed` event carries `experiment_arm` property before launch.
  - **Run conditions**: 50/50 split on first-time paid-traffic visitors. Stop at 5,000 signups per arm or 14 days, whichever first. Early-stop only if treatment is losing at p < 0.01.
  - **Measurement**: Amplitude funnel `pricing_page_viewed → signup_completed`, segmented by `experiment_arm`, paid-traffic cohort. Pull conversion and lift for both arms at stop.
- **Status**: Untested
```

**What to notice:** Claude refused to record the vague first version ("social proof will increase conversion") and only proceeded once the user could name the *specific* treatment, *specific* cohort, *specific* metric, and *specific* threshold. That's the hypothesis formula doing its job — forcing precision before experiments get scheduled.
