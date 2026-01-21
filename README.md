# jeff - Specification CLI for Product Discovery

A CLI that generates specification artifacts combining User Story Mapping (Patton), hypothesis-driven validation (Klein), and Opportunity Solution Trees (Torres).

## Installation

```bash
uv sync
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
