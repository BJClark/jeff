"""Story mapping workflow commands."""

import click

from jeff.config import require_jeff_dir
from jeff.prompts import get_prompt


@click.command("map")
@click.option("--show", is_flag=True, help="Display current story map")
def map_cmd(show: bool):
    """Print prompt for creating/updating story map.

    Use --show to display the current story map instead.
    """
    jeff_dir = require_jeff_dir()

    if show:
        story_map_path = jeff_dir / "STORY_MAP.md"
        if story_map_path.exists():
            click.echo(story_map_path.read_text())
        else:
            raise click.ClickException("STORY_MAP.md not found")
    else:
        # Print the prompt
        prompt = get_prompt("story-map")
        click.echo(prompt)

        # Also show current state if exists
        story_map_path = jeff_dir / "STORY_MAP.md"
        if story_map_path.exists():
            click.echo("\n---\n")
            click.echo("## Current Story Map\n")
            click.echo(story_map_path.read_text())
