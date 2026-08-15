# Project 1 — A Watch Loop (USD → PKR Rate Watch)

**Loop Engineering, Concept 4 — in-session heartbeat.**

This project watches the USD to PKR exchange rate and reports it back to
you, every minute, while you do something else. Close the terminal and the
watching dies — that is the whole concept.

It uses a free, key-free public API (`open.er-api.com`), so there is
nothing to sign up for.

## See it work right now (no loop needed)

```bash
python3 .claude/skills/rate-watch/scripts/rate.py
```

Run it twice in a row. The second run will tell you how much the rate
moved since the first — because it saves its last reading to
`last-rate.txt` and compares against it. That file is the loop's memory
(the **spine**, if you remember that word from the course).

## Turn it into a loop

```bash
claude
```

Say **yes** when Claude asks whether you trust the folder. Then type:

```
/loop show me the USD to PKR rate every minute
```

That is the last thing you type. A fresh reading arrives every minute
while you work on something else.

## The one thing to notice

**Now close the terminal.** The watching dies with it. That is not a bug —
it is the definition of an in-session loop. This is exactly what Project 1
(the ISS loop) taught, just with a different thing to watch.

## What ships in this folder

| File | Job |
|---|---|
| `.claude/skills/rate-watch/` | Owns the logic: fetch the rate, compare to last time, report plainly |
| `.claude/skills/rate-watch/scripts/rate.py` | Calls the API; fails loudly instead of inventing a number |
| `.claude/settings.json` | Pre-grants the permissions the loop needs, so it never stops to ask |
| `AGENTS.md` | Points any agent at the skill |
| `CLAUDE.md` | One line — imports `AGENTS.md` |

## Try a harder prompt

Once the basic loop works, try:

```
/loop every 5 minutes, check the USD to PKR rate and only tell me if it moved more than 0.50
```

This is a small taste of Concept 6 (Sky Watch) — a watch that stays quiet
on calm readings and speaks up only when something is worth mentioning.
