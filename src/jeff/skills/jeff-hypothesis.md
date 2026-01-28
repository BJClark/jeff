---
name: jeff:hypothesis
description: Create and track hypotheses for validation following Laura Klein's methodology
allowed-tools:
  - Bash
  - Read
  - Write
---

<objective>
Help the user create and track hypotheses for validation using Laura Klein's hypothesis-driven development approach.
</objective>

<process>

1. **Check if jeff is initialized:**
   ```bash
   [ -d .jeff ] || echo "Run 'jeff init' first to initialize the project"
   ```

2. **Get the hypothesis prompt:**
   ```bash
   jeff hypothesis
   ```

3. **Read current hypotheses:**
   ```bash
   cat .jeff/HYPOTHESES.md
   ```

4. **Help the user formulate hypotheses:**
   - **Assumption**: What do we believe to be true?
   - **Metric**: How will we measure success?
   - **Validation Method**: How will we test this?
   - **Result**: What did we learn?

5. **Write updates to hypotheses:**
   After discussing with the user, update `.jeff/HYPOTHESES.md` with the new content.

</process>

<methodology>
Hypothesis-Driven Development (Laura Klein):
- Identify risky assumptions
- Turn assumptions into testable hypotheses
- Define clear success metrics
- Design minimum viable tests
- Record learnings and pivot/persevere
</methodology>
