---
name: jeff-hypothesis
description: Create and track product hypotheses using Laura Klein's hypothesis-driven development approach. Use when the user asks to "track a hypothesis", says "I have an assumption to test", "validate this idea", or mentions risky assumptions. Writes to .jeff/HYPOTHESES.md.
allowed-tools: AskUserQuestion Read Write Edit
metadata:
  author: Will Clark
  version: "0.1.0"
  source-repo: https://github.com/BJClark/jeff
---

## Objective

Help the user turn risky product assumptions into testable, falsifiable hypotheses with clear success metrics.

## Process

### 1. Check project state

Use the Read tool to open `.jeff/HYPOTHESES.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `jeff-init` first and stop.
- If `.jeff/` exists but `HYPOTHESES.md` is missing, offer to recreate it from the template.

### 2. Create a new hypothesis

Walk the user through each field one at a time:

1. **Assumption** — "What do we believe to be true that we haven't tested?"
2. **Statement** — "We believe that [specific change] will result in [expected outcome] for [target users], measured by [metric] with a threshold of [number]."
3. **Metric** — "How will we measure it?"
4. **Threshold** — "What result means success? What means failure?"
5. **Risk level** — High (core business), Medium (feature-level), Low (implementation detail).
6. **Validation method** — Concierge, Wizard of Oz, Fake door, Prototype, or A/B test. Pick the lightest.

### 3. Update an existing hypothesis

When an experiment completes, capture: Status (Validated/Invalidated/Inconclusive), Results, Learning, Decision (persevere/pivot/kill). Move to the right section. Never delete invalidated hypotheses.

### 4. Review all active hypotheses

Check: falsifiable? measurable? proportionate validation method? sitting untested too long?

### 5. Write the updates

Edit `.jeff/HYPOTHESES.md` in place. Increment IDs for new hypotheses.

## Examples

**User says:** "I want to track a hypothesis that adding social proof will increase conversion."

Actions: Walk through hypothesis formula. Classify risk. Suggest validation method. Write new H# to `.jeff/HYPOTHESES.md`.

## Troubleshooting

- **Not falsifiable.** If the user can't describe a result that would disprove it, push back.
- **No metric.** Ask if instrumentation exists or needs to be built.
- **Validation too heavy.** Suggest cheaper methods for low-risk hypotheses.
- **User wants to delete invalidated hypothesis.** Don't — move to Invalidated section with learning intact.

## Methodology reference

Hypothesis-Driven Development (Laura Klein, *Build Better Products*, 2016): specific, measurable, falsifiable hypotheses with validation rigour matched to risk.
