"""Opportunity Solution Tree workflow commands."""

import click

from jeff.config import require_jeff_dir
from jeff.prompts import get_prompt


@click.command()
@click.option("--show", is_flag=True, help="Display current opportunity solution tree")
def opportunity(show: bool):
    """Print prompt for OST creation/refinement.

    Use --show to display the current opportunity solution tree instead.
    """
    jeff_dir = require_jeff_dir()

    if show:
        ost_path = jeff_dir / "OPPORTUNITIES.md"
        if ost_path.exists():
            click.echo(ost_path.read_text())
        else:
            raise click.ClickException("OPPORTUNITIES.md not found")
    else:
        # Print the prompt
        prompt = get_prompt("opportunity")
        click.echo(prompt)

        # Also show current state if exists
        ost_path = jeff_dir / "OPPORTUNITIES.md"
        if ost_path.exists():
            click.echo("\n---\n")
            click.echo("## Current Opportunity Solution Tree\n")
            click.echo(ost_path.read_text())
