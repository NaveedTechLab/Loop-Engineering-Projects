# Project 6 — The Doorbell Loop (TODO Comment Watcher)

**Loop Engineering, Concept 7 — event-driven heartbeat.**

This is the same shape as the official Doorbell project — zero cost until
a pull request opens, then a fresh, rented GitHub Actions machine reacts —
but pointed at a different, genuinely useful task: **flagging new TODO and
FIXME comments a PR introduces**, so technical debt doesn't slip in
silently.

## Why this task fits the doorbell shape well

A code reviewer catches a stray `# TODO: fix this later` maybe half the
time, when they're paying close attention. A doorbell never misses one,
and it costs nothing on the days nobody opens a PR.

## Setup (same mechanics as the official Doorbell — you've done this before)

**1. This needs its own repo, or a subfolder in one that already has
`CLAUDE_CODE_OAUTH_TOKEN` set up.** The workflow file must live at
`.github/workflows/` in the repo root — GitHub only looks there.

If reusing your `Loop-Engineering-Projects` repo, this project's own
`.github/workflows/todo-doorbell.yml` needs to be merged into (or placed
alongside) the repo's single `.github/workflows/` folder at the root —
GitHub only reads one `.github` per repo.

**2. Confirm your token secret is still set** (you already did this for
Project 4/Doorbell):
```bash
gh secret list --repo NaveedTechLab/Loop-Engineering-Projects
```
You should see `CLAUDE_CODE_OAUTH_TOKEN` in the list. If not:
```bash
claude setup-token
gh secret set CLAUDE_CODE_OAUTH_TOKEN --repo NaveedTechLab/Loop-Engineering-Projects
```

**3. Commit and push this project**, including the workflow file at the
repo root's `.github/workflows/`.

## Ring the doorbell

1. On GitHub, open `inventory.py` in this project's folder.
2. Click the pencil (Edit) icon.
3. Add a new comment somewhere, for example:
   ```python
   # TODO: add support for multiple warehouses
   ```
4. Choose **"Create a new branch for this commit and start a pull
   request"** → **Propose changes** → **Create pull request**.
5. Wait about a minute. A comment should appear listing exactly the TODO
   you added — nothing else.

## What to notice

- **It costs nothing until you open a PR.** No schedule, no polling.
- **It only flags NEW TODOs**, not any that already existed — this is a
  harder task than the original Doorbell's bug-finder, because the
  workflow must diff against the base branch, not just read the file.
- **Push a second commit to the same PR** with a second new TODO. A fresh
  comment should appear about just the new one — proof that each event
  starts a brand-new session with no memory of the last one, and the only
  way it "knows" what's already been flagged is by reading the PR's own
  diff and comment history from the repo, not from memory.

## What ships in this folder

| File | Job |
|---|---|
| `.github/workflows/todo-doorbell.yml` | The event-driven trigger — fires on PR open/update |
| `inventory.py` | A sample file to edit when testing |

## The interview-ready idea

> "Unlike a scheduled loop, this one has zero cost and does nothing at all
> until a specific event — a pull request — happens. And because every
> event spins up a brand-new machine with no memory, the loop has to prove
> it can tell 'new' from 'old' by reading the repo's actual diff, not by
> remembering a previous run."
