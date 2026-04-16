# jeff — Expanded Workflow Overview

This is the deeper tour of how the skills interact. Read this after `/jeff:help` if you want the "why" and the edge cases, not just the command list.

## The three frameworks, briefly

### User Story Mapping (Jeff Patton)

Organises work around **what the user does** — not what the team builds. The map has three layers:

- **Backbone** — 3–8 big user activities, narrative order, left to right.
- **Walking skeleton** — the thinnest story per activity that keeps the end-to-end flow alive.
- **Ribs** — everything else, split into Release 1 (ships) and Future (doesn't yet).

Patton's test: "If you're not talking about users and what they do, you're not story mapping."

### Opportunity Solution Trees (Teresa Torres)

Keeps the team anchored on **outcomes over outputs**:

- **Outcome** — a measurable business/user result.
- **Opportunities** — customer needs discovered through research.
- **Solutions** — candidate ways to address an opportunity (≥3 per opportunity).
- **Experiments** — cheapest tests of the riskiest assumptions.

The tree is a working document. Torres' data: teams that force ≥3 solutions per opportunity pick the "obvious first" solution less than half the time.

### Hypothesis-Driven Development (Laura Klein)

Treats every product decision as a hypothesis until tested. A good hypothesis is:

- **Specific** — one variable, one target segment.
- **Measurable** — real metric, real threshold.
- **Falsifiable** — there's a number that would make you say "no."
- **Risk-proportionate** — match method to stakes (fake door → A/B test).

Never delete invalidated hypotheses. They're the memory of what's been tried.

## How the artifacts talk to each other

```
STORY_MAP.md  ←──────── shapes which opportunities are worth exploring ───────────  OPPORTUNITIES.md
      ↓                                                                                    ↓
      └───── backbone activities suggest where tasks cluster ─────→ TASKS.md    assumptions become → HYPOTHESES.md
                                                                          ↑                               ↓
                                                                          └──── results feed back ────────┘

          research/INSIGHTS.md  ─── evidence for opportunities, contradicts hypotheses, scopes patterns
```

In practice:
- An **interview** (P4 says the list feels overwhelming) lands in `research/USER_INTERVIEWS.md`.
- Across 3 interviews, a **pattern** emerges → `research/INSIGHTS.md`.
- The insight becomes **evidence** on an opportunity in `OPPORTUNITIES.md`.
- A candidate solution's riskiest assumption graduates into a **hypothesis** in `HYPOTHESES.md`.
- The experiment runs; results go in `research/VALIDATION_RESULTS.md` and update the hypothesis status.
- A validated solution spawns **tasks** in `TASKS.md` via `/jeff:bdd`.
- Tasks become **GitHub issues** via `/jeff:issues`.

## When to use each command

### `/jeff:init`
- First command in any new project. Scaffolds `.jeff/` and 8 template files.
- Also when another skill errors with "`.jeff/` missing."

### `/jeff:map`
- Starting a new project (build the backbone).
- Scoping an MVP (build the walking skeleton).
- Prioritising a release (fill ribs, apply the "would you ship without it?" test).
- Reviewing a stale map (cut the map back to what you'd actually ship).

### `/jeff:opportunity`
- Translating research insights into opportunities.
- Responding when someone says "add feature X" (redirect to the need).
- Generating ≥3 candidate solutions per opportunity.
- Picking the cheapest experiment for a risky assumption.
- Reviewing an OST that's gone stale.

### `/jeff:hypothesis`
- Formalising a risky assumption as an experiment.
- Recording results after an experiment completes.
- Reviewing the active list for falsifiability and staleness.

### `/jeff:research`
- After every user interview — log while it's fresh.
- After 3–5 interviews — synthesise patterns into insights.
- When an insight reinforces or contradicts the OST — link both.

### `/jeff:bdd`
- After the story map is populated — turn stories into tasks with acceptance criteria.
- After the story map changes — regenerate affected tasks without disturbing in-flight ones.
- Before handing work to engineering.

### `/jeff:issues`
- When tasks are ready for engineering pickup.
- Defaults to `--dry-run` — preview before committing.
- Supports filtering by source (`map`, `opportunities`, `hypotheses`) for staggered batches.

## Common pitfalls

1. **Jumping to features before mapping user activities.** Use `/jeff:map` first; `/jeff:opportunity` builds on it.
2. **Writing opportunities that are really solutions.** `/jeff:opportunity` will redirect — let it.
3. **Non-falsifiable hypotheses.** `/jeff:hypothesis` won't record a hypothesis without a threshold.
4. **Single-source insights.** `/jeff:research insight` will file patterns with N=1 under `Emerging Patterns`, not `Key Insights`.
5. **Creating 30 GitHub issues at once.** `/jeff:issues` warns and suggests splitting.
6. **Deleting invalidated hypotheses.** Don't. The `## Invalidated` section is the team's memory.

## Where to go next

- **New to discovery?** Read `skills/jeff-map/references/methodology.md` and `skills/jeff-opportunity/references/methodology.md`.
- **Picking an experiment?** `skills/jeff-opportunity/references/experiment-methods.md`.
- **Writing good acceptance criteria?** `skills/jeff-bdd/references/acceptance-criteria.md`.
- **Setting up GitHub?** `skills/jeff-issues/references/gh-cli-setup.md`.

## Methodology sources

- Jeff Patton, *User Story Mapping* (O'Reilly, 2014).
- Teresa Torres, *Continuous Discovery Habits* (Product Talk, 2021).
- Laura Klein, *Build Better Products* (Rosenfeld, 2016).
