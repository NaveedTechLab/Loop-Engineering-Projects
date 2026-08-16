# Agent Instructions

This project's daily loop watches a set of modules and fixes failing
ones. See `run-logs/` for the history of past runs.

## Rules

- Never edit any `test_*.py` file.
- After fixing a failing module, run the full test suite before opening
  a PR — not just the changed module's own test file. A fix can pass
  its own module's tests while silently breaking a different module
  that depends on shared code.
- `progress.md` is the spine — read it first, update it last.
- Never commit directly to `main`. Only `claude/*` branches.
- Escalate anything risky to "needs a human" rather than shipping it
  unreviewed.
