"""Template files for jeff artifacts."""

from pathlib import Path


TEMPLATES_DIR = Path(__file__).parent


def get_template(name: str) -> str:
    """Load a template file by name."""
    template_path = TEMPLATES_DIR / f"{name}.md"
    if template_path.exists():
        return template_path.read_text()
    raise FileNotFoundError(f"Template not found: {name}")
