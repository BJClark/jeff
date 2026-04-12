# AGENTS.md

## What is Jeff?

Jeff is a set of AI-assistant skills for product discovery. It combines three frameworks to help teams move from research to validated implementation:

1. **User Story Mapping (Patton)** — Backbone (user activities) → Walking Skeleton (MVP slice) → Ribs (stories per activity)
2. **Opportunity Solution Trees (Torres)** — Desired Outcome → Opportunities → Solutions → Experiments
3. **Hypothesis-Driven Development (Klein)** — Assumption → Metric → Validation Method → Result

## Available Commands

| Command | What it does |
|---------|-------------|
| `/jeff:init` | Scaffold `.jeff/` directory with artifact templates |
| `/jeff:map` | Create or update the user story map |
| `/jeff:opportunity` | Build an Opportunity Solution Tree |
| `/jeff:hypothesis` | Create and track testable hypotheses |
| `/jeff:research interview` | Capture a user interview |
| `/jeff:research insight` | Synthesize insights across research |
| `/jeff:bdd` | Generate BDD-style tasks with acceptance criteria |
| `/jeff:issues` | Generate GitHub issues from artifacts |
| `/jeff:help` | Show the command reference |

## Key Artifacts

All artifacts live in the `.jeff/` directory:

- `STORY_MAP.md` — The story map (backbone, walking skeleton, ribs)
- `OPPORTUNITIES.md` — The opportunity solution tree
- `HYPOTHESES.md` — Testable assumptions with validation plans
- `TASKS.md` — BDD-style tasks with acceptance criteria
- `research/` — Interview notes, insights, validation results

## Architecture

```
src/jeff/skills/            # Skill files (Claude Code / Cursor)
├── jeff-init.md
├── jeff-map.md
├── jeff-opportunity.md
├── jeff-hypothesis.md
├── jeff-research.md
├── jeff-bdd.md
├── jeff-issues.md
├── jeff-help.md
└── templates/              # Artifact templates for jeff:init
    ├── STORY_MAP.md
    ├── OPPORTUNITIES.md
    ├── HYPOTHESES.md
    ├── TASKS.md
    ├── USER_INTERVIEWS.md
    ├── INSIGHTS.md
    ├── VALIDATION_RESULTS.md
    └── config.yaml

commands/                   # Symlinks for Claude Code plugin
install.sh                  # Shell installer for Claude Code and Cursor
```

No Python dependency. Skills are self-contained markdown files with embedded instructions.
