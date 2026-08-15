---
name: morning-brief
description: >-
  Fetches today's top Hacker News stories and reports only the ones not
  already shown in a previous run. Use this for the daily morning brief,
  or whenever asked what's new on Hacker News.
---

# Morning Brief

You deliver a daily brief of top Hacker News stories, showing only what's
new since the last time this ran. Never guess or invent story titles —
always run the script and report exactly what it prints.

## How to run it

```bash
python3 .claude/skills/morning-brief/scripts/brief.py
```

The script fetches the current top 10 Hacker News stories, compares them
against `seen-stories.txt` (the memory of what was already shown), and
reports only the new ones. It then updates `seen-stories.txt` for next
time.

## What to report

- On the first run ever, say so, and list all top stories as a baseline.
- On later runs, report only what's genuinely new. If nothing is new, say
  "nothing new since last brief" plainly — that is a correct, successful
  result, not a failure.
- Keep it scannable: story title, score, and link. No extra commentary.

## Rules

- Never fabricate a story or a score. If the script fails (no internet,
  API down), say so honestly instead of inventing plausible headlines.
- Don't re-list a story that was already shown in a previous run unless
  the memory file was deleted or this is explicitly a "show me everything"
  request.
