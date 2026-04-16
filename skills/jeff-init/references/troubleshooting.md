# jeff-init — Troubleshooting

## `.jeff/` already exists

Ask before overwriting. If the user confirms a reinit, preserve every file whose content differs from the template (those are their edits) and only rewrite the templates the user hasn't touched.

## Permission denied

The user can't write to the current directory. Suggest `chmod`, changing directories, or running from a location they own. Don't silently retry with `sudo` — that changes file ownership in ways users don't expect.

## Running from an unusual location

If the current directory is `/`, the user's `$HOME`, `/tmp`, or obviously not a project root, warn before scaffolding. Ask: "Do you want `.jeff/` created here, or did you mean to `cd` into a project first?"

## Missing `templates/` folder inside the skill

If the skill's bundled `templates/` directory is absent (install corruption), stop and tell the user to reinstall jeff. Do not generate templates inline from this skill — they belong in `templates/` so `jeff-init` and the docs stay in sync.

## Project name has unusual characters

Slashes, colons, and quotes in the name break YAML. Either escape them or ask the user for a simpler name. Warn first, don't silently mangle.

## Partial write

If the skill crashes mid-scaffold, `.jeff/` will be incomplete. On the next run, `Read .jeff/config.yaml`: if it's missing, treat the directory as uninitialized and proceed with a fresh scaffold (overwriting whatever partial files exist).
