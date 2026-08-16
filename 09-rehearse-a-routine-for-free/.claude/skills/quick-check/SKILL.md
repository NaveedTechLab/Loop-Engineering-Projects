---
name: quick-check
description: >-
  Runs a trivial timestamped check, used for rehearsing routines before
  trusting them to run on a real schedule. Use when asked to run the
  quick check.
---

# Quick Check

Run the script and report exactly what it prints. This task is
deliberately trivial — the point is proving a schedule actually fires,
not the content of the check itself.

```bash
python3 .claude/skills/quick-check/scripts/quick_check.py
```

Always report the timestamp it prints. That's what proves the run was
real and just happened.
