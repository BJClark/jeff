# Acceptance Criteria — Quality Rules and Anti-Patterns

Acceptance criteria are the contract between discovery and engineering. They answer "how will we know this is done, from the user's perspective?" without prescribing how to build it.

## The three rules

### 1. Behaviour-level, not implementation-level

Criteria describe what the user or system does, not what the code looks like.

Good:
- "When the user taps 'Save', the recipe appears in their Saved list."
- "If the shopping list is empty, the UI shows an empty state with a prompt to add recipes."

Bad:
- "The `RecipeController.save()` method returns a 201 with the saved recipe JSON."
- "The React state `savedRecipes` is updated after the API call resolves."

The engineering team decides how to build. Acceptance criteria describe the observable outcome.

### 2. Independently pass/fail

Each criterion is its own checkbox. If two conditions need to both be true for a scenario to pass, that's one criterion with an "and", not two criteria.

Good:
- "The user sees their saved recipes in order by save date, most recent first."

Bad as two criteria:
- "The user sees their saved recipes."
- "Recipes are ordered most recent first."
  
(These are two assertions about one behaviour. Keep them together or QA will double-count.)

### 3. Adds user or business value

Every criterion should be a thing a user or stakeholder could care about. "The code should be clean" isn't acceptance criteria — it's engineering standard. Criteria live in the user's world.

Bad criteria (not user-facing):
- "The component uses hooks, not class state."
- "The function has ≥80% test coverage."
- "SQL queries are parameterised."

These are engineering practices. They belong in definition-of-done or code review, not acceptance criteria.

## "Should" statements vs Gherkin

Two idioms, both acceptable. Pick the one that reads cleaner for the specific behaviour:

**Should statements** — tighter, good for simple behaviours:
- "The system should show the empty state when no recipes are saved."
- "The system should prevent submitting the form without an email."

**Gherkin (Given / When / Then)** — better for conditional or multi-step behaviours:
- **Given** the user has 3 saved recipes
- **When** they tap 'Generate shopping list'
- **Then** the system combines ingredients and displays the merged list

Don't mix both in one criterion. A task can have some `should` criteria and some Gherkin — but each individual criterion commits to one style.

## Too many criteria is a smell

If a task has 8+ acceptance criteria, it's probably two tasks. Either the behaviour is too broad (split the title) or the criteria are too granular (consolidate pass/fail pairs into one criterion).

Rule of thumb: 3–6 criteria per task. Fewer and the task is probably trivial; more and it probably needs splitting.

## Anti-pattern: "happy path only"

Criteria only describe the success case. No error states, no empty states, no edge cases.

Bad:
- "The user can save a recipe."

Better:
- "When the user taps 'Save' on a recipe they haven't saved yet, the recipe is added to Saved."
- "When the user taps 'Save' on a recipe already in Saved, the system leaves the list unchanged and shows 'Already saved'."
- "If the save API fails, the system shows a retry prompt; the recipe is not silently lost."

Three criteria, three states. QA has something to actually test.

## Anti-pattern: untestable language

Criteria use fuzzy verbs that can't be pass/fail:

- "The system should feel fast." → Pick a threshold: "The saved-recipes list renders within 200ms."
- "The user should be delighted." → Unmeasurable; cut it.
- "The UI should be intuitive." → Replace with specific behaviours: "First-time users complete the save flow without help."

If you can't write a test (automated or manual) that clearly passes or fails against a criterion, rewrite the criterion.

## Anti-pattern: feature list masquerading as criteria

Each bullet describes *what to build* not *what should happen*.

Bad:
- "Build a modal."
- "Add a form with email and password fields."
- "Submit button sends a POST to /api/signup."

Better:
- "When the user taps 'Sign up', they see a form with email and password fields."
- "If either field is empty when they tap 'Create account', the system shows an inline error next to the empty field."
- "On successful signup, the user is logged in and redirected to the onboarding screen."

The first set is a spec. The second is acceptance criteria.
