---
name: execute-approved
description: >-
  Executes a proposal from proposal.md ONLY if it's still PENDING
  APPROVAL, and does nothing if already executed. Use for the "Routine B"
  executor step of the two-routine gate — this should only ever be
  triggered by an explicit human approval action (an API call), never on
  a schedule.
---

# Execute Approved

Run the script and report exactly what happened.

```bash
python3 .claude/skills/execute-approved/scripts/execute_approved.py
```

## Rules

- This skill should only run when explicitly fired by a human's approval
  action (in the real setup, an authenticated API call) — never attach
  this to a schedule or any trigger a human didn't directly cause.
- If the proposal is already marked EXECUTED, do nothing and report that
  plainly — never execute twice.
- If there's no proposal, or its status isn't recognizable, refuse to act
  and say so.
