# Project 8 — Your Own Daily Loop

**This is the capstone.** It combines everything from Projects 1–7 and
the official showcase projects into one loop, matching the course's
"minimum safe loop checklist" (Part 5) exactly.

| # | Checklist item | Where it lives here |
|---|---|---|
| 1 | Success condition | Each `watched/` module's own tests passing |
| 2 | Limit | "Never open more than 5 PRs in one run" (in the skill) |
| 3 | Isolated branch/worktree | Each fix on its own `claude/fix-<name>` branch |
| 4 | Read-only checker | The `reviewer` subagent |
| 5 | State file | `progress.md` — the spine |
| 6 | Human gate | Risky/failed work goes to "needs a human", never a PR |
| 7 | Log/notification | The PR itself, plus `progress.md`'s "Done" section |

## The loop shape

```
every day (or on-demand):
  read progress.md                      # spine
  find failing tests under watched/     # the work
  for each failing module:
    fix it on its own claude/ branch    # isolation
    have the reviewer subagent grade it # maker-checker
    if PASS-LOW RISK: open a PR         # connector
    if PASS-RISKY or FAIL: log to progress.md, no PR   # human gate
  update progress.md                    # spine, again
```

## Setup

```bash
pip install -r requirements.txt --break-system-packages
```

## See today's starting work

```bash
python3 -m pytest watched/ -v
```
You should see **3 failed, 4 passed** across the two watched modules.

## Run it once, by hand, before scheduling anything

```bash
claude
```

Say **yes** when it asks whether you trust the folder, then:

```
Run the daily-loop skill.
```

Watch it: read the (empty) spine, find the 2 broken modules, fix each one
on its own branch, get an independent reviewer verdict for each, and open
pull requests for the low-risk passes. Then check `progress.md` — it
should now have entries under "Done" with today's date.

**This step matters.** Part 6 of the course is explicit: prove a loop by
hand, watched, before you ever let it run on a schedule, unattended.

## Turn it into a real scheduled Routine

Once the by-hand run looks right:

```
/schedule every day at 9am, run the daily-loop skill
```

Or, to rehearse without waiting until tomorrow:
```
/schedule in 2 minutes, run the daily-loop skill
```
(One-offs don't count against your daily Routine cap.)

## Requirements for the PR step

Opening real pull requests needs the same setup you already did for
Project 4 (Doorbell) and Project 6:
- This repo needs `CLAUDE_CODE_OAUTH_TOKEN` set as a secret (or the
  Routine needs GitHub connector access, since Routines use your
  claude.ai account's connected GitHub, not a separate token — check
  `claude.ai/customize/connectors`).
- The Claude GitHub App should be installed on this repo.

If you'd rather run this project in "report only" mode first (the safest
way to grow a new loop, per Part 6), tell it:
```
Run the daily-loop skill, but never open pull requests — just report what
you would have fixed and write it to progress.md instead.
```

## What to notice once it's run a few times

- **Add a third broken module** to `watched/` (copy the pattern: a
  `.py` file with a docstring-described bug, plus its own `test_*.py`).
  Run the loop again — it should find and fix it without you changing any
  instructions. That's the payoff of a codified skill (Project 5's
  lesson) plus a spine (Project 3's lesson).
- **Check that "Done" entries accumulate** in `progress.md` across
  multiple runs, rather than being overwritten. That's the spine actually
  working as memory, not just a scratch file.
- **If you deliberately introduce a risky-looking change** (e.g. a module
  where the "fix" would require changing a function's signature), confirm
  the loop logs it to "needs a human" instead of opening a PR. That's the
  human gate holding.

## What ships in this folder

| File | Job |
|---|---|
| `watched/` | The modules the loop watches — currently 2, with real bugs |
| `.claude/skills/daily-loop/SKILL.md` | **The codified whole loop** — find, fix, verify, ship or escalate |
| `.claude/agents/reviewer.md` | The independent checker |
| `progress.md` | **The spine** |
| `requirements.txt` | Just `pytest` |

## The interview-ready idea

> "This project combines every part of a loop into one: a scheduled
> heartbeat, a spine that survives between runs, isolated branches per
> fix, an independent reviewer, and a human gate that only lets low-risk,
> reviewer-approved work ship automatically — anything risky gets logged
> for a person instead. It's the same shape as the course's own
> dogfooding example, built from scratch on my own repo."
