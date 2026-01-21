"""Hypothesis tracking workflow commands."""

import re

import click

from jeff.config import require_jeff_dir
from jeff.prompts import get_prompt


def parse_hypotheses(content: str) -> list[dict]:
    """Parse hypotheses from HYPOTHESES.md content."""
    hypotheses = []

    # Match hypothesis blocks starting with ### H followed by number
    pattern = r"### (H\d+): ([^\n]+)\n(.*?)(?=\n### H\d+:|\n## |\Z)"
    matches = re.findall(pattern, content, re.DOTALL)

    for match in matches:
        hyp_id, name, body = match
        status_match = re.search(r"\*\*Status:\*\*\s*([^\n]+)", body)
        status = status_match.group(1).strip() if status_match else "Unknown"

        hypotheses.append({
            "id": hyp_id,
            "name": name.strip(),
            "status": status,
        })

    return hypotheses


@click.command()
@click.option("--list", "list_hypotheses", is_flag=True, help="List current hypotheses")
@click.option("--validate", "validate_id", help="Print prompt for validating a specific hypothesis")
def hypothesis(list_hypotheses: bool, validate_id: str):
    """Print prompt for hypothesis generation.

    Use --list to see current hypotheses.
    Use --validate ID to get a validation planning prompt.
    """
    jeff_dir = require_jeff_dir()
    hyp_path = jeff_dir / "HYPOTHESES.md"

    if list_hypotheses:
        if not hyp_path.exists():
            raise click.ClickException("HYPOTHESES.md not found")

        content = hyp_path.read_text()
        hypotheses = parse_hypotheses(content)

        if not hypotheses:
            click.echo("No hypotheses found.")
            return

        click.echo("Current Hypotheses:\n")
        for h in hypotheses:
            click.echo(f"  {h['id']}: {h['name']}")
            click.echo(f"      Status: {h['status']}")
            click.echo()

    elif validate_id:
        if not hyp_path.exists():
            raise click.ClickException("HYPOTHESES.md not found")

        content = hyp_path.read_text()

        # Find the specific hypothesis
        pattern = rf"### ({validate_id}): ([^\n]+)\n(.*?)(?=\n### H\d+:|\n## |\Z)"
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

        if not match:
            raise click.ClickException(f"Hypothesis {validate_id} not found")

        hyp_id, name, body = match.groups()

        click.echo(f"# Validation Planning: {hyp_id} - {name}\n")
        click.echo("## Current Hypothesis\n")
        click.echo(f"### {hyp_id}: {name}")
        click.echo(body.strip())
        click.echo("\n---\n")
        click.echo("## Validation Prompt\n")
        click.echo("""Help plan validation for this hypothesis.

Consider:
1. What's the riskiest assumption to test first?
2. What's the lightest-weight experiment that could falsify it?
3. How do we measure the metric defined?
4. What sample size gives us confidence?
5. What's our timeline?

Suggest a concrete validation plan with:
- Experiment design
- Success/failure criteria
- Timeline
- Resources needed
""")

    else:
        # Print the prompt
        prompt = get_prompt("hypothesis")
        click.echo(prompt)

        # Also show current state if exists
        if hyp_path.exists():
            click.echo("\n---\n")
            click.echo("## Current Hypotheses\n")
            click.echo(hyp_path.read_text())
