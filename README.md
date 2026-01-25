# jeff - Specification CLI for Product Discovery

A CLI that generates specification artifacts combining User Story Mapping (Patton), hypothesis-driven validation (Klein), and Opportunity Solution Trees (Torres).

## Installation

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
