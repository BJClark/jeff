---
name: jeff-research
description: Capture user research — interview notes and synthesised insights (pattern + evidence + implication). Use when the user just finished a user interview, wants to record observations, or needs to extract patterns across prior research. Triggers on 'log an interview', 'capture research notes', 'I just finished a user interview', 'extract insights', 'synthesise patterns'. Writes to .jeff/research/USER_INTERVIEWS.md or .jeff/research/INSIGHTS.md.
argument-hint: "[interview|insight]"
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## When to use
- User says "I just finished an interview, help me log it" / "capture research notes".
- User says "I've done N interviews, help me pull out the insights" / "extract patterns".
- User wants to link research back to the OST or hypotheses.

## Inputs
- Required: `.jeff/research/` directory (scaffolded by `/jeff:init`).
- Optional `$ARGUMENTS`: `interview` or `insight`. If absent, ask.

## Workflow

1. **Check project state.** Read `.jeff/research/USER_INTERVIEWS.md`. If `.jeff/` is missing, send the user to `/jeff:init` and stop.

2. **Determine research type.** Use `$ARGUMENTS` if set. Otherwise ask: "Are you capturing a single interview you just finished, or extracting insights from research you've already done?"

3. **For interviews**: walk the user through 6 fields, one at a time. Don't dump the template.
   - **Participant** — anonymised ID (P1, P2), role/background, recruitment channel, what they use today.
   - **Key quotes** — verbatim, not paraphrased. "Give me their actual words."
   - **Observations** — what you *saw them do*, separate from what they said. Behaviour often contradicts reported preference.
   - **Pain points** — explicit frustrations they named.
   - **Goals / desires** — what they were trying to achieve, in their own words.
   - **Follow-up questions** — what you wish you'd asked; what the next interview should probe.

   Append the new interview under `## Interviews` in `.jeff/research/USER_INTERVIEWS.md`. Keep each interview self-contained.

4. **For insights**: read both `USER_INTERVIEWS.md` and `INSIGHTS.md`. An insight = **pattern + evidence + implication**. Walk through:
   - **Pattern** — seen across ≥2 interviews or data points. Single-source patterns go under `## Emerging Patterns`, not `## Key Insights`.
   - **Evidence** — list specific interviews / quotes / data points. Push for ≥2.
   - **Implication** — what should the team *do differently* because of this? If nothing, it's trivia, not an insight.
   - **Related opportunities** — does this map to a row in `OPPORTUNITIES.md`? Link explicitly.

   Append under `## Key Insights`.

5. **Link back to the OST when appropriate.** If an insight reinforces or contradicts an existing opportunity or hypothesis, surface it:
   - "This insight is evidence for Opportunity O2 — should I add it to the Evidence field?"
   - "This contradicts the assumption under H3 — should we revisit?"

   Don't edit `OPPORTUNITIES.md` or `HYPOTHESES.md` silently — propose, then act on confirmation.

## Output
- Appends to `.jeff/research/USER_INTERVIEWS.md` (interviews) or `.jeff/research/INSIGHTS.md` (insights). Preserves prior entries. Anonymises PII by default.

## More
- Interview field guidance: `references/interview-protocol.md`
- Insight formula (pattern + evidence + implication): `references/insight-formula.md`
- Common failures and fixes: `references/troubleshooting.md`
- Anti-patterns and redirects: `references/edge-cases.md`
- Worked examples: `examples/interview-log.md`, `examples/synthesising-insights.md`, `examples/linking-insight-to-ost.md`
