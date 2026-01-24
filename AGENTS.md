# AGENTS.md

## What is Jeff?

Jeff is a CLI that generates prompts for AI-assisted product discovery. Users pipe jeff's output to an LLM (via Claude, ChatGPT, etc.) and paste responses back into markdown artifacts.

## Core Methodologies

Jeff combines three product discovery frameworks:

1. **User Story Mapping (Patton)** - Backbone (user activities) → Walking Skeleton (MVP slice) → Ribs (stories per activity)
2. **Opportunity Solution Trees (Torres)** - Desired Outcome → Opportunities → Solutions → Experiments
3. **Hypothesis-Driven Development (Klein)** - Assumption → Metric → Validation Method → Result

## Key Artifacts

All artifacts live in `.jeff/` directory:
- `STORY_MAP.md` - The story map structure
- `OPPORTUNITIES.md` - The opportunity solution tree
- `HYPOTHESES.md` - Testable assumptions with validation plans
- `research/` - Interview notes, insights, validation results

## How Commands Work

Commands follow a pattern:
- `jeff <command>` - Prints a prompt (user copies to LLM)
- `jeff <command> --show` - Displays current artifact state
- `jeff <command> --list` - Lists items (for hypotheses)

The CLI does NOT call LLMs directly. It generates context-aware prompts that include current artifact state.

## Architecture

```
src/jeff/
├── cli.py              # Typer CLI entry point
├── config.py           # Project config management
├── commands/           # One module per command group
├── prompts/            # Markdown prompt templates
├── parsers/            # Extract structured data from artifacts
└── templates/          # Initial artifact templates for `jeff init`
```
