#!/usr/bin/env bash
set -euo pipefail

# jeff installer — copies skill files into Claude Code or Cursor.
# No Python dependency required.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/src/jeff/skills"
TEMPLATES_DIR="$SKILLS_DIR/templates"

# ── Helpers ──────────────────────────────────────────────────────────────────

usage() {
  cat <<'EOF'
Usage:
  ./install.sh --claude [--global|--local]    Install skills for Claude Code
  ./install.sh --cursor [--global|--local]    Install for Cursor
  ./install.sh --all    [--global|--local]    Install for all supported tools
  ./install.sh --uninstall --claude [--global|--local]
  ./install.sh --uninstall --cursor [--global|--local]

Options:
  --global    System-wide install (default)
  --local     Install into the current project only
  --dry-run   Show what would be done without doing it
  --help      Show this help

Claude Code:
  --global    copies skills to ~/.claude/commands/
  --local     copies skills to ./.claude/commands/

Cursor:
  --global    copies AGENTS.md to ~/.cursor/rules/jeff.mdc
  --local     copies AGENTS.md to ./.cursor/rules/jeff.mdc
EOF
  exit 0
}

info()  { echo "  ✓ $*"; }
warn()  { echo "  ! $*"; }
error() { echo "  ✗ $*" >&2; exit 1; }

# ── Core functions ───────────────────────────────────────────────────────────

install_claude() {
  local target_dir="$1"
  local dry_run="$2"

  echo "Installing jeff skills for Claude Code → $target_dir"

  if [[ "$dry_run" == "true" ]]; then
    echo "  (dry-run) Would create: $target_dir"
    for f in "$SKILLS_DIR"/jeff-*.md; do
      echo "  (dry-run) Would copy: $(basename "$f")"
    done
    return
  fi

  mkdir -p "$target_dir"

  local count=0
  for f in "$SKILLS_DIR"/jeff-*.md; do
    [ -f "$f" ] || continue
    local name
    name=$(basename "$f")
    # Back up existing file if present and different
    if [ -f "$target_dir/$name" ]; then
      if ! diff -q "$f" "$target_dir/$name" >/dev/null 2>&1; then
        cp "$target_dir/$name" "$target_dir/$name.bak"
      fi
    fi
    cp "$f" "$target_dir/$name"
    count=$((count + 1))
  done

  info "Installed $count skill files"
}

install_cursor() {
  local target_dir="$1"
  local dry_run="$2"
  local agents_src="$SCRIPT_DIR/AGENTS.md"

  echo "Installing jeff context for Cursor → $target_dir"

  if [ ! -f "$agents_src" ]; then
    error "AGENTS.md not found at $agents_src"
  fi

  if [[ "$dry_run" == "true" ]]; then
    echo "  (dry-run) Would create: $target_dir/jeff.mdc"
    return
  fi

  mkdir -p "$target_dir"

  # Write as an .mdc rule file with frontmatter
  {
    echo "---"
    echo "description: Jeff product discovery skills — story mapping, OST, hypotheses, research"
    echo "globs:"
    echo "alwaysApply: true"
    echo "---"
    echo ""
    cat "$agents_src"
  } > "$target_dir/jeff.mdc"

  info "Created $target_dir/jeff.mdc"
}

uninstall_claude() {
  local target_dir="$1"
  local dry_run="$2"

  echo "Uninstalling jeff skills from Claude Code ← $target_dir"

  if [ ! -d "$target_dir" ]; then
    warn "Nothing to uninstall — $target_dir does not exist"
    return
  fi

  local count=0
  for f in "$target_dir"/jeff-*.md; do
    [ -f "$f" ] || continue
    if [[ "$dry_run" == "true" ]]; then
      echo "  (dry-run) Would remove: $(basename "$f")"
    else
      rm "$f"
      # Also remove backup if present
      [ -f "$f.bak" ] && rm "$f.bak"
    fi
    count=$((count + 1))
  done

  if [ "$count" -eq 0 ]; then
    warn "No jeff skill files found in $target_dir"
  else
    info "Removed $count skill files"
  fi
}

uninstall_cursor() {
  local target_dir="$1"
  local dry_run="$2"

  echo "Uninstalling jeff context from Cursor ← $target_dir"

  if [ -f "$target_dir/jeff.mdc" ]; then
    if [[ "$dry_run" == "true" ]]; then
      echo "  (dry-run) Would remove: $target_dir/jeff.mdc"
    else
      rm "$target_dir/jeff.mdc"
      info "Removed $target_dir/jeff.mdc"
    fi
  else
    warn "No jeff.mdc found in $target_dir"
  fi
}

# ── Argument parsing ────────────────────────────────────────────────────────

TOOL=""
SCOPE="global"
UNINSTALL=false
DRY_RUN=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --claude)     TOOL="claude"; shift ;;
    --cursor)     TOOL="cursor"; shift ;;
    --all)        TOOL="all"; shift ;;
    --global)     SCOPE="global"; shift ;;
    --local)      SCOPE="local"; shift ;;
    --uninstall)  UNINSTALL=true; shift ;;
    --dry-run)    DRY_RUN=true; shift ;;
    --help|-h)    usage ;;
    *)            error "Unknown option: $1. Run with --help for usage." ;;
  esac
done

if [ -z "$TOOL" ]; then
  usage
fi

# ── Resolve target directories ──────────────────────────────────────────────

resolve_claude_dir() {
  if [[ "$SCOPE" == "global" ]]; then
    local dir="$HOME/.claude/commands"
    if [ ! -d "$HOME/.claude" ]; then
      error "~/.claude/ does not exist. Install Claude Code first: https://docs.anthropic.com/en/docs/claude-code"
    fi
    echo "$dir"
  else
    echo ".claude/commands"
  fi
}

resolve_cursor_dir() {
  if [[ "$SCOPE" == "global" ]]; then
    local dir="$HOME/.cursor/rules"
    if [ ! -d "$HOME/.cursor" ]; then
      error "~/.cursor/ does not exist. Install Cursor first: https://cursor.com"
    fi
    echo "$dir"
  else
    echo ".cursor/rules"
  fi
}

# ── Execute ─────────────────────────────────────────────────────────────────

echo ""

if [[ "$UNINSTALL" == "true" ]]; then
  case "$TOOL" in
    claude)
      uninstall_claude "$(resolve_claude_dir)" "$DRY_RUN"
      ;;
    cursor)
      uninstall_cursor "$(resolve_cursor_dir)" "$DRY_RUN"
      ;;
    all)
      uninstall_claude "$(resolve_claude_dir)" "$DRY_RUN"
      uninstall_cursor "$(resolve_cursor_dir)" "$DRY_RUN"
      ;;
  esac
else
  case "$TOOL" in
    claude)
      install_claude "$(resolve_claude_dir)" "$DRY_RUN"
      ;;
    cursor)
      install_cursor "$(resolve_cursor_dir)" "$DRY_RUN"
      ;;
    all)
      install_claude "$(resolve_claude_dir)" "$DRY_RUN"
      install_cursor "$(resolve_cursor_dir)" "$DRY_RUN"
      ;;
  esac
fi

echo ""
echo "Done!"
