---
name: jeff:research
description: Capture user research — interview notes and synthesized insights. Use when the user says "log an interview", "I just finished a user interview", "capture research notes", "extract insights", or mentions interview participants, observations, or patterns. Writes to .jeff/research/USER_INTERVIEWS.md or .jeff/research/INSIGHTS.md.
argument-hint: "[type: interview|insight]"
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## Objective

Help the user capture user research in a consistent, reusable format — either **interview notes** (individual sessions) or **insights** (patterns synthesized across multiple interviews or data points).

## Arguments

Research type: `$ARGUMENTS`

- `interview` — capture a single user interview.
- `insight` — synthesize patterns across prior research.
- (none) — ask the user which they want.

## Process

### 1. Check project state

Use the Read tool to open `.jeff/research/USER_INTERVIEWS.md`. If it doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `/jeff:init` first and stop.

### 2. Determine research type

If `$ARGUMENTS` is set, use it. Otherwise ask:

> "Are you capturing a single interview you just finished, or extracting insights from research you've already done?"

### 3. For interviews

Use the Read tool to open `.jeff/research/USER_INTERVIEWS.md` so you can append in-place.

Then walk the user through each field — don't dump the template, ask one question at a time:

1. **Participant** — ID or pseudonym (don't store real PII), role/background, how they were recruited, what they use today.
2. **Key quotes** — "What did they say that surprised you, or that captured the issue? Give me verbatim if possible." Quote them literally; don't paraphrase insights into the quote.
3. **Observations** — "What did you *see them do*, separate from what they said?" Behaviour often contradicts reported preference.
4. **Pain points** — explicit frustrations they named.
5. **Goals / desires** — what they were trying to achieve, in their own words.
6. **Follow-up questions** — "What do you wish you'd asked? What should the next interview probe?"

Append the new interview under `## Interviews` in `.jeff/research/USER_INTERVIEWS.md`, using the template structure. Keep each interview self-contained.

### 4. For insights

Use the Read tool to open both `.jeff/research/USER_INTERVIEWS.md` and `.jeff/research/INSIGHTS.md`.

An insight is **a pattern + evidence + implication**, not just an observation. Walk through:

1. **Pattern** — "What have you noticed across multiple interviews or data points?" If it's only in one interview, it's probably not yet an insight — put it under `## Emerging Patterns` instead.
2. **Evidence** — list the specific interviews, quotes, or data points that support the pattern. An insight with only one supporting reference is thin; push for at least two.
3. **Implication** — "So what? What should we *do differently* because of this?" If there's no implication, it's trivia, not an insight.
4. **Related opportunities** — does this map to a row in `.jeff/OPPORTUNITIES.md`? Link it explicitly.

Append the new insight under `## Key Insights` in `.jeff/research/INSIGHTS.md`.

### 5. Link back to the OST when appropriate

If an insight reinforces or contradicts an existing opportunity, tell the user and offer to update `.jeff/OPPORTUNITIES.md`:

- "This insight is evidence for Opportunity 2 — should I add it to the Evidence field?"
- "This contradicts the assumption under Solution A — should we reclassify Opportunity 2?"

Don't edit `OPPORTUNITIES.md` silently; surface it as a suggestion.

## Examples

**User says:** "I just finished an interview with a beta user, let me log it."

Actions:
1. Read `.jeff/research/USER_INTERVIEWS.md`.
2. Ask the 6 interview fields in sequence, one at a time.
3. Append a new dated section under `## Interviews` with the user's answers, preserving quotes verbatim.
4. Ask whether any of this should feed an insight now or wait for more interviews.

Result: A new interview entry in `.jeff/research/USER_INTERVIEWS.md`, properly structured.

---

**User says:** "I've done five interviews now. Help me pull out the insights."

Actions:
1. Read both `USER_INTERVIEWS.md` and `INSIGHTS.md`.
2. Walk through the interviews looking for repeated themes; name the patterns out loud ("Three people mentioned X...").
3. For each pattern that repeats ≥2x, draft an insight (pattern + evidence + implication).
4. Append them under `## Key Insights`; anything only seen once goes under `## Emerging Patterns`.
5. For each new insight, suggest whether it should update an opportunity in `.jeff/OPPORTUNITIES.md`.

Result: 2–4 insights synthesized with evidence references; emerging patterns captured separately.

## Troubleshooting

- **`.jeff/research/` missing.** Send the user to `/jeff:init` first.
- **Quote vs. paraphrase.** If the user paraphrases, ask "did they actually say that, or is that your interpretation?" Keep verbatim quotes in `Key Quotes` and interpretation in `Observations`.
- **Single-source "insight".** If a pattern only appears in one interview, don't promote it to an insight — add it to `## Emerging Patterns` and note that more evidence is needed.
- **PII in notes.** If the user gives you real names / emails / identifying info, ask whether they want to anonymise (P1, P2, …) before writing. Default to anonymising.
- **Insight with no implication.** Push back: "What would the team do differently because of this?" If nothing, it's an observation, not an insight.
- **Contradiction with OST.** If an insight contradicts an assumption in `OPPORTUNITIES.md`, surface it explicitly and offer to update — don't leave the contradiction sitting silently in two files.
