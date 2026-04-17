# jeff — Product Discovery Skills

A set of AI-assistant skills for product discovery, combining **User Story Mapping** (Patton), **Opportunity Solution Trees** (Torres), and **Hypothesis-Driven Development** (Klein).

Distributed as a **Claude Code plugin**. No Python, no build step — jeff is a set of markdown skills that plug directly into Claude Code (via the plugin system) or Cursor (via a rules file).

## Installation

### Claude Code (Recommended): install as a plugin

```bash
claude plugin marketplace add BJClark/jeff
claude plugin install jeff@jeff
```

All `/jeff:*` commands appear immediately. To uninstall: `claude plugin uninstall jeff@jeff`.

### Claude Code: try without installing

```bash
git clone https://github.com/BJClark/jeff ~/tools/jeff
claude --plugin-dir ~/tools/jeff
```

Loads jeff for the current session only — useful for evaluating before committing.

### Cursor: global or per-project

```bash
git clone https://github.com/BJClark/jeff ~/tools/jeff

# System-wide (~/.cursor/rules/)
~/tools/jeff/install.sh --cursor --global

# Project-local (./.cursor/rules/)
~/tools/jeff/install.sh --cursor --local
```

Cursor isn't plugin-aware, so `install.sh` writes a set of `.mdc` rule files:

- `jeff.mdc` — always-on umbrella rule (command reference + workflow overview).
- `jeff-init.mdc`, `jeff-map.mdc`, `jeff-opportunity.mdc`, `jeff-hypothesis.mdc`, `jeff-research.mdc`, `jeff-bdd.mdc`, `jeff-issues.mdc`, `jeff-help.mdc` — one on-demand rule per skill, each carrying its own description so Cursor loads it only when relevant. The `jeff-` prefix lives in the filename (not in the repo) so Cursor rules stay namespaced without polluting the plugin's skill names.

Uninstall: `~/tools/jeff/install.sh --uninstall --cursor --global` removes `jeff.mdc` and every `jeff-*.mdc`.

## Slash Commands

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
| `/jeff:help` | Show the command reference and workflow overview |

## Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           PRODUCT DISCOVERY                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  1. INITIALIZE                                                          │
│     /jeff:init                                                          │
│     └── Creates .jeff/ directory with artifact templates                │
│                                                                         │
│  2. MAP THE USER JOURNEY                                                │
│     /jeff:map                                                           │
│     └── Build the story map: backbone → walking skeleton → ribs         │
│         Output: .jeff/STORY_MAP.md                                      │
│                                                                         │
│  3. IDENTIFY OPPORTUNITIES                                              │
│     /jeff:opportunity                                                   │
│     └── Create Opportunity Solution Tree from research                  │
│         outcome → opportunities → solutions → experiments               │
│         Output: .jeff/OPPORTUNITIES.md                                  │
│                                                                         │
│  4. FORM HYPOTHESES                                                     │
│     /jeff:hypothesis                                                    │
│     └── Convert risky assumptions into testable hypotheses              │
│         Output: .jeff/HYPOTHESES.md                                     │
│                                                                         │
│  5. CAPTURE RESEARCH (ongoing)                                          │
│     /jeff:research interview    → Document user interviews              │
│     /jeff:research insight      → Extract patterns into insights        │
│         Output: .jeff/research/                                         │
│                                                                         │
│  6. GENERATE IMPLEMENTATION TASKS                                       │
│     /jeff:issues                → GitHub issues from artifacts          │
│     /jeff:bdd                   → BDD-style tasks with acceptance criteria│
│         Output: .jeff/issues/ or .jeff/TASKS.md                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Typical Flow

1. **Start a new project**: `/jeff:init` scaffolds `.jeff/` with templates
2. **Define the user journey**: `/jeff:map` walks you through backbone, walking skeleton, ribs
3. **Dig into opportunities**: `/jeff:research` to capture interviews, then `/jeff:opportunity` to build the OST
4. **Identify risks**: `/jeff:hypothesis` to surface and plan validation for assumptions
5. **Build**: When ready to implement, `/jeff:issues` for GitHub issues or `/jeff:bdd` for tasks with acceptance criteria

Each artifact builds on the previous ones — the story map informs opportunities, opportunities inform hypotheses, and all three feed into issue generation.

## Project Structure

After `/jeff:init`, your project will have:

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

## Skill Anatomy

jeff ships as Claude Agent Skills with progressive disclosure. Every skill lives in its own folder under `skills/`:

```
skills/<name>/
├── SKILL.md                    # The active workflow (kept under 5,000 words)
├── references/                 # Loaded on demand from SKILL.md
│   ├── methodology.md          # Framework theory (Patton / Torres / Klein)
│   ├── troubleshooting.md      # Symptom → fix pairs
│   └── edge-cases.md           # Anti-patterns and redirects
└── examples/                   # Worked conversations, one scenario per file
    ├── golden-path.md
    └── tricky-case.md
```

- **Frontmatter** (always loaded) — name, description, allowed-tools; tells Claude when to activate the skill.
- **SKILL.md body** (loaded on match) — the trigger list, inputs, numbered workflow, output contract, and pointers to companion files.
- **`references/` and `examples/`** (loaded on demand) — heavy context that only materialises when the workflow explicitly reads it.

Thin wrappers in `commands/<name>.md` expose each skill as a `/jeff:<name>` slash command (the `jeff:` prefix comes from the plugin name in `.claude-plugin/plugin.json`). The wrapper's only job is to invoke the matching skill; everything else lives under `skills/`.

See [AGENTS.md](AGENTS.md) for the full architecture diagram.

## Methodology Sources

- [User Story Mapping by Jeff Patton](https://www.jpattonassociates.com/the-new-backlog/)
- [Build Better Products by Laura Klein](https://rosenfeldmedia.com/books/build-better-products/)
- [Opportunity Solution Trees by Teresa Torres](https://www.producttalk.org/opportunity-solution-trees/)
