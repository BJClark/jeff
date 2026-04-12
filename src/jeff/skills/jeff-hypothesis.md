---
name: jeff:hypothesis
description: Create and track product hypotheses using Laura Klein's hypothesis-driven development approach. Use when the user asks to "track a hypothesis", says "I have an assumption to test", "validate this idea", "record what we learned", or mentions risky assumptions that need validation. Writes to .jeff/HYPOTHESES.md.
argument-hint: "[hypothesis-id]"
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## Objective

Help the user turn risky product assumptions into **testable, falsifiable hypotheses** with clear success metrics, following Laura Klein's hypothesis-driven development approach.

## Arguments

Optional hypothesis ID (e.g. `H3`): `$ARGUMENTS`

- If an ID is provided, focus on that specific hypothesis (create, update, or record results).
- If no ID, either create a new hypothesis or work across all active ones.

## Process

### 1. Check project state

Use the Read tool to open `.jeff/HYPOTHESES.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `/jeff:init` first and stop.
- If `.jeff/` exists but `HYPOTHESES.md` is missing, offer to recreate it from the template.

### 2. Decide the mode

- **New hypothesis** — create one from a user assumption.
- **Update existing** — refine a hypothesis as you learn more, or record results after an experiment.
- **Review all** — sanity-check the active list.

### 3. Create a new hypothesis

Walk the user through each field — ask one at a time, don't dump the whole template:

1. **The assumption.** "What do we believe to be true that we haven't tested?" Often this comes from an OPPORTUNITIES.md solution's assumptions list.
2. **The statement.** Rewrite as: _"We believe that **[specific change]** will result in **[expected outcome]** for **[target users]**, which we'll measure by **[metric]** with a threshold of **[number]**."_
3. **Metric.** "How will we measure it? Which existing number moves, or do we need new instrumentation?"
4. **Threshold.** "What result would make us say 'yes, this worked'? What result would make us say 'no'?" If the user can't answer "what result would make us stop", the hypothesis isn't falsifiable yet — push back.
5. **Risk level.** "If this turns out wrong, how much does it cost?"
   - **High**: core business model / expensive to reverse → needs a real experiment before committing.
   - **Medium**: feature-level / moderate cost → fake door or prototype is usually enough.
   - **Low**: implementation detail / cheap to change → often not worth formalising at all.
6. **Validation method.** Pick the *lightest* method that actually tests the assumption:
   - **Concierge** — manually deliver the service end-to-end to a few users.
   - **Wizard of Oz** — fake automation, real humans behind it.
   - **Fake door** — measure interest before building.
   - **Prototype** — low-fidelity clickable test.
   - **A/B test** — production comparison (last resort, most expensive to run).

### 4. Update an existing hypothesis

When an experiment completes, capture:

- **Status**: `Validated` | `Invalidated` | `Inconclusive`
- **Results**: what numbers did you see vs. the threshold?
- **Learning**: what does this tell you — about this hypothesis, but also about the broader opportunity?
- **Decision**: persevere, pivot, or kill?

Move the hypothesis to the `## Validated` or `## Invalidated` section of the file. **Don't delete invalidated hypotheses** — negative learning is the most valuable output of this process.

### 5. Review all active hypotheses

For each one in `## Active Hypotheses`, check:

- Is it *falsifiable*? (Is there a concrete result that would disprove it?)
- Is the metric actually measurable with current instrumentation?
- Is the validation method proportionate to the risk level?
- Has it been sitting untested for weeks? Add a "next step" nudge.

### 6. Write the updates

Edit `.jeff/HYPOTHESES.md` in place. Preserve existing hypotheses and their statuses. Increment IDs (`H1`, `H2`, …) for new ones.

## Examples

**User says:** "I want to track a hypothesis that adding social proof on the pricing page will increase conversion."

Actions:
1. Walk the user through the hypothesis formula and restate: "We believe that adding customer logos to the pricing page will result in higher trial sign-ups for first-time visitors, which we'll measure by sign-up conversion rate with a threshold of +15% vs. control."
2. Classify as Medium risk (feature-level, easy to revert).
3. Suggest an A/B test as the validation method — but ask first whether a fake door or simple prototype comparison would work cheaper.
4. Write the new H# to `.jeff/HYPOTHESES.md` with status `Untested`.

Result: A falsifiable hypothesis with a clear metric, threshold, and validation plan.

---

**User says:** "H3's experiment just finished. We saw a 4% lift, not the 15% we predicted."

Actions:
1. Read H3 from `.jeff/HYPOTHESES.md`.
2. Ask what the threshold was and whether 4% is inside or outside noise.
3. Status: `Inconclusive` (below threshold but directionally positive) — or `Invalidated` if the user is confident the effect won't scale.
4. Record results, learning, and decision. Move to the right section.

Result: H3 updated with results and learning; next steps (rerun with more power / kill / pivot) captured.

## Troubleshooting

- **`.jeff/` missing.** Send the user to `/jeff:init` first.
- **Hypothesis isn't falsifiable.** If the user can't describe a result that would *disprove* it, it's a wish, not a hypothesis. Refuse to record it until they can.
- **No metric defined.** Ask whether the metric exists today or needs instrumentation. If instrumentation is needed, note that as a prerequisite task — don't skip it.
- **Validation method too heavy.** If they propose an A/B test for a Low-risk hypothesis, suggest a cheaper method. A/B tests take weeks and real traffic — save them for things you genuinely can't learn cheaper.
- **User wants to delete an invalidated hypothesis.** Don't. Move it to `## Invalidated` with the learning intact. Future-you wants to know which ideas failed and why.

## Methodology reference

Hypothesis-Driven Development (Laura Klein, *Build Better Products*, Rosenfeld 2016):

- Every product idea is a hypothesis until validated.
- Good hypotheses are **specific**, **measurable**, and **falsifiable**.
- Match validation rigour to risk — cheap tests first, production tests only when they're the only option that answers the question.
- Record *all* results, including invalidations — those are the learnings that compound.
