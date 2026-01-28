---
name: jeff:opportunity
description: Create or update an Opportunity Solution Tree following Teresa Torres' methodology
allowed-tools:
  - Bash
  - Read
  - Write
---

<objective>
Help the user create or update their Opportunity Solution Tree using Teresa Torres' methodology.
</objective>

<process>

1. **Check if jeff is initialized:**
   ```bash
   [ -d .jeff ] || echo "Run 'jeff init' first to initialize the project"
   ```

2. **Get the opportunity prompt:**
   ```bash
   jeff opportunity
   ```

3. **Read current OST state:**
   ```bash
   cat .jeff/OPPORTUNITIES.md
   ```

4. **Help the user build their OST:**
   - **Desired Outcome**: What business/user outcome are we targeting?
   - **Opportunities**: Customer needs, pain points, desires
   - **Solutions**: Ideas to address each opportunity
   - **Experiments**: Ways to test each solution

5. **Write updates to the OST:**
   After discussing with the user, update `.jeff/OPPORTUNITIES.md` with the new content.

</process>

<methodology>
Opportunity Solution Trees (Teresa Torres):
- Start with a clear desired outcome (measurable)
- Discover opportunities through continuous research
- Generate multiple solutions per opportunity
- Design small experiments to test assumptions
</methodology>
