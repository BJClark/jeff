"""BDD tasks generation commands."""

import re
import subprocess
from pathlib import Path
from dataclasses import dataclass, field

import click

from jeff.config import require_jeff_dir, load_config
from jeff.prompts import get_prompt
from jeff.parsers.story_map import parse_story_map


@dataclass
class Task:
    """A task from TASKS.md."""
    id: str
    title: str
    priority: str
    source: str
    status: str
    description: str = ""
    acceptance_criteria: list[str] = field(default_factory=list)
    notes: str = ""


def parse_tasks(content: str) -> list[Task]:
    """Parse tasks from TASKS.md content."""
    tasks = []

    # Parse the overview table for basic info
    lines = content.split("\n")
    task_basics = {}

    for line in lines:
        line_stripped = line.strip()

        # Look for table rows starting with | T
        if line_stripped.startswith("| T") and "|" in line_stripped:
            cells = [c.strip() for c in line_stripped.split("|") if c.strip()]
            if len(cells) >= 5:
                task_basics[cells[0]] = {
                    "id": cells[0],
                    "title": cells[1],
                    "priority": cells[2],
                    "source": cells[3],
                    "status": cells[4]
                }

    # Parse detailed task sections
    current_task_id = None
    current_section = None
    description_lines = []
    criteria_lines = []
    notes_lines = []

    for line in lines:
        # Match task headers like "### T1: Task Title"
        task_match = re.match(r'^###\s+(T\d+):\s+(.+)$', line.strip())
        if task_match:
            # Save previous task if exists
            if current_task_id and current_task_id in task_basics:
                task_basics[current_task_id]["description"] = "\n".join(description_lines).strip()
                task_basics[current_task_id]["acceptance_criteria"] = [
                    c.strip() for c in criteria_lines if c.strip()
                ]
                task_basics[current_task_id]["notes"] = "\n".join(notes_lines).strip()

            current_task_id = task_match.group(1)
            description_lines = []
            criteria_lines = []
            notes_lines = []
            current_section = None
            continue

        if current_task_id:
            if line.strip().startswith("**Description:**"):
                current_section = "description"
                continue
            elif line.strip().startswith("**Acceptance Criteria:**"):
                current_section = "criteria"
                continue
            elif line.strip().startswith("**Notes:**"):
                current_section = "notes"
                continue
            elif line.strip().startswith("**"):
                current_section = None
                continue
            elif line.strip().startswith("###"):
                current_section = None

            if current_section == "description":
                description_lines.append(line)
            elif current_section == "criteria":
                # Parse checkbox items
                criteria_match = re.match(r'^-\s*\[.\]\s*(.+)$', line.strip())
                if criteria_match:
                    criteria_lines.append(criteria_match.group(1))
            elif current_section == "notes":
                notes_lines.append(line)

    # Save last task
    if current_task_id and current_task_id in task_basics:
        task_basics[current_task_id]["description"] = "\n".join(description_lines).strip()
        task_basics[current_task_id]["acceptance_criteria"] = [
            c.strip() for c in criteria_lines if c.strip()
        ]
        task_basics[current_task_id]["notes"] = "\n".join(notes_lines).strip()

    # Build task objects
    for task_id in sorted(task_basics.keys()):
        info = task_basics[task_id]
        tasks.append(Task(
            id=info["id"],
            title=info["title"],
            priority=info["priority"],
            source=info["source"],
            status=info["status"],
            description=info.get("description", ""),
            acceptance_criteria=info.get("acceptance_criteria", []),
            notes=info.get("notes", "")
        ))

    return tasks


def get_task_summary(tasks: list[Task]) -> dict:
    """Get summary counts by status and priority."""
    summary = {
        "total": len(tasks),
        "by_status": {},
        "by_priority": {}
    }

    for task in tasks:
        status = task.status.lower()
        priority = task.priority.lower()

        summary["by_status"][status] = summary["by_status"].get(status, 0) + 1
        summary["by_priority"][priority] = summary["by_priority"].get(priority, 0) + 1

    return summary


def format_issue_body(task: Task) -> str:
    """Format a task as a GitHub issue body."""
    criteria_text = "\n".join(f"- [ ] {c}" for c in task.acceptance_criteria) if task.acceptance_criteria else "- [ ] _Define acceptance criteria_"

    body = f"""## Summary
{task.description or task.title}

## Context
- **Task ID:** {task.id}
- **Priority:** {task.priority}
- **Source:** {task.source}

## Acceptance Criteria
{criteria_text}

## Notes
{task.notes or "_Add technical notes and dependencies_"}

---
_Generated from TASKS.md via `jeff bdd --create`_
"""
    return body


def create_github_issue(task: Task, config: dict) -> tuple[bool, str]:
    """Create a GitHub issue using gh CLI."""
    labels = config.get("github", {}).get("labels", ["jeff"])

    # Add priority label
    priority_lower = task.priority.lower()
    if priority_lower == "mvp":
        labels = labels + ["mvp"]
    elif priority_lower == "release 1":
        labels = labels + ["release-1"]

    prefix = config.get("github", {}).get("title_prefix", "")
    title = f"{prefix}[{task.id}] {task.title}" if prefix else f"[{task.id}] {task.title}"

    body = format_issue_body(task)

    cmd = [
        "gh", "issue", "create",
        "--title", title,
        "--body", body,
    ]

    for label in labels:
        cmd.extend(["--label", label])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()
    except FileNotFoundError:
        return False, "gh CLI not found. Install from https://cli.github.com/"


@click.command()
@click.option("--show", is_flag=True, help="Display current TASKS.md only")
@click.option("--list", "list_tasks", is_flag=True, help="Show summary of tasks by status")
@click.option("--create", "create_issues", is_flag=True, help="Create GitHub issues via gh CLI")
@click.option("--dry-run", is_flag=True, help="Preview issues without creating")
@click.option("--status", "filter_status", default="pending", help="Filter tasks by status (default: pending)")
def bdd(show: bool, list_tasks: bool, create_issues: bool, dry_run: bool, filter_status: str):
    """Print prompt for generating implementation tasks from artifacts.

    Transforms product discovery artifacts (STORY_MAP.md, OPPORTUNITIES.md)
    into structured, behavior-focused implementation tasks.

    Use --show to display the current TASKS.md.
    Use --list to see a summary of tasks by status.
    Use --dry-run to preview GitHub issues that would be created.
    Use --create to create GitHub issues via gh CLI.
    Use --status to filter which tasks to create issues for (default: pending).
    """
    jeff_dir = require_jeff_dir()
    config = load_config(jeff_dir)

    tasks_path = jeff_dir / "TASKS.md"

    if show:
        # Display current TASKS.md only
        if tasks_path.exists():
            click.echo(tasks_path.read_text())
        else:
            click.echo("TASKS.md not found. Run 'jeff init' to create it.")
        return

    if list_tasks:
        # Show summary of tasks
        if not tasks_path.exists():
            click.echo("TASKS.md not found. Run 'jeff init' to create it.")
            return

        content = tasks_path.read_text()
        tasks = parse_tasks(content)

        if not tasks:
            click.echo("No tasks found in TASKS.md. Use 'jeff bdd' to generate tasks.")
            return

        summary = get_task_summary(tasks)

        click.echo(f"Task Summary: {summary['total']} total tasks\n")

        click.echo("By Status:")
        for status, count in sorted(summary["by_status"].items()):
            click.echo(f"  {status}: {count}")

        click.echo("\nBy Priority:")
        for priority, count in sorted(summary["by_priority"].items()):
            click.echo(f"  {priority}: {count}")

        click.echo("\nUse 'jeff bdd --show' to see full TASKS.md.")
        return

    if dry_run or create_issues:
        # Create GitHub issues from tasks
        if not tasks_path.exists():
            click.echo("TASKS.md not found. Run 'jeff init' to create it.")
            return

        content = tasks_path.read_text()
        all_tasks = parse_tasks(content)

        if not all_tasks:
            click.echo("No tasks found in TASKS.md. Use 'jeff bdd' to generate tasks first.")
            return

        # Filter by status
        filtered_tasks = [
            t for t in all_tasks
            if t.status.lower() == filter_status.lower()
        ]

        if not filtered_tasks:
            click.echo(f"No tasks with status '{filter_status}' found.")
            click.echo(f"Available statuses: {', '.join(set(t.status for t in all_tasks))}")
            return

        click.echo(f"Found {len(filtered_tasks)} tasks with status '{filter_status}':\n")

        for task in filtered_tasks:
            click.echo(f"{'='*60}")
            click.echo(f"[{task.id}] {task.title}")
            click.echo(f"Priority: {task.priority} | Source: {task.source}")
            click.echo(f"{'='*60}")
            click.echo(format_issue_body(task))
            click.echo()

            if create_issues:
                click.echo("Creating issue...")
                success, result = create_github_issue(task, config)
                if success:
                    click.echo(f"Created: {result}\n")
                else:
                    click.echo(f"Failed: {result}\n")

        if dry_run:
            click.echo("Use 'jeff bdd --create' to create these issues.")
            click.echo("Use 'jeff bdd --create --status <status>' to filter by a different status.")
        return

    # Default: Print prompt + current TASKS.md state
    prompt = get_prompt("bdd")
    click.echo(prompt)

    click.echo("\n---\n")
    click.echo("## Source Artifacts\n")

    # Show summary of available artifacts
    story_map_path = jeff_dir / "STORY_MAP.md"
    if story_map_path.exists():
        stories = parse_story_map(story_map_path.read_text())
        skeleton = [s for s in stories if s.section == "skeleton" and not s.title.startswith("_")]
        release1 = [s for s in stories if s.section == "release1" and not s.title.startswith("_")]
        future = [s for s in stories if s.section == "future" and not s.title.startswith("_")]
        click.echo(f"- STORY_MAP.md: {len(skeleton)} skeleton, {len(release1)} release 1, {len(future)} future stories")
    else:
        click.echo("- STORY_MAP.md: not found")

    opp_path = jeff_dir / "OPPORTUNITIES.md"
    if opp_path.exists():
        click.echo("- OPPORTUNITIES.md: available")
    else:
        click.echo("- OPPORTUNITIES.md: not found")

    click.echo("\n## Current TASKS.md State\n")

    if tasks_path.exists():
        content = tasks_path.read_text()
        tasks = parse_tasks(content)

        if tasks:
            summary = get_task_summary(tasks)
            click.echo(f"Existing tasks: {summary['total']}")
            for status, count in sorted(summary["by_status"].items()):
                click.echo(f"  - {status}: {count}")
        else:
            click.echo("Template ready - no tasks defined yet.")

        click.echo("\n---\n")
        click.echo("Current TASKS.md content:\n")
        click.echo(content)
    else:
        click.echo("TASKS.md not found. Run 'jeff init' to create it.")

    click.echo("\nUse 'jeff bdd --show' to display TASKS.md only.")
    click.echo("Use 'jeff bdd --list' to see task summary.")
    click.echo("Use 'jeff bdd --dry-run' to preview GitHub issues.")
    click.echo("Use 'jeff bdd --create' to create GitHub issues.")
