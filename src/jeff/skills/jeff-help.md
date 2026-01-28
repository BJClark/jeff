---
name: jeff:help
description: Show available jeff commands for product discovery workflows
allowed-tools:
  - Bash
---

<objective>
Display the jeff command reference for product discovery.
</objective>

Run `jeff --help` to show the available commands, then explain the workflow:

1. `jeff init` - Initialize a new project with .jeff/ directory
2. `jeff map` - Create/update story map (User Story Mapping - Patton)
3. `jeff opportunity` - Create Opportunity Solution Tree (Torres)
4. `jeff hypothesis` - Track hypotheses and validation (Klein)
5. `jeff research interview` - Capture user interview notes
6. `jeff research insight` - Extract insights from research
7. `jeff issues` - Generate GitHub issues from artifacts
8. `jeff bdd` - Generate BDD-style tasks with acceptance criteria

Typical workflow:
```
jeff init → jeff map → jeff opportunity → jeff hypothesis → jeff issues
```

Each command generates a prompt. Copy it to your AI assistant, get the response, and paste it back into the artifact file in `.jeff/`.
