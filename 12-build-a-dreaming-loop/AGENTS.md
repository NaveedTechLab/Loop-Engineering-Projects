# Agent Instructions

This project's daily loop watches a set of modules and fixes failing
ones. See `run-logs/` for the history of past runs.

## Rules

- Never edit any `test_*.py` file.
- `progress.md` is the spine — read it first, update it last.
- Never commit directly to `main`. Only `claude/*` branches.
- Escalate anything risky to "needs a human" rather than shipping it
  unreviewed.
