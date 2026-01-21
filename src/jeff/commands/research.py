"""Research capture workflow commands."""

import click

from jeff.config import require_jeff_dir


INTERVIEW_PROMPT = """# Interview Notes Prompt

You are helping capture user interview notes in a structured format.

## Your Task

Help document this interview in research/USER_INTERVIEWS.md.

**Capture:**
1. Context (role, background, how recruited)
2. Key quotes (verbatim when possible)
3. Observations (behavior, surprises, body language)
4. Pain points expressed
5. Goals and desires
6. Follow-up questions for next time

## Interview Note Template

```markdown
### Interview: [Participant ID] - [Date]

**Context:**
- Role/Background:
- How recruited:
- Current solution:

**Key Quotes:**
> "Direct quote"

**Observations:**
- [What you noticed]

**Pain Points:**
-

**Goals/Desires:**
-

**Follow-up Questions:**
-
```

## Tips

- Use participant IDs, not names (for privacy)
- Capture exact quotes when possible
- Note non-verbal cues
- Distinguish facts from interpretations
- Flag surprising or contradictory information
"""

INSIGHT_PROMPT = """# Insight Extraction Prompt

You are helping synthesize research into actionable insights.

## Context

An insight connects observations to implications. It's not just a finding - it explains WHY something matters and WHAT to do about it.

**Good insight:** "Users check competitor prices before purchasing (observed in 8/10 interviews), suggesting price transparency builds trust more than hiding it."

**Not an insight:** "8/10 users check competitor prices" (this is just a finding)

## Your Task

Help extract insights and add them to research/INSIGHTS.md.

**Process:**
1. Review recent interviews and experiments
2. Identify patterns (things that appear 3+ times)
3. Connect patterns to implications
4. Link insights to opportunities

## Insight Template

```markdown
### Insight: [Title]

**Pattern:** [What did you observe repeatedly?]

**Evidence:**
- [Source 1]
- [Source 2]
- [Source 3]

**Implication:** [What should we do differently?]

**Related Opportunities:** [Links to OPPORTUNITIES.md]
```

## Questions to Consider

- What surprised us?
- What contradicted our assumptions?
- What do users say vs. what do they do?
- What patterns cut across multiple interviews?
"""


@click.command()
@click.argument("subcommand", type=click.Choice(["interview", "insight"]))
def research(subcommand: str):
    """Print prompts for research capture.

    \b
    Subcommands:
      interview  - Prompt for capturing interview notes
      insight    - Prompt for extracting insights from research
    """
    jeff_dir = require_jeff_dir()

    if subcommand == "interview":
        click.echo(INTERVIEW_PROMPT)

        # Show current interviews
        interviews_path = jeff_dir / "research" / "USER_INTERVIEWS.md"
        if interviews_path.exists():
            click.echo("\n---\n")
            click.echo("## Current Interview Notes\n")
            click.echo(interviews_path.read_text())

    elif subcommand == "insight":
        click.echo(INSIGHT_PROMPT)

        # Show current insights
        insights_path = jeff_dir / "research" / "INSIGHTS.md"
        if insights_path.exists():
            click.echo("\n---\n")
            click.echo("## Current Insights\n")
            click.echo(insights_path.read_text())
