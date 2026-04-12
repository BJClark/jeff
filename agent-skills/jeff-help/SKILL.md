---
name: jeff-help
description: Show the jeff product-discovery command reference and typical workflow. Use when the user asks "what can jeff do", "how do I use jeff", or wants an overview.
allowed-tools: Read
metadata:
  author: Will Clark
  version: "0.1.0"
  source-repo: https://github.com/BJClark/jeff
---

## Objective

Display the jeff command reference and guide new users through the product discovery workflow.

## Response

### Jeff — Product Discovery Skills

Jeff combines three frameworks for AI-assisted product discovery:

- **User Story Mapping** (Jeff Patton) — map the user's journey before the feature backlog.
- **Opportunity Solution Trees** (Teresa Torres) — connect outcomes to opportunities to solutions to experiments.
- **Hypothesis-Driven Development** (Laura Klein) — turn risky assumptions into testable hypotheses.

### Available commands

| Command | What it does |
|---------|-------------|
| `jeff-init` | Scaffold `.jeff/` directory with artifact templates |
| `jeff-map` | Create or update the user story map |
| `jeff-opportunity` | Build an Opportunity Solution Tree |
| `jeff-hypothesis` | Create and track testable hypotheses |
| `jeff-research` | Capture interviews or synthesize insights |
| `jeff-bdd` | Generate BDD-style tasks with acceptance criteria |
| `jeff-issues` | Generate GitHub issues from artifacts |

### Typical workflow

```
jeff-init → jeff-map → jeff-opportunity → jeff-hypothesis → jeff-issues
```

1. **Start**: `jeff-init` scaffolds `.jeff/` with templates.
2. **Map**: `jeff-map` walks you through backbone, walking skeleton, ribs.
3. **Research**: `jeff-research` to capture interviews and extract insights.
4. **Opportunities**: `jeff-opportunity` to build the OST.
5. **Risks**: `jeff-hypothesis` to surface and validate assumptions.
6. **Build**: `jeff-bdd` for tasks, or `jeff-issues` for GitHub issues.

### Project structure

```
.jeff/
├── config.yaml
├── STORY_MAP.md
├── OPPORTUNITIES.md
├── HYPOTHESES.md
├── TASKS.md
├── research/
│   ├── USER_INTERVIEWS.md
│   ├── INSIGHTS.md
│   └── VALIDATION_RESULTS.md
└── issues/
```
