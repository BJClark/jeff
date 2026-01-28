---
name: jeff:research
description: Capture user research - interviews and insights
allowed-tools:
  - Bash
  - Read
  - Write
---

<objective>
Help the user capture user research including interview notes and synthesized insights.
</objective>

<process>

1. **Check if jeff is initialized:**
   ```bash
   [ -d .jeff ] || echo "Run 'jeff init' first to initialize the project"
   ```

2. **Determine research type:**
   Ask the user: "Are you capturing an interview or extracting insights?"

3. **For interviews:**
   ```bash
   jeff research interview
   cat .jeff/research/USER_INTERVIEWS.md
   ```
   Help capture: participant info, key quotes, observations, follow-up questions.

4. **For insights:**
   ```bash
   jeff research insight
   cat .jeff/research/INSIGHTS.md
   ```
   Help extract patterns across interviews and connect to opportunities.

5. **Write updates:**
   Update the appropriate file in `.jeff/research/`.

</process>
