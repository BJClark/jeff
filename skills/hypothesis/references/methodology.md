# Hypothesis-Driven Development — Methodology

Based on Laura Klein, *Build Better Products* (Rosenfeld, 2016). The core claim: every product decision is a hypothesis about user behaviour until it's tested. Treating decisions as hypotheses — with metrics, thresholds, and falsifiable predictions — is how teams avoid shipping confidence that isn't backed by evidence.

## What makes a good hypothesis

### Specific
"Users want faster checkout" is too vague — it can't be tested. "Adding Apple Pay will increase checkout conversion for iOS users" is specific. You can measure it.

### Measurable
The hypothesis references a metric that exists (or will exist by the time the experiment runs). "Users will feel less frustrated" isn't measurable without a survey instrument. "Session-to-purchase conversion rate" is.

### Falsifiable
There's a result that would make you say "no, this is wrong." If nothing could disprove the hypothesis, it's not a hypothesis — it's a wish. Klein's rule: if you can't describe the failing outcome, don't bother running the experiment.

### Threshold-driven
A hypothesis with "will improve" is a coin flip. A hypothesis with "+15% conversion" gives you something to compare results against. Even a rough threshold beats no threshold.

### Risk-proportionate
The validation method matches the cost of being wrong. A Low-risk hypothesis ("the button should be blue") doesn't deserve a four-week A/B test. A High-risk hypothesis ("users will pay 3× the price") shouldn't be settled with a prototype.

## The hypothesis formula

> We believe that **[specific change]** will result in **[expected outcome]** for **[target users]**, which we'll measure by **[metric]** with a threshold of **[number]**.

Filled in:

> We believe that **adding customer logos above the pricing table** will result in **higher trial sign-up conversion** for **first-time visitors from paid traffic**, which we'll measure by **signup conversion rate** with a threshold of **+15% vs. control**.

This structure forces every component to show up. Missing pieces are visible.

## Recording results

Every hypothesis ends in one of three statuses:

- **Validated** — results met or exceeded the threshold. Proceed.
- **Invalidated** — results clearly fell short. Stop, learn, pivot.
- **Inconclusive** — results were directionally positive but below threshold, or statistical power was insufficient. Decide whether to rerun with more traffic/time, or abandon.

**Never delete invalidated hypotheses.** They're the most valuable output of the process — they tell future-you which ideas have already been tried and failed. A team that deletes failures reinvents them every quarter.

## Relation to the OST

Hypotheses often come from `OPPORTUNITIES.md` solutions. When a solution's "riskiest assumption" graduates into an actual scheduled experiment, it becomes a hypothesis here. Cite the opportunity ID on the hypothesis so the link is traceable.

## Why cheap methods matter

Klein's data: teams that default to A/B tests run fewer experiments and learn slower than teams that use the full method toolbox (concierge, Wizard of Oz, fake door, prototype, A/B). The goal is not rigorous experiments — it's learning per unit time. A fake door on Tuesday beats an A/B test in six weeks.
