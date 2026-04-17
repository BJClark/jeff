#!/usr/bin/env bash
set -euo pipefail

# jeff installer for Cursor.
#
# For Claude Code, use the plugin flow instead:
#   claude plugin marketplace add BJClark/jeff
#   claude plugin install jeff@jeff
# or, to try without installing:
#   claude --plugin-dir /path/to/this/repo

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ── Helpers ──────────────────────────────────────────────────────────────────

usage() {
  cat <<'EOF'
Usage:
  ./install.sh --cursor [--global|--local]    Install jeff rules for Cursor
  ./install.sh --uninstall --cursor [--global|--local]

What it installs (into ~/.cursor/rules/ or ./.cursor/rules/):
  jeff.mdc            Always-on umbrella rule (command reference + workflow)
  jeff-<skill>.mdc    One on-demand rule per skill (init, map, opportunity,
                      hypothesis, research, bdd, issues, help). Each carries
                      its own description so Cursor loads it when relevant.

Options:
  --global    System-wide install (default) — ~/.cursor/rules/
  --local     Project-local install — ./.cursor/rules/
  --dry-run   Show what would be done without doing it
  --help      Show this help

Claude Code users: jeff is now distributed as a Claude Code plugin.
  claude plugin marketplace add BJClark/jeff
  claude plugin install jeff@jeff
See README.md for details.
EOF
  exit 0
}

info()  { echo "  ✓ $*"; }
warn()  { echo "  ! $*"; }
error() { echo "  ✗ $*" >&2; exit 1; }

# Extract the frontmatter `description:` value from a SKILL.md file.
# Reads the first frontmatter block (between the first pair of --- lines).
extract_description() {
  local skill_file="$1"
  awk '
    /^---$/ { c++; if (c == 2) exit; next }
    c == 1 && /^description:/ {
      sub(/^description:[[:space:]]*/, "")
      print
      exit
    }
  ' "$skill_file"
}

# Extract the body of a SKILL.md file (everything after the closing --- of
# frontmatter).
extract_body() {
  local skill_file="$1"
  awk '
    /^---$/ { c++; next }
    c >= 2 { print }
  ' "$skill_file"
}

# ── Core functions ───────────────────────────────────────────────────────────

install_cursor() {
  local target_dir="$1"
  local dry_run="$2"
  local agents_src="$SCRIPT_DIR/AGENTS.md"
  local skills_dir="$SCRIPT_DIR/skills"

  echo "Installing jeff rules for Cursor → $target_dir"

  if [ ! -f "$agents_src" ]; then
    error "AGENTS.md not found at $agents_src"
  fi
  if [ ! -d "$skills_dir" ]; then
    error "skills/ directory not found at $skills_dir"
  fi

  if [[ "$dry_run" == "true" ]]; then
    echo "  (dry-run) Would create: $target_dir/jeff.mdc (umbrella, alwaysApply: true)"
    for skill_dir in "$skills_dir"/*/; do
      local skill_name
      skill_name=$(basename "$skill_dir")
      echo "  (dry-run) Would create: $target_dir/jeff-$skill_name.mdc (on-demand)"
    done
    return
  fi

  mkdir -p "$target_dir"

  # Umbrella rule: always-on overview from AGENTS.md.
  {
    echo "---"
    echo "description: Jeff product discovery skills — story mapping, OST, hypotheses, research. Command reference and workflow overview for /jeff:* slash commands."
    echo "globs:"
    echo "alwaysApply: true"
    echo "---"
    echo ""
    cat "$agents_src"
  } > "$target_dir/jeff.mdc"
  info "Created $target_dir/jeff.mdc (umbrella)"

  # Per-skill rules: on-demand, loaded when their description matches context.
  for skill_dir in "$skills_dir"/*/; do
    local skill_name skill_file desc
    skill_name=$(basename "$skill_dir")
    skill_file="$skill_dir/SKILL.md"

    if [ ! -f "$skill_file" ]; then
      warn "Skipping $skill_name — no SKILL.md found"
      continue
    fi

    desc=$(extract_description "$skill_file")
    if [ -z "$desc" ]; then
      warn "Skipping $skill_name — no description in frontmatter"
      continue
    fi

    {
      echo "---"
      echo "description: $desc"
      echo "globs:"
      echo "alwaysApply: false"
      echo "---"
      echo ""
      extract_body "$skill_file"
    } > "$target_dir/jeff-$skill_name.mdc"
    info "Created $target_dir/jeff-$skill_name.mdc"
  done
}

uninstall_cursor() {
  local target_dir="$1"
  local dry_run="$2"

  echo "Uninstalling jeff rules from Cursor ← $target_dir"

  if [ ! -d "$target_dir" ]; then
    warn "No rules directory at $target_dir"
    return
  fi

  local removed=0
  shopt -s nullglob
  for f in "$target_dir"/jeff.mdc "$target_dir"/jeff-*.mdc; do
    if [[ "$dry_run" == "true" ]]; then
      echo "  (dry-run) Would remove: $f"
    else
      rm "$f"
      info "Removed $f"
    fi
    removed=$((removed + 1))
  done
  shopt -u nullglob

  if [[ "$removed" -eq 0 ]]; then
    warn "No jeff rules found in $target_dir"
  fi
}

# ── Argument parsing ────────────────────────────────────────────────────────

TOOL=""
SCOPE="global"
UNINSTALL=false
DRY_RUN=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --cursor)     TOOL="cursor"; shift ;;
    --global)     SCOPE="global"; shift ;;
    --local)      SCOPE="local"; shift ;;
    --uninstall)  UNINSTALL=true; shift ;;
    --dry-run)    DRY_RUN=true; shift ;;
    --help|-h)    usage ;;
    --claude|--all)
      error "The --claude install path is gone. Use the Claude Code plugin flow instead:
    claude plugin marketplace add BJClark/jeff
    claude plugin install jeff@jeff
  See README.md for details." ;;
    *)            error "Unknown option: $1. Run with --help for usage." ;;
  esac
done

if [ -z "$TOOL" ]; then
  usage
fi

# ── Resolve target directories ──────────────────────────────────────────────

resolve_cursor_dir() {
  if [[ "$SCOPE" == "global" ]]; then
    if [ ! -d "$HOME/.cursor" ]; then
      error "~/.cursor/ does not exist. Install Cursor first: https://cursor.com"
    fi
    echo "$HOME/.cursor/rules"
  else
    echo ".cursor/rules"
  fi
}

# ── Execute ─────────────────────────────────────────────────────────────────

echo ""

if [[ "$UNINSTALL" == "true" ]]; then
  uninstall_cursor "$(resolve_cursor_dir)" "$DRY_RUN"
else
  install_cursor "$(resolve_cursor_dir)" "$DRY_RUN"
fi

echo ""
echo "Done!"
