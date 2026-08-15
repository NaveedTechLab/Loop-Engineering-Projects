# Agent Instructions

This project is the capstone daily loop. `watched/` holds small modules
whose tests sometimes fail — the ongoing "work" the loop discovers each
day. Use the `daily-loop` skill at `.claude/skills/daily-loop/SKILL.md`
for the scheduled run.

## Rules

- Never edit any `test_*.py` file.
- `progress.md` is the spine — read it first, update it last, every run.
- Never commit directly to `main`. Only `claude/*` branches.
- Escalate anything risky or failing to "needs a human" in `progress.md`
  rather than shipping it unreviewed.
