#!/usr/bin/env bash
set -euo pipefail

# jeff installer — copies skill files into Claude Code or Cursor.
# No Python dependency required.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMMANDS_SRC="$SCRIPT_DIR/commands"
SKILLS_SRC="$SCRIPT_DIR/skills"

JEFF_COMMANDS=(jeff-init jeff-map jeff-opportunity jeff-hypothesis jeff-research jeff-bdd jeff-issues jeff-help)
JEFF_SKILLS=(jeff-init jeff-map jeff-opportunity jeff-hypothesis jeff-research jeff-bdd jeff-issues jeff-help)

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
  --global    copies wrappers to ~/.claude/commands/ and skills to ~/.claude/skills/
  --local     copies wrappers to ./.claude/commands/ and skills to ./.claude/skills/

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
  local claude_root="$1"
  local dry_run="$2"
  local commands_dst="$claude_root/commands"
  local skills_dst="$claude_root/skills"

  echo "Installing jeff for Claude Code → $claude_root"

  if [ ! -d "$COMMANDS_SRC" ]; then
    error "commands/ not found at $COMMANDS_SRC"
  fi
  if [ ! -d "$SKILLS_SRC" ]; then
    error "skills/ not found at $SKILLS_SRC"
  fi

  if [[ "$dry_run" == "true" ]]; then
    echo "  (dry-run) Would create: $commands_dst"
    for name in "${JEFF_COMMANDS[@]}"; do
      if [ -f "$COMMANDS_SRC/$name.md" ]; then
        echo "  (dry-run) Would copy: commands/$name.md → $commands_dst/$name.md"
      fi
    done
    echo "  (dry-run) Would create: $skills_dst"
    for name in "${JEFF_SKILLS[@]}"; do
      if [ -d "$SKILLS_SRC/$name" ]; then
        echo "  (dry-run) Would copy: skills/$name/ → $skills_dst/$name/"
      fi
    done
    return
  fi

  mkdir -p "$commands_dst"
  mkdir -p "$skills_dst"

  # Copy command wrappers
  local cmd_count=0
  for name in "${JEFF_COMMANDS[@]}"; do
    local src="$COMMANDS_SRC/$name.md"
    [ -f "$src" ] || { warn "missing commands/$name.md — skipped"; continue; }
    local dst="$commands_dst/$name.md"
    # Back up existing file if present and different
    if [ -f "$dst" ] && ! diff -q "$src" "$dst" >/dev/null 2>&1; then
      cp "$dst" "$dst.bak"
    fi
    cp "$src" "$dst"
    cmd_count=$((cmd_count + 1))
  done
  info "Installed $cmd_count command wrappers → $commands_dst"

  # Copy skill folders (SKILL.md + references/ + examples/ + templates/)
  local skill_count=0
  for name in "${JEFF_SKILLS[@]}"; do
    local src="$SKILLS_SRC/$name"
    [ -d "$src" ] || { warn "missing skills/$name/ — skipped"; continue; }
    local dst="$skills_dst/$name"
    # Back up existing folder if present and different
    if [ -d "$dst" ] && ! diff -rq "$src" "$dst" >/dev/null 2>&1; then
      rm -rf "$dst.bak"
      cp -R "$dst" "$dst.bak"
    fi
    rm -rf "$dst"
    cp -R "$src" "$dst"
    skill_count=$((skill_count + 1))
  done
  info "Installed $skill_count skill folders → $skills_dst"
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
  local claude_root="$1"
  local dry_run="$2"
  local commands_dst="$claude_root/commands"
  local skills_dst="$claude_root/skills"

  echo "Uninstalling jeff from Claude Code ← $claude_root"

  if [ ! -d "$claude_root" ]; then
    warn "Nothing to uninstall — $claude_root does not exist"
    return
  fi

  # Remove command wrappers — only the ones we own
  local cmd_count=0
  for name in "${JEFF_COMMANDS[@]}"; do
    local f="$commands_dst/$name.md"
    [ -f "$f" ] || continue
    if [[ "$dry_run" == "true" ]]; then
      echo "  (dry-run) Would remove: $f"
    else
      rm "$f"
      [ -f "$f.bak" ] && rm "$f.bak"
    fi
    cmd_count=$((cmd_count + 1))
  done

  # Remove skill folders — only the ones we own
  local skill_count=0
  for name in "${JEFF_SKILLS[@]}"; do
    local d="$skills_dst/$name"
    [ -d "$d" ] || continue
    if [[ "$dry_run" == "true" ]]; then
      echo "  (dry-run) Would remove: $d/"
    else
      rm -rf "$d"
      [ -d "$d.bak" ] && rm -rf "$d.bak"
    fi
    skill_count=$((skill_count + 1))
  done

  if [ "$cmd_count" -eq 0 ] && [ "$skill_count" -eq 0 ]; then
    warn "No jeff files found under $claude_root"
  else
    info "Removed $cmd_count command wrappers and $skill_count skill folders"
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
    if [ ! -d "$HOME/.claude" ]; then
      error "~/.claude/ does not exist. Install Claude Code first: https://docs.anthropic.com/en/docs/claude-code"
    fi
    echo "$HOME/.claude"
  else
    echo ".claude"
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
