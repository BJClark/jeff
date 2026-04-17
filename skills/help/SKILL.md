---
name: help
description: Show the jeff product-discovery command reference and typical workflow for new users. Use when someone is new to jeff, wants to know what commands are available, or asks for a workflow overview. Triggers on 'what can jeff do', 'how do I use jeff', 'jeff help', 'jeff overview', 'list jeff commands'.
allowed-tools:
  - Read
---

## When to use
- User is new to jeff and asks what it can do.
- User wants a list of available `/jeff:*` commands.
- User asks for the typical workflow or "where do I start".

## Inputs
- None.

## Workflow

Display the content below. If the user wants more depth on a specific area, point them at `references/workflow-overview.md` rather than inlining the full detail.

---

### Jeff — Product Discovery Skills

Jeff is a set of skills for AI-assisted product discovery, combining three frameworks:

- **User Story Mapping** (Jeff Patton) — map the user's journey before the feature backlog.
- **Opportunity Solution Trees** (Teresa Torres) — connect outcomes to customer opportunities to solutions to experiments.
- **Hypothesis-Driven Development** (Laura Klein) — turn risky assumptions into falsifiable, measurable hypotheses.

### Commands

| Command               | What it does                                                     |
|-----------------------|------------------------------------------------------------------|
| `/jeff:init`          | Scaffold `.jeff/` with artifact templates (run this first).     |
| `/jeff:map`           | Create or update the user story map (backbone, skeleton, ribs). |
| `/jeff:opportunity`   | Build or review an Opportunity Solution Tree.                    |
| `/jeff:hypothesis`    | Create, update, or review testable hypotheses.                   |
| `/jeff:research`      | Capture user interviews or synthesise insights.                  |
| `/jeff:bdd`           | Generate tasks with Gherkin-style acceptance criteria.           |
| `/jeff:issues`        | Generate GitHub issues from the discovery artifacts.             |
| `/jeff:help`          | Show this reference.                                             |

### Typical workflow

```
/jeff:init → /jeff:map → /jeff:opportunity → /jeff:hypothesis → /jeff:bdd → /jeff:issues
             ↑                                                                          |
             └──── /jeff:research (ongoing, feeds all the above) ──────────────────────┘
```

1. **Start**: `/jeff:init` scaffolds `.jeff/` in your project.
2. **Map**: `/jeff:map` walks you through backbone → walking skeleton → ribs.
3. **Discover**: `/jeff:research interview` captures user interviews; `/jeff:research insight` synthesises patterns.
4. **OST**: `/jeff:opportunity` turns insights into opportunities and candidate solutions.
5. **Validate**: `/jeff:hypothesis` formalises risky assumptions as experiments.
6. **Ship**: `/jeff:bdd` for tasks with acceptance criteria, or `/jeff:issues` to push straight to GitHub.

### Artifacts

After `/jeff:init`, your project has:

```
.jeff/
├── config.yaml                 # project settings
├── STORY_MAP.md                # backbone, walking skeleton, ribs
├── OPPORTUNITIES.md            # outcome → opportunities → solutions → experiments
├── HYPOTHESES.md               # active / validated / invalidated
├── TASKS.md                    # BDD tasks with acceptance criteria
├── research/
│   ├── USER_INTERVIEWS.md      # per-interview notes
│   ├── INSIGHTS.md             # synthesised patterns
│   └── VALIDATION_RESULTS.md   # experiment outcomes
└── issues/                     # GitHub batch records
```

Each artifact builds on the previous ones — the story map informs opportunities, opportunities surface hypotheses, and all three feed task and issue generation.

### Want more detail on any area?

Ask. Each skill has companion reference files and worked examples:

- `skills/map/` — story mapping with Patton's methodology.
- `skills/opportunity/` — OST with experiment method comparisons.
- `skills/hypothesis/` — hypothesis formula, validation methods.
- `skills/research/` — interview protocol, insight formula.
- `skills/bdd/` — acceptance criteria quality rules.
- `skills/issues/` — GitHub issue template and gh CLI setup.

Or load the expanded workflow in `references/workflow-overview.md`.

## More
- Expanded workflow overview and methodology pointers: `references/workflow-overview.md`
