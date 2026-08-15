---
name: rate-watch
description: >-
  Fetches the current USD to PKR exchange rate from a free public API and
  reports it in plain English, along with how much it has moved since the
  last check (if a previous reading is available). Use this whenever asked
  about the current exchange rate, or to watch the rate over time.
---

# Rate Watch

You watch the USD → PKR exchange rate. Never guess a number. Always run the
script and report exactly what it prints.

## How to run it

```bash
python3 .claude/skills/rate-watch/scripts/rate.py
```

The script prints the current rate, the timestamp, and — if a previous
reading exists in `last-rate.txt` — how much the rate has moved since then.
It also updates `last-rate.txt` with the new reading, so the next run can
compare again.

## What to report

- Always state the rate plainly: "1 USD = X PKR as of [time]."
- If a previous reading exists, mention the direction and size of the move
  ("up 0.3 from last check" or "essentially unchanged").
- If the script fails (no internet, API down), say so plainly. Do not
  invent a plausible-sounding number. A failed check is worth reporting
  honestly — a wrong number is not.

## Rules

- Never fabricate a rate. If the script does not run successfully, there is
  no rate to report.
- Keep each report to one or two short sentences. This is a watch, not an
  essay.
