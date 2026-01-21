"""Configuration management for jeff projects."""

import os
from pathlib import Path
from typing import Optional

import yaml


JEFF_DIR = ".jeff"
CONFIG_FILE = "config.yaml"


def find_jeff_root(start_path: Optional[Path] = None) -> Optional[Path]:
    """Find the nearest .jeff directory by walking up from start_path."""
    if start_path is None:
        start_path = Path.cwd()

    current = start_path.resolve()
    while current != current.parent:
        jeff_path = current / JEFF_DIR
        if jeff_path.is_dir():
            return current
        current = current.parent

    # Check root
    jeff_path = current / JEFF_DIR
    if jeff_path.is_dir():
        return current

    return None


def get_jeff_dir(start_path: Optional[Path] = None) -> Optional[Path]:
    """Get the .jeff directory path."""
    root = find_jeff_root(start_path)
    if root:
        return root / JEFF_DIR
    return None


def load_config(jeff_dir: Path) -> dict:
    """Load configuration from config.yaml."""
    config_path = jeff_dir / CONFIG_FILE
    if config_path.exists():
        with open(config_path, "r") as f:
            return yaml.safe_load(f) or {}
    return {}


def save_config(jeff_dir: Path, config: dict) -> None:
    """Save configuration to config.yaml."""
    config_path = jeff_dir / CONFIG_FILE
    with open(config_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)


def require_jeff_dir() -> Path:
    """Get the .jeff directory or exit with error."""
    jeff_dir = get_jeff_dir()
    if jeff_dir is None:
        raise click.ClickException(
            "Not in a jeff project. Run 'jeff init' to create one."
        )
    return jeff_dir


# Import click here to avoid circular imports
import click
