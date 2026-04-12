---
name: jeff-research
description: Capture user research — interview notes and synthesized insights. Use when the user says "log an interview", "capture research notes", or "extract insights". Writes to .jeff/research/USER_INTERVIEWS.md or .jeff/research/INSIGHTS.md.
allowed-tools: AskUserQuestion Read Write Edit
metadata:
  author: Will Clark
  version: "0.1.0"
  source-repo: https://github.com/BJClark/jeff
---

## Objective

Help the user capture user research in a consistent, reusable format — either interview notes (individual sessions) or insights (patterns synthesized across multiple interviews).

## Process

### 1. Check project state

Use the Read tool to open `.jeff/research/USER_INTERVIEWS.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `jeff-init` first and stop.

### 2. Determine research type

Ask: "Are you capturing a single interview, or extracting insights from research you've done?"

### 3. For interviews

Read `.jeff/research/USER_INTERVIEWS.md`, then walk through:

1. **Participant** — ID or pseudonym, role, how recruited, current solution.
2. **Key quotes** — verbatim, not paraphrased.
3. **Observations** — what you saw them do (behaviour vs. reported preference).
4. **Pain points** — explicit frustrations.
5. **Goals / desires** — in their own words.
6. **Follow-up questions** — what to probe next time.

Append under `## Interviews`.

### 4. For insights

Read both `USER_INTERVIEWS.md` and `INSIGHTS.md`. An insight is pattern + evidence (>= 2 sources) + implication.

- Single-source observations go under `## Emerging Patterns`.
- If an insight maps to an opportunity in `OPPORTUNITIES.md`, link it explicitly.

## Examples

**User says:** "I just finished an interview, let me log it."

Actions: Read interviews file. Ask 6 fields in sequence. Append new entry.

## Troubleshooting

- **Quote vs. paraphrase.** Ask "did they actually say that, or is that your interpretation?"
- **Single-source insight.** Keep in Emerging Patterns until more evidence.
- **PII.** Default to anonymising (P1, P2, ...).
