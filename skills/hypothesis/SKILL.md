---
name: hypothesis
description: Create and track falsifiable product hypotheses with metrics, thresholds, and proportionate validation methods. Use when the user wants to turn a risky assumption into a real experiment, record experiment results, or review the active hypothesis list. Triggers on 'track a hypothesis', 'assumption to test', 'validate this idea', 'record what we learned', 'we got the results back'. Writes to .jeff/HYPOTHESES.md.
argument-hint: "[hypothesis-id]"
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## When to use
- User says "track a hypothesis" / "I have an assumption to test" / "validate this idea".
- An experiment just completed and results need recording.
- User wants to sanity-check the active hypothesis list (too many, too old, non-falsifiable).

## Inputs
- Required: `.jeff/HYPOTHESES.md` (scaffolded by `/jeff:init`).
- Optional context: `.jeff/OPPORTUNITIES.md` — assumptions from solutions often become hypotheses.
- Optional `$ARGUMENTS`: a hypothesis ID (`H3`) to focus on.

## Workflow

1. **Check project state.** Read `.jeff/HYPOTHESES.md`. If `.jeff/` is missing, send the user to `/jeff:init` and stop. If the file is missing but `.jeff/` exists, offer to recreate from template.

2. **Decide the mode.**
   - **New** — create a hypothesis from a user assumption.
   - **Update** — record results after an experiment completes.
   - **Review** — sanity-check the active list.

3. **Create a new hypothesis.** Walk the user through each field, one at a time:
   - **Assumption.** "What do we believe to be true that we haven't tested?" (Often pulled from `OPPORTUNITIES.md`.)
   - **Statement.** Rewrite as: _"We believe that **[specific change]** will result in **[expected outcome]** for **[target users]**, which we'll measure by **[metric]** with a threshold of **[number]**."_
   - **Metric.** Must be measurable with current instrumentation (or instrumentation must be added as a prerequisite task).
   - **Threshold.** "What result means 'yes this worked'? What means 'no'?" If the user can't name a result that would *disprove* the hypothesis, it isn't falsifiable yet — push back.
   - **Risk level.** H / M / L. Drives the validation method.
   - **Validation method.** Pick the *lightest* method that actually tests the assumption. See `references/validation-methods.md`.
   - **Experiment plan.** Explicit instructions for *how to actually run this*. Capture:
     - **Setup** — what to build/configure (variant spec, instrumentation to add, cohort filter, feature flag).
     - **Run conditions** — sample size or duration, traffic allocation, stop criteria (e.g. "run until 5k signups per arm or 14 days, whichever first").
     - **Measurement** — where the metric is read (dashboard, query, tool) and how results get pulled for the update step.
     If any of these can't be answered, the hypothesis isn't ready to run — flag the gap (e.g. "instrumentation missing") as a prerequisite task rather than recording a vague plan.

4. **Update an existing hypothesis.** When an experiment completes, capture:
   - **Status.** `Validated` / `Invalidated` / `Inconclusive`.
   - **Results.** The actual numbers vs. the threshold.
   - **Learning.** What does this tell us — about the hypothesis and about the broader opportunity?
   - **Decision.** Persevere / pivot / kill.

   Move the hypothesis to the `## Validated` or `## Invalidated` section. **Never delete invalidated hypotheses** — negative learning is the point.

5. **Review all active hypotheses.** For each:
   - Falsifiable? (Is there a result that would disprove it?)
   - Metric actually measurable today?
   - Validation method proportionate to the risk level?
   - Sitting untested for weeks? Add a "next step" nudge or propose deprecation.

6. **Write the updates.** Edit `.jeff/HYPOTHESES.md` in place. Preserve existing entries and their statuses. Increment IDs (`H1`, `H2`, …) for new ones.

## Output
- Writes/edits `.jeff/HYPOTHESES.md`. Preserves prior entries. If the hypothesis traces to an opportunity in `OPPORTUNITIES.md`, cite the opportunity ID.

## More
- Methodology and theory: `references/methodology.md`
- Validation method comparison: `references/validation-methods.md`
- Common failures and fixes: `references/troubleshooting.md`
- Anti-patterns and redirects: `references/edge-cases.md`
- Worked examples: `examples/social-proof-ab-test.md`, `examples/recording-inconclusive-result.md`, `examples/reviewing-stale-active-list.md`
