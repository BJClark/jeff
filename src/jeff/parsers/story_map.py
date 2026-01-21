"""Parser for STORY_MAP.md files."""

import re
from dataclasses import dataclass


@dataclass
class Story:
    """A story from the story map."""
    activity: str
    title: str
    section: str  # "skeleton", "release1", "future"


def parse_table_row(row: str) -> list[str]:
    """Parse a markdown table row into cells."""
    cells = row.split("|")
    # Remove empty first/last from leading/trailing pipes
    cells = [c.strip() for c in cells if c.strip()]
    return cells


def parse_story_map(content: str) -> list[Story]:
    """Extract stories from a STORY_MAP.md file."""
    stories = []
    lines = content.split("\n")

    current_section = None
    backbone_activities = []
    in_table = False
    table_rows = []

    for line in lines:
        line_stripped = line.strip()

        # Track sections
        if line_stripped.startswith("## Backbone"):
            current_section = "backbone"
            in_table = False
            table_rows = []
        elif line_stripped.startswith("## Walking Skeleton"):
            current_section = "skeleton"
            in_table = False
            table_rows = []
        elif line_stripped.startswith("### Release 1"):
            current_section = "release1"
            in_table = False
            table_rows = []
        elif line_stripped.startswith("### Future"):
            current_section = "future"
            in_table = False
            table_rows = []
        elif line_stripped.startswith("## ") or line_stripped.startswith("# "):
            current_section = None
            in_table = False
            table_rows = []

        # Parse tables
        if line_stripped.startswith("|") and current_section:
            if "---" in line_stripped:
                # This is the separator row, next rows are data
                in_table = True
                continue

            if in_table or current_section == "backbone":
                cells = parse_table_row(line_stripped)

                if current_section == "backbone":
                    # First row after header is activities
                    if cells and not any(c.startswith("_") for c in cells):
                        backbone_activities = cells
                    elif cells and any(c.startswith("_") for c in cells):
                        # This is the description row
                        backbone_activities = [
                            f"Activity {i+1}"
                            for i in range(len(cells))
                        ]
                elif current_section == "skeleton":
                    for i, cell in enumerate(cells):
                        if cell and not cell.startswith("_"):
                            activity = backbone_activities[i] if i < len(backbone_activities) else f"Activity {i+1}"
                            stories.append(Story(
                                activity=activity,
                                title=cell,
                                section="skeleton"
                            ))
                elif current_section in ("release1", "future"):
                    for i, cell in enumerate(cells):
                        if cell and not cell.startswith("_"):
                            activity = backbone_activities[i] if i < len(backbone_activities) else f"Activity {i+1}"
                            stories.append(Story(
                                activity=activity,
                                title=cell,
                                section=current_section
                            ))

    return stories
