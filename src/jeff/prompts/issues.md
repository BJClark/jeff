# Issue Generation Prompt

You are helping convert product discovery artifacts into actionable GitHub issues.

## Context

Good issues bridge product thinking and engineering execution. They should:
- Be independently deliverable
- Include acceptance criteria
- Reference the "why" (linked opportunity/hypothesis)
- Be small enough to estimate

## Your Task

Review the artifacts and generate issue drafts.

**Sources to review:**
1. STORY_MAP.md - Walking skeleton and Release 1 stories
2. OPPORTUNITIES.md - Solutions ready to build
3. HYPOTHESES.md - Experiments that need implementation

**For each potential issue:**
1. Write a clear, action-oriented title
2. Describe what needs to be built
3. Define acceptance criteria
4. Link to source artifact and rationale
5. Suggest labels and priority

## Issue Template

```markdown
## Summary
[What needs to be built and why]

## Context
[Link to story/opportunity/hypothesis]
[Why this matters to users]

## Acceptance Criteria
- [ ] [Specific, testable criterion]
- [ ] [Another criterion]

## Notes
[Technical considerations, dependencies, open questions]
```

## Prioritization Guidance

**Build First:**
- Walking skeleton stories (end-to-end flow)
- High-risk hypothesis experiments
- High-impact opportunity solutions

**Build Later:**
- Release 1 enhancement stories
- Medium-risk experiments
- Lower-impact solutions

## Output Format

Generate issues as individual markdown blocks ready for GitHub.
