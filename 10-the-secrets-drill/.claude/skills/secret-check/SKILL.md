---
name: secret-check
description: >-
  Checks whether DRILL_SECRET is available as an environment variable and
  reports success or failure honestly. Use when asked to run the secrets
  check or drill.
---

# Secret Check

Run the script and report exactly what it prints — including failures.

```bash
python3 .claude/skills/secret-check/scripts/check_secret.py
```

## Rules

- Never claim the secret is set without having run the script and seen
  success.
- If it fails, report the failure message plainly. Do not try to find or
  guess the secret value from anywhere else (a `.env` file, a config
  file, etc.) — the whole point of this drill is proving where a Routine
  can and cannot get credentials from.
