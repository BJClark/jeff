---
name: jeff:issues
description: Generate GitHub issues from jeff artifacts
allowed-tools:
  - Bash
  - Read
  - Write
---

<objective>
Generate GitHub issues from the story map, opportunities, and hypotheses.
</objective>

<process>

1. **Check if jeff is initialized:**
   ```bash
   [ -d .jeff ] || echo "Run 'jeff init' first to initialize the project"
   ```

2. **Get the issues prompt:**
   ```bash
   jeff issues
   ```

3. **Read current artifacts:**
   ```bash
   cat .jeff/STORY_MAP.md
   cat .jeff/OPPORTUNITIES.md
   cat .jeff/HYPOTHESES.md
   ```

4. **Help generate issues:**
   - Convert walking skeleton items to implementation issues
   - Create validation issues from hypotheses
   - Link issues to opportunities and outcomes

5. **Options for output:**
   - `jeff issues --dry-run` - Preview issues without creating
   - `jeff issues --create` - Create issues via gh CLI
   - Write to `.jeff/issues/` for manual review

</process>
