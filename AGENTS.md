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

Jeff follows the Claude Agent Skills layout with progressive disclosure. Each skill is a folder containing a slim `SKILL.md` (the active workflow) plus `references/` and `examples/` that are loaded on demand.

```
.claude-plugin/
├── plugin.json                 # Plugin manifest (name: "jeff", points at commands/ and skills/)
└── marketplace.json            # Marketplace entry so `claude plugin install jeff@jeff` works

commands/                       # Thin slash-command wrappers — invoke the matching skill
├── init.md                     # → /jeff:init
├── map.md                      # → /jeff:map
├── opportunity.md
├── hypothesis.md
├── research.md
├── bdd.md
├── issues.md
└── help.md

skills/                         # Canonical Agent Skills (plugin-namespaced as jeff:<name>)
├── init/
│   ├── SKILL.md
│   ├── references/             # troubleshooting, edge cases
│   ├── examples/               # worked scenarios
│   └── templates/              # artifact scaffolds copied into .jeff/
├── map/
│   ├── SKILL.md
│   ├── references/             # methodology (Patton), troubleshooting, edge cases
│   └── examples/
├── opportunity/
│   ├── SKILL.md
│   ├── references/             # methodology (Torres), experiment-methods, …
│   └── examples/
├── hypothesis/
│   ├── SKILL.md
│   ├── references/             # methodology (Klein), validation-methods, …
│   └── examples/
├── research/
│   ├── SKILL.md
│   ├── references/             # interview-protocol, insight-formula, …
│   └── examples/
├── bdd/
│   ├── SKILL.md
│   ├── references/             # acceptance-criteria, task-template, …
│   └── examples/
├── issues/
│   ├── SKILL.md
│   ├── references/             # issue-template, gh-cli-setup, …
│   └── examples/
└── help/
    ├── SKILL.md
    └── references/workflow-overview.md

install.sh                      # Shell installer for Cursor (Claude Code uses the plugin flow)
```

### Progressive disclosure

- **Frontmatter** — always loaded into the skill index; used by Claude to decide when to activate a skill.
- **SKILL.md body** — loaded when the skill activates; contains only the active workflow.
- **`references/` and `examples/`** — loaded on demand when SKILL.md explicitly points to them. Methodology, troubleshooting, edge cases, and worked scenarios live here so the base skill stays under the 5,000-word budget.

No Python dependency. Skills are self-contained markdown with embedded instructions.
