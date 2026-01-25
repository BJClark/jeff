# BDD Tasks Generation Prompt

You are helping transform product discovery artifacts into structured, behavior-focused implementation tasks for engineers.

## Context

Good implementation tasks bridge product thinking and engineering execution. They should:
- Be behavior-focused (what the system should do, not how)
- Include clear acceptance criteria using "should" statements
- Be code-agnostic (no implementation details)
- Link back to source artifacts for context
- Be independently deliverable

## Your Task

Review the artifacts and generate implementation tasks in TASKS.md format.

**Sources to review:**
1. STORY_MAP.md - Walking skeleton and Release 1 stories
2. OPPORTUNITIES.md - Solutions and business context

**For each task:**
1. Write a clear, behavior-focused title
2. Link to the source artifact
3. Assign appropriate priority (MVP / Release 1 / Future)
4. Write a description of what needs to be accomplished
5. Define acceptance criteria using "should" statements
6. Add relevant context from opportunities

## Task Template

```markdown
### T[N]: [Task Title]
**Source:** STORY_MAP.md > [Activity] > [Story Title]
**Priority:** MVP / Release 1 / Future

**Description:**
[What needs to be accomplished from the user's perspective]

**Acceptance Criteria:**
- [ ] The system should [behavior 1]
- [ ] The system should [behavior 2]
- [ ] When [condition], then [expected behavior]
- [ ] Given [context], when [action], then [result]

**Notes:**
[Business context from opportunities, related tasks, dependencies]
```

## Acceptance Criteria Guidance

Write acceptance criteria that are:
- **Behavioral:** Describe what the system does, not how
- **Testable:** Can be verified as pass/fail
- **Independent:** Each criterion stands alone
- **Valuable:** Each adds user or business value

**Good examples:**
- "The system should display an error message when login fails"
- "When a user submits the form, then their data should be saved"
- "Given an authenticated user, when they view the dashboard, then they should see their recent activity"

**Avoid:**
- Implementation details ("The React component should...")
- Vague criteria ("The feature should work well")
- Technical jargon users wouldn't understand

## Priority Mapping

**MVP (Walking Skeleton):**
- Stories from the Walking Skeleton section
- End-to-end flow essentials
- Highest risk items to validate early

**Release 1:**
- Stories from Release 1 section
- Enhancements to the walking skeleton
- High-impact opportunity solutions

**Future:**
- Stories marked as Future
- Lower priority opportunities
- Nice-to-have enhancements

## Output Format

Update TASKS.md with:
1. The overview table (ID, Task, Priority, Source, Status)
2. Detailed task sections with acceptance criteria

Set initial status to "Pending" for all new tasks.

## Incremental Updates

If TASKS.md already has tasks:
- Preserve existing tasks and their statuses
- Add new tasks with incrementing IDs
- Note any conflicts between new stories and existing tasks
