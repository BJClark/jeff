---
name: jeff:bdd
description: Generate BDD-style tasks with acceptance criteria
allowed-tools:
  - Bash
  - Read
  - Write
---

<objective>
Generate BDD-style tasks with Gherkin acceptance criteria from jeff artifacts.
</objective>

<process>

1. **Check if jeff is initialized:**
   ```bash
   [ -d .jeff ] || echo "Run 'jeff init' first to initialize the project"
   ```

2. **Get the BDD prompt:**
   ```bash
   jeff bdd
   ```

3. **Read current artifacts:**
   ```bash
   cat .jeff/STORY_MAP.md
   cat .jeff/OPPORTUNITIES.md
   ```

4. **Generate BDD tasks:**
   For each user story, create:
   - Feature description
   - User story (As a... I want... So that...)
   - Acceptance criteria in Gherkin format (Given/When/Then)

5. **Write to tasks file:**
   Update `.jeff/TASKS.md` with generated BDD tasks.

</process>
