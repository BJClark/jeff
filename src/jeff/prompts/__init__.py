"""Prompt templates for jeff workflows."""

from pathlib import Path


PROMPTS_DIR = Path(__file__).parent


def get_prompt(name: str) -> str:
    """Load a prompt file by name."""
    prompt_path = PROMPTS_DIR / f"{name}.md"
    if prompt_path.exists():
        return prompt_path.read_text()
    raise FileNotFoundError(f"Prompt not found: {name}")
