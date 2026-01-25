"""Main CLI entry point for jeff."""

import click

from jeff.commands.init import init
from jeff.commands.map import map_cmd
from jeff.commands.opportunity import opportunity
from jeff.commands.hypothesis import hypothesis
from jeff.commands.research import research
from jeff.commands.issues import issues
from jeff.commands.bdd import bdd


@click.group()
@click.version_option()
def main():
    """jeff - Specification CLI for Product Discovery.

    Generates specification artifacts combining User Story Mapping (Patton),
    hypothesis-driven validation (Klein), and Opportunity Solution Trees (Torres).
    """
    pass


main.add_command(init)
main.add_command(map_cmd, name="map")
main.add_command(opportunity)
main.add_command(hypothesis)
main.add_command(research)
main.add_command(issues)
main.add_command(bdd)


if __name__ == "__main__":
    main()
