---
name: jeff:map
description: Create or update a user story map following Jeff Patton's methodology
allowed-tools:
  - Bash
  - Read
  - Write
---

<objective>
Help the user create or update their story map using Jeff Patton's User Story Mapping methodology.
</objective>

<process>

1. **Check if jeff is initialized:**
   ```bash
   [ -d .jeff ] || echo "Run 'jeff init' first to initialize the project"
   ```

2. **Get the story map prompt:**
   ```bash
   jeff map
   ```

3. **Read current story map state:**
   ```bash
   cat .jeff/STORY_MAP.md
   ```

4. **Help the user build their story map:**
   - **Backbone**: User activities (big things users do)
   - **Walking Skeleton**: Minimum viable slice through each activity
   - **Ribs**: User stories hanging off each backbone item

5. **Write updates to the story map:**
   After discussing with the user, update `.jeff/STORY_MAP.md` with the new content.

</process>

<methodology>
User Story Mapping (Jeff Patton):
- Start with user activities (backbone) - the big things users do
- Add the walking skeleton - minimum steps to complete each activity
- Fill in ribs - detailed stories for each step
- Slice horizontally for releases
</methodology>
