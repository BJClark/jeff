# jeff - Specification CLI for Product Discovery

A CLI that generates specification artifacts combining User Story Mapping (Patton), hypothesis-driven validation (Klein), and Opportunity Solution Trees (Torres).

## Installation

### System-wide (recommended)

```bash
# Install from GitHub
uv tool install git+https://github.com/BJClark/jeff.git

# Or from a local clone
uv tool install .
```

To update: `uv tool upgrade jeff`

To uninstall: `uv tool uninstall jeff`

### Development

```bash
uv sync
```

## AI Assistant Setup

Jeff is designed to work with AI coding assistants. Each tool has its own configuration format for project context.

### Claude Code

Claude Code automatically reads `AGENTS.md` in the project root. No additional setup needed.

```bash
# Run jeff commands directly in Claude Code
claude "Run jeff map and help me create a story map for my project"
```

### Cursor

Create a `.cursorrules` file in your project root:

```bash
cp AGENTS.md .cursorrules
```

Or reference it in `.cursor/rules`:

```
Include @AGENTS.md for project context
```

### Zed

Add to your `.zed/settings.json`:

```json
{
  "assistant": {
    "default_model": {
      "provider": "anthropic",
      "model": "claude-sonnet-4-20250514"
    },
    "context_sources": ["AGENTS.md"]
  }
}
```

### Opencode

Create an `opencode.md` file in your project root:

```bash
cp AGENTS.md opencode.md
```

Or configure in `opencode.json`:

```json
{
  "context": ["AGENTS.md"]
}
```

### Conductor

Add Jeff context to your `conductor.yaml`:

```yaml
agents:
  - name: jeff-assistant
    context:
      - AGENTS.md
    tools:
      - shell
```

## Workflow

Jeff guides you through a product discovery workflow. Each command generates a prompt—copy it to your AI assistant, get the response, and paste it into the corresponding artifact file.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           PRODUCT DISCOVERY                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  1. INITIALIZE                                                          │
│     jeff init                                                           │
│     └── Creates .jeff/ directory with artifact templates                │
│                                                                         │
│  2. MAP THE USER JOURNEY                                                │
│     jeff map                                                            │
│     └── Build the story map: backbone → walking skeleton → ribs         │
│         Output: .jeff/STORY_MAP.md                                      │
│                                                                         │
│  3. IDENTIFY OPPORTUNITIES                                              │
│     jeff opportunity                                                    │
│     └── Create Opportunity Solution Tree from research                  │
│         outcome → opportunities → solutions → experiments               │
│         Output: .jeff/OPPORTUNITIES.md                                  │
│                                                                         │
│  4. FORM HYPOTHESES                                                     │
│     jeff hypothesis                                                     │
│     └── Convert risky assumptions into testable hypotheses              │
│         Output: .jeff/HYPOTHESES.md                                     │
│                                                                         │
│  5. CAPTURE RESEARCH (ongoing)                                          │
│     jeff research interview    → Document user interviews               │
│     jeff research insight      → Extract patterns into insights         │
│         Output: .jeff/research/                                         │
│                                                                         │
│  6. GENERATE IMPLEMENTATION TASKS                                       │
│     jeff issues                → GitHub issues from artifacts           │
│     jeff bdd                   → BDD-style tasks with acceptance criteria│
│         Output: .jeff/issues/ or .jeff/TASKS.md                         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Typical Flow

1. **Start a new project**: `jeff init --name "My Product"`
2. **Define the user journey**: Run `jeff map`, work with AI to build your story map
3. **Dig into opportunities**: Run `jeff opportunity` to create your OST
4. **Identify risks**: Run `jeff hypothesis` to surface and plan validation for assumptions
5. **Iterate**: As you do research, use `jeff research interview` and `jeff research insight` to capture learnings
6. **Build**: When ready to implement, run `jeff issues` or `jeff bdd` to generate actionable tasks

Each artifact builds on the previous ones—the story map informs opportunities, opportunities inform hypotheses, and all three feed into issue generation.

## Usage

```bash
# Initialize project
jeff init [--name PROJECT_NAME]

# Story mapping workflow
jeff map                       # Print prompt for creating/updating story map
jeff map --show                # Display current story map

# Opportunity workflow
jeff opportunity               # Print prompt for OST creation
jeff opportunity --show        # Display current OST

# Hypothesis workflow
jeff hypothesis                # Print prompt for hypothesis generation
jeff hypothesis --list         # List current hypotheses
jeff hypothesis --validate ID  # Print prompt for validation planning

# Research capture
jeff research interview        # Print prompt for interview notes
jeff research insight          # Print prompt for insight extraction

# GitHub issues
jeff issues                    # Print prompt for generating issues from artifacts
jeff issues --create           # Create issues directly via gh CLI
jeff issues --dry-run          # Preview issues without creating
```

## Directory Structure

After `jeff init`, your project will have:

```
.jeff/
├── config.yaml                 # Project settings
├── prompts/                    # AI prompts for each workflow
├── STORY_MAP.md               # Backbone, walking skeleton, ribs
├── OPPORTUNITIES.md           # OST: outcome → opportunities → solutions
├── HYPOTHESES.md              # Assumptions, metrics, validation plans
├── research/
│   ├── USER_INTERVIEWS.md
│   ├── VALIDATION_RESULTS.md
│   └── INSIGHTS.md
└── issues/                    # Generated issue drafts
```

## Methodology Sources

- [User Story Mapping by Jeff Patton](https://www.jpattonassociates.com/the-new-backlog/)
- [Build Better Products by Laura Klein](https://rosenfeldmedia.com/books/build-better-products/)
- [Opportunity Solution Trees by Teresa Torres](https://www.producttalk.org/opportunity-solution-trees/)
