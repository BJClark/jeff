"""Initialize a new jeff project."""

import os
from datetime import datetime
from pathlib import Path

import click

from jeff.config import JEFF_DIR, find_jeff_root


DIRECTORIES = [
    "prompts",
    "research",
    "issues",
]

ARTIFACT_FILES = [
    "STORY_MAP.md",
    "OPPORTUNITIES.md",
    "HYPOTHESES.md",
]

RESEARCH_FILES = [
    "USER_INTERVIEWS.md",
    "VALIDATION_RESULTS.md",
    "INSIGHTS.md",
]

PROMPT_FILES = [
    "story-map.md",
    "hypothesis.md",
    "opportunity.md",
    "issues.md",
]


def get_template_content(template_name: str, project_name: str) -> str:
    """Load and format a template."""
    from jeff.templates import TEMPLATES_DIR

    # Try .md first, then .yaml
    for ext in [".md", ".yaml"]:
        template_path = TEMPLATES_DIR / f"{template_name}{ext}"
        if template_path.exists():
            content = template_path.read_text()
            return content.format(
                project_name=project_name,
                created=datetime.now().strftime("%Y-%m-%d"),
            )

    raise FileNotFoundError(f"Template not found: {template_name}")


def get_prompt_content(prompt_name: str) -> str:
    """Load a prompt template."""
    from jeff.prompts import PROMPTS_DIR

    prompt_path = PROMPTS_DIR / f"{prompt_name}.md"
    if prompt_path.exists():
        return prompt_path.read_text()
    raise FileNotFoundError(f"Prompt not found: {prompt_name}")


@click.command()
@click.option("--name", "-n", "project_name", help="Project name (defaults to directory name)")
def init(project_name: str):
    """Initialize a new jeff project in the current directory.

    Creates a .jeff/ directory with templates for story mapping,
    opportunity solution trees, and hypothesis tracking.
    """
    # Check if already initialized
    existing = find_jeff_root()
    if existing and existing == Path.cwd():
        raise click.ClickException(f"Already a jeff project: {existing}")

    # Determine project name
    if not project_name:
        project_name = Path.cwd().name

    jeff_dir = Path.cwd() / JEFF_DIR

    click.echo(f"Initializing jeff project: {project_name}")

    # Create directories
    jeff_dir.mkdir(exist_ok=True)
    for subdir in DIRECTORIES:
        (jeff_dir / subdir).mkdir(exist_ok=True)

    # Create config
    config_content = get_template_content("config", project_name)
    (jeff_dir / "config.yaml").write_text(config_content)

    # Create artifact files
    for artifact in ARTIFACT_FILES:
        name = artifact.replace(".md", "")
        content = get_template_content(name, project_name)
        (jeff_dir / artifact).write_text(content)

    # Create research files
    for research_file in RESEARCH_FILES:
        name = research_file.replace(".md", "")
        content = get_template_content(name, project_name)
        (jeff_dir / "research" / research_file).write_text(content)

    # Copy prompt files
    for prompt_file in PROMPT_FILES:
        name = prompt_file.replace(".md", "")
        content = get_prompt_content(name)
        (jeff_dir / "prompts" / prompt_file).write_text(content)

    click.echo(f"Created .jeff/ with project structure")
    click.echo("")
    click.echo("Next steps:")
    click.echo("  jeff map          # Get prompt for creating your story map")
    click.echo("  jeff opportunity  # Get prompt for opportunity solution tree")
    click.echo("  jeff hypothesis   # Get prompt for hypothesis tracking")
