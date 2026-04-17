# Example: Building a backbone from scratch

**User says:** "Let's start mapping out the onboarding flow for this product."

**Context:** `.jeff/STORY_MAP.md` exists but is empty (template placeholders only). This is a fresh discovery session for a recipe-planning SaaS.

**Claude's turn 1:** Read `.jeff/STORY_MAP.md`, confirm it's empty, and ask the backbone questions one at a time.

> "Great — we'll start with the backbone. First: who is the primary user going through onboarding? One persona is easier to map than a blend."

**User's answer:** "A home cook who just signed up after seeing a friend's shared meal plan."

**Claude's turn 2:**
> "Got it. What triggers them to start this journey — what's the moment just before they open the app for the first time?"

**User's answer:** "They click the share link in iMessage and land on the signup page."

**Claude's turn 3:**
> "And what does 'done' look like from their side — what's the first moment they'd say 'okay, I got what I came for'?"

**User's answer:** "They've saved a recipe to this week's plan and added ingredients to a shopping list."

**Claude's turn 4:**
> "Now walk me through the 3–8 big activities between clicking the link and that first-win moment. In the user's narrative order, not ours."

**User's answer:** "They sign in, tell us a bit about their diet, browse recipes, pick one they like, save it to this week, and generate a shopping list."

**Claude's turn 5:** Translate into verb-first activities and confirm.

> "So the backbone reads: **Sign in → Set preferences → Discover recipes → Save a recipe → Plan the week → Generate shopping list**. Six activities, narrative order. Sound right?"

**User:** "Yep — that's the spine."

**Claude writes to `.jeff/STORY_MAP.md`:**

```diff
 ## Backbone
 
-| <!-- Activity 1 --> | <!-- Activity 2 --> | ... |
+| Sign in | Set preferences | Discover recipes | Save a recipe | Plan the week | Generate shopping list |
```

**What to notice:** Claude asked the four backbone questions in sequence, one at a time, and translated the user's narrative into verb-first cells before committing. The user was never shown the template structure — only the resulting summary for confirmation. This is the "facilitate, don't transcribe" pattern.
