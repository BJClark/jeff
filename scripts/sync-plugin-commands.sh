#!/bin/bash
# Regenerate symlinks in commands/ from src/jeff/skills/

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SKILLS_DIR="$PROJECT_ROOT/src/jeff/skills"
COMMANDS_DIR="$PROJECT_ROOT/commands"

# Create commands directory if needed
mkdir -p "$COMMANDS_DIR"

# Remove existing symlinks
find "$COMMANDS_DIR" -type l -delete

# Create new symlinks (strip jeff- prefix for plugin namespacing)
for skill in "$SKILLS_DIR"/jeff-*.md; do
    if [ -f "$skill" ]; then
        src_name=$(basename "$skill")
        cmd_name="${src_name#jeff-}"
        ln -s "../src/jeff/skills/$src_name" "$COMMANDS_DIR/$cmd_name"
        echo "Linked: $cmd_name -> $src_name"
    fi
done

echo "Done. $(ls -1 "$COMMANDS_DIR" | wc -l | tr -d ' ') commands linked."
