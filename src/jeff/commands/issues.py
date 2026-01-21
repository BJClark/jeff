"""GitHub issue generation commands."""

import subprocess
import re
from pathlib import Path
from dataclasses import dataclass

import click

from jeff.config import require_jeff_dir, load_config
from jeff.prompts import get_prompt
from jeff.parsers.story_map import parse_story_map, Story
from jeff.parsers.opportunity import parse_opportunities, Solution


@dataclass
class Issue:
    """A generated issue draft."""
    title: str
    body: str
    labels: list[str]
    source: str  # "story_map", "opportunity", "hypothesis"
    source_ref: str  # Reference to the source item


def generate_story_issue(story: Story, config: dict) -> Issue:
    """Generate an issue from a story map item."""
    priority = "MVP" if story.section == "skeleton" else "Release 1" if story.section == "release1" else "Future"

    body = f"""## Summary
{story.title}

## Context
- **Activity:** {story.activity}
- **Priority:** {priority}
- **Source:** STORY_MAP.md

## Acceptance Criteria
- [ ] _Define acceptance criteria_

## Notes
_Add technical notes and dependencies_
"""
    labels = config.get("github", {}).get("labels", ["jeff"])
    if story.section == "skeleton":
        labels = labels + ["mvp"]

    prefix = config.get("github", {}).get("title_prefix", "")
    title = f"{prefix}{story.title}" if prefix else story.title

    return Issue(
        title=title,
        body=body,
        labels=labels,
        source="story_map",
        source_ref=f"{story.activity}: {story.title}"
    )


def generate_solution_issue(solution: Solution, config: dict) -> Issue:
    """Generate an issue from an opportunity solution."""
    assumptions_text = "\n".join(f"- {a}" for a in solution.assumptions) if solution.assumptions else "_None specified_"

    body = f"""## Summary
{solution.title}

## Context
- **Opportunity:** {solution.opportunity}
- **Source:** OPPORTUNITIES.md

## Assumptions
{assumptions_text}

## Experiment
{solution.experiment or "_Define experiment_"}

## Acceptance Criteria
- [ ] _Define acceptance criteria_

## Notes
_Add technical notes and dependencies_
"""
    labels = config.get("github", {}).get("labels", ["jeff"]) + ["opportunity"]

    prefix = config.get("github", {}).get("title_prefix", "")
    title = f"{prefix}{solution.title}" if prefix else solution.title

    return Issue(
        title=title,
        body=body,
        labels=labels,
        source="opportunity",
        source_ref=f"{solution.opportunity}: {solution.title}"
    )


def collect_issues(jeff_dir: Path, config: dict) -> list[Issue]:
    """Collect issues from all artifacts."""
    issues = []

    # Parse story map
    story_map_path = jeff_dir / "STORY_MAP.md"
    if story_map_path.exists():
        content = story_map_path.read_text()
        stories = parse_story_map(content)
        # Only generate issues for skeleton and release1 stories
        for story in stories:
            if story.section in ("skeleton", "release1") and not story.title.startswith("_"):
                issues.append(generate_story_issue(story, config))

    # Parse opportunities
    opp_path = jeff_dir / "OPPORTUNITIES.md"
    if opp_path.exists():
        content = opp_path.read_text()
        solutions = parse_opportunities(content)
        for solution in solutions:
            if not solution.title.startswith("["):  # Skip placeholders
                issues.append(generate_solution_issue(solution, config))

    return issues


def create_github_issue(issue: Issue) -> tuple[bool, str]:
    """Create a GitHub issue using gh CLI."""
    cmd = [
        "gh", "issue", "create",
        "--title", issue.title,
        "--body", issue.body,
    ]

    for label in issue.labels:
        cmd.extend(["--label", label])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        # gh returns the issue URL on success
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()
    except FileNotFoundError:
        return False, "gh CLI not found. Install from https://cli.github.com/"


@click.command()
@click.option("--create", "create_issues", is_flag=True, help="Create issues via gh CLI")
@click.option("--dry-run", is_flag=True, help="Preview issues without creating")
def issues(create_issues: bool, dry_run: bool):
    """Print prompt for generating issues from artifacts.

    Use --dry-run to preview issues that would be created.
    Use --create to create issues directly via gh CLI.
    """
    jeff_dir = require_jeff_dir()
    config = load_config(jeff_dir)

    if dry_run or create_issues:
        issue_list = collect_issues(jeff_dir, config)

        if not issue_list:
            click.echo("No issues to generate. Add content to STORY_MAP.md or OPPORTUNITIES.md first.")
            return

        click.echo(f"Found {len(issue_list)} potential issues:\n")

        for i, issue in enumerate(issue_list, 1):
            click.echo(f"{'='*60}")
            click.echo(f"Issue {i}: {issue.title}")
            click.echo(f"Source: {issue.source} - {issue.source_ref}")
            click.echo(f"Labels: {', '.join(issue.labels)}")
            click.echo(f"{'='*60}")
            click.echo(issue.body)
            click.echo()

            if create_issues:
                click.echo("Creating issue...")
                success, result = create_github_issue(issue)
                if success:
                    click.echo(f"Created: {result}\n")
                else:
                    click.echo(f"Failed: {result}\n")

    else:
        # Print the prompt
        prompt = get_prompt("issues")
        click.echo(prompt)

        # Show summary of what's available
        click.echo("\n---\n")
        click.echo("## Available Artifacts\n")

        story_map_path = jeff_dir / "STORY_MAP.md"
        if story_map_path.exists():
            stories = parse_story_map(story_map_path.read_text())
            skeleton = [s for s in stories if s.section == "skeleton" and not s.title.startswith("_")]
            release1 = [s for s in stories if s.section == "release1" and not s.title.startswith("_")]
            click.echo(f"- STORY_MAP.md: {len(skeleton)} skeleton stories, {len(release1)} release 1 stories")
        else:
            click.echo("- STORY_MAP.md: not found")

        opp_path = jeff_dir / "OPPORTUNITIES.md"
        if opp_path.exists():
            solutions = parse_opportunities(opp_path.read_text())
            real_solutions = [s for s in solutions if not s.title.startswith("[")]
            click.echo(f"- OPPORTUNITIES.md: {len(real_solutions)} solutions")
        else:
            click.echo("- OPPORTUNITIES.md: not found")

        click.echo("\nUse 'jeff issues --dry-run' to preview generated issues.")
        click.echo("Use 'jeff issues --create' to create them via gh CLI.")
