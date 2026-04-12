---
name: jeff:help
description: Show the jeff product-discovery command reference and typical workflow. Use when the user asks "what can jeff do", "how do I use jeff", "jeff help", or is new to the plugin and wants an overview.
allowed-tools:
  - Read
---

## Objective

Display the jeff command reference and guide new users through the product discovery workflow.

## Response

### Jeff — Product Discovery Skills

Jeff is a set of skills for AI-assisted product discovery. It combines three frameworks:

- **User Story Mapping** (Jeff Patton) — map the user's journey before the feature backlog.
- **Opportunity Solution Trees** (Teresa Torres) — connect outcomes to opportunities to solutions to experiments.
- **Hypothesis-Driven Development** (Laura Klein) — turn risky assumptions into testable hypotheses.

### Available commands

| Command | What it does |
|---------|-------------|
| `/jeff:init` | Scaffold `.jeff/` directory with artifact templates |
| `/jeff:map` | Create or update the user story map (backbone, skeleton, ribs) |
| `/jeff:opportunity` | Build an Opportunity Solution Tree |
| `/jeff:hypothesis` | Create and track testable hypotheses |
| `/jeff:research interview` | Capture a user interview |
| `/jeff:research insight` | Synthesize insights across research |
| `/jeff:bdd` | Generate BDD-style tasks with acceptance criteria |
| `/jeff:issues` | Generate GitHub issues from artifacts |

### Typical workflow

```
/jeff:init → /jeff:map → /jeff:opportunity → /jeff:hypothesis → /jeff:issues
             ↑                                                       |
             └──── /jeff:research (ongoing, feeds all the above) ────┘
```

1. **Start a new project**: `/jeff:init` scaffolds `.jeff/` with templates.
2. **Map the user journey**: `/jeff:map` walks you through backbone → walking skeleton → ribs.
3. **Identify opportunities**: `/jeff:research` to capture interviews, then `/jeff:opportunity` to build the OST.
4. **Surface risks**: `/jeff:hypothesis` to turn risky assumptions into experiments.
5. **Implement**: `/jeff:bdd` for tasks with acceptance criteria, or `/jeff:issues` to push straight to GitHub.

Each artifact builds on the previous ones — the story map informs opportunities, opportunities surface hypotheses, and all three feed into issue generation.

### Project structure

After `/jeff:init`, you'll have:

```
.jeff/
├── config.yaml                 # Project settings
├── STORY_MAP.md               # Backbone, walking skeleton, ribs
├── OPPORTUNITIES.md           # OST: outcome → opportunities → solutions
├── HYPOTHESES.md              # Assumptions, metrics, validation plans
├── TASKS.md                   # BDD tasks with acceptance criteria
├── research/
│   ├── USER_INTERVIEWS.md     # Individual interview notes
│   ├── INSIGHTS.md            # Synthesized patterns
│   └── VALIDATION_RESULTS.md  # Experiment outcomes
└── issues/                    # Generated issue drafts
```
