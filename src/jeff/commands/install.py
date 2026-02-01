"""Install jeff skills into AI coding tools."""

import json
import os
import shutil
from pathlib import Path

import click
import yaml

from jeff.skills import SKILLS_DIR

# Tool configurations
TOOLS = {
    "claude": {
        "name": "Claude Code",
        "global_dir": Path.home() / ".claude" / "commands",
        "local_dir": Path(".claude") / "commands",
        "supports_global": True,
        "flatten": True,
    },
    "opencode": {
        "name": "Opencode",
        "global_dir": Path.home() / ".config" / "opencode" / "command",
        "local_dir": Path(".opencode") / "command",
        "supports_global": True,
        "flatten": True,  # jeff-map.md instead of jeff/jeff-map.md
    },
    "cursor": {
        "name": "Cursor",
        "local_dir": Path(".cursorrules"),
        "supports_global": False,
    },
    "zed": {
        "name": "Zed",
        "local_dir": Path(".zed") / "settings.json",
        "supports_global": False,
    },
    "conductor": {
        "name": "Conductor",
        "local_dir": Path("conductor.yaml"),
        "supports_global": False,
    },
}


def get_target_dir(tool: str, is_global: bool) -> Path:
    """Get the target directory for a tool."""
    config = TOOLS[tool]

    if is_global:
        if not config.get("supports_global"):
            raise click.ClickException(
                f"{config['name']} does not support global installation. "
                f"Use --local instead."
            )
        return config["global_dir"]

    return Path.cwd() / config["local_dir"]


def copy_skills(tool: str, target_dir: Path):
    """Copy skill files to target directory."""
    config = TOOLS[tool]

    # Create target directory
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy skill files
    count = 0
    for skill_file in SKILLS_DIR.glob("*.md"):
        dest = target_dir / skill_file.name
        shutil.copy2(skill_file, dest)
        count += 1

    return count


def install_cursor(target_path: Path):
    """Install for Cursor by copying AGENTS.md to .cursorrules."""
    agents_md = Path.cwd() / "AGENTS.md"

    if not agents_md.exists():
        raise click.ClickException(
            "AGENTS.md not found. Run 'jeff init' first or create AGENTS.md."
        )

    # Read AGENTS.md and append jeff skill info
    content = agents_md.read_text()

    # Add jeff commands section if not present
    if "## Jeff Commands" not in content:
        content += """

## Jeff Commands

Jeff is installed. Use these commands:
- `jeff map` - Create/update story map
- `jeff opportunity` - Create Opportunity Solution Tree
- `jeff hypothesis` - Track hypotheses
- `jeff research interview` - Capture interview notes
- `jeff research insight` - Extract insights
- `jeff issues` - Generate GitHub issues
- `jeff bdd` - Generate BDD tasks

Run `jeff --help` for more information.
"""

    target_path.write_text(content)


def install_zed(target_path: Path):
    """Install for Zed by updating .zed/settings.json."""
    target_path.parent.mkdir(parents=True, exist_ok=True)

    # Read existing settings or create new
    if target_path.exists():
        settings = json.loads(target_path.read_text())
    else:
        settings = {}

    # Add/update assistant config
    if "assistant" not in settings:
        settings["assistant"] = {}

    # Add AGENTS.md to context sources
    context_sources = settings["assistant"].get("context_sources", [])
    if "AGENTS.md" not in context_sources:
        context_sources.append("AGENTS.md")
        settings["assistant"]["context_sources"] = context_sources

    target_path.write_text(json.dumps(settings, indent=2) + "\n")


def install_conductor(target_path: Path):
    """Install for Conductor by creating/updating conductor.yaml."""
    # Read existing config or create new
    if target_path.exists():
        config = yaml.safe_load(target_path.read_text()) or {}
    else:
        config = {}

    # Add agents list if not present
    if "agents" not in config:
        config["agents"] = []

    # Check if jeff-assistant already exists
    jeff_agent = None
    for agent in config["agents"]:
        if agent.get("name") == "jeff-assistant":
            jeff_agent = agent
            break

    if jeff_agent is None:
        jeff_agent = {"name": "jeff-assistant"}
        config["agents"].append(jeff_agent)

    # Update jeff agent config
    jeff_agent["context"] = jeff_agent.get("context", [])
    if "AGENTS.md" not in jeff_agent["context"]:
        jeff_agent["context"].append("AGENTS.md")

    jeff_agent["tools"] = jeff_agent.get("tools", [])
    if "shell" not in jeff_agent["tools"]:
        jeff_agent["tools"].append("shell")

    target_path.write_text(yaml.dump(config, default_flow_style=False))


def remove_skills(tool: str, target_dir: Path):
    """Remove skill files from target directory."""
    config = TOOLS[tool]

    if not target_dir.exists():
        return 0

    count = 0

    if tool in ("cursor", "zed", "conductor"):
        # These are single files, just remove them
        if target_dir.is_file():
            target_dir.unlink()
            count = 1
    elif config.get("flatten"):
        # Opencode: remove jeff-*.md files from the command directory
        for f in target_dir.glob("jeff-*.md"):
            f.unlink()
            count += 1
    else:
        # Claude: remove the jeff/ directory
        if target_dir.exists() and target_dir.is_dir():
            shutil.rmtree(target_dir)
            count = len(list(SKILLS_DIR.glob("*.md")))

    return count


@click.command("install")
@click.option("--claude", "tool", flag_value="claude", help="Install for Claude Code")
@click.option("--opencode", "tool", flag_value="opencode", help="Install for Opencode")
@click.option("--cursor", "tool", flag_value="cursor", help="Install for Cursor")
@click.option("--zed", "tool", flag_value="zed", help="Install for Zed")
@click.option("--conductor", "tool", flag_value="conductor", help="Install for Conductor")
@click.option("--global", "is_global", is_flag=True, help="Install globally (all projects)")
@click.option("--local", "is_local", is_flag=True, help="Install locally (current project)")
def install(tool: str, is_global: bool, is_local: bool):
    """Install jeff skills for an AI coding tool.

    Examples:

    \b
      jeff install --claude --global    Install for Claude Code globally
      jeff install --claude --local     Install for Claude Code locally
      jeff install --cursor             Install for Cursor (local only)
      jeff install                      Interactive mode

    Supported tools:

    \b
      --claude      Claude Code (~/.claude/skills/jeff/)
      --opencode    Opencode (~/.config/opencode/command/)
      --cursor      Cursor (.cursorrules) - local only
      --zed         Zed (.zed/settings.json) - local only
      --conductor   Conductor (conductor.yaml) - local only
    """
    # Interactive mode if no tool specified
    if not tool:
        tool = _interactive_tool_select()

    # Validate scope
    if is_global and is_local:
        raise click.ClickException("Cannot specify both --global and --local")

    config = TOOLS[tool]

    # Determine scope
    if not is_global and not is_local:
        if config["supports_global"]:
            is_global = _interactive_scope_select(tool)
        else:
            is_local = True
            click.echo(f"{config['name']} only supports local installation.")

    # Check global support
    if is_global and not config["supports_global"]:
        raise click.ClickException(
            f"{config['name']} does not support global installation. "
            f"Use --local instead."
        )

    target_dir = get_target_dir(tool, is_global)
    scope_label = "globally" if is_global else "locally"

    click.echo(f"\nInstalling jeff for {config['name']} {scope_label}...")
    click.echo(f"Target: {target_dir}\n")

    # Install based on tool type
    if tool == "cursor":
        install_cursor(target_dir)
        click.echo(click.style("✓", fg="green") + " Created .cursorrules with jeff context")
    elif tool == "zed":
        install_zed(target_dir)
        click.echo(click.style("✓", fg="green") + " Updated .zed/settings.json")
    elif tool == "conductor":
        install_conductor(target_dir)
        click.echo(click.style("✓", fg="green") + " Updated conductor.yaml")
    else:
        count = copy_skills(tool, target_dir)
        click.echo(click.style("✓", fg="green") + f" Installed {count} skills")

    click.echo(f"\n{click.style('Done!', fg='green')} ", nl=False)

    if tool in ("claude", "opencode"):
        click.echo(f"Try {click.style('/jeff:help', fg='cyan')} in {config['name']}.")
    else:
        click.echo(f"Run {click.style('jeff --help', fg='cyan')} in {config['name']}.")


@click.command("uninstall")
@click.option("--claude", "tool", flag_value="claude", help="Uninstall from Claude Code")
@click.option("--opencode", "tool", flag_value="opencode", help="Uninstall from Opencode")
@click.option("--cursor", "tool", flag_value="cursor", help="Uninstall from Cursor")
@click.option("--zed", "tool", flag_value="zed", help="Uninstall from Zed")
@click.option("--conductor", "tool", flag_value="conductor", help="Uninstall from Conductor")
@click.option("--global", "is_global", is_flag=True, help="Uninstall globally")
@click.option("--local", "is_local", is_flag=True, help="Uninstall locally")
def uninstall(tool: str, is_global: bool, is_local: bool):
    """Uninstall jeff skills from an AI coding tool.

    Examples:

    \b
      jeff uninstall --claude --global    Uninstall from Claude Code globally
      jeff uninstall --cursor             Uninstall from Cursor
    """
    if not tool:
        raise click.ClickException("Please specify a tool (--claude, --opencode, etc.)")

    if is_global and is_local:
        raise click.ClickException("Cannot specify both --global and --local")

    config = TOOLS[tool]

    if not is_global and not is_local:
        if config["supports_global"]:
            raise click.ClickException("Please specify --global or --local")
        is_local = True

    if is_global and not config["supports_global"]:
        raise click.ClickException(f"{config['name']} only supports local installation.")

    target_dir = get_target_dir(tool, is_global)
    scope_label = "globally" if is_global else "locally"

    click.echo(f"\nUninstalling jeff from {config['name']} {scope_label}...")

    count = remove_skills(tool, target_dir)

    if count > 0:
        click.echo(click.style("✓", fg="green") + f" Removed {count} item(s)")
        click.echo(f"\n{click.style('Done!', fg='green')} Jeff has been uninstalled.")
    else:
        click.echo(click.style("!", fg="yellow") + " Nothing to uninstall.")


def _interactive_tool_select() -> str:
    """Interactively select a tool."""
    click.echo("\nWhich AI tool would you like to install jeff for?\n")
    click.echo("  1) Claude Code")
    click.echo("  2) Opencode")
    click.echo("  3) Cursor")
    click.echo("  4) Zed")
    click.echo("  5) Conductor")
    click.echo()

    choice = click.prompt("Choice", default="1")

    tools = ["claude", "opencode", "cursor", "zed", "conductor"]
    try:
        return tools[int(choice) - 1]
    except (ValueError, IndexError):
        raise click.ClickException("Invalid choice")


def _interactive_scope_select(tool: str) -> bool:
    """Interactively select scope (global/local)."""
    config = TOOLS[tool]

    click.echo(f"\nWhere would you like to install?\n")
    click.echo(f"  1) Global ({config['global_dir']})")
    click.echo(f"  2) Local  (./{config['local_dir']})")
    click.echo()

    choice = click.prompt("Choice", default="1")

    return choice == "1"
