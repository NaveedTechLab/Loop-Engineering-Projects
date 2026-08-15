# Project 3 — The Morning Brief With a Memory

**Loop Engineering, Concept 6 — unattended schedules, paired with Concept 12 — the spine.**

This is the two ideas from Sky Watch and Paper Watch, combined into one
project. Every morning it checks Hacker News's top 10 stories — **but only
shows you the ones you haven't seen yet.** How does it skip the ones
already shown? It writes them into `seen-stories.txt`, and reads that file
first next time. That file is the **spine** — the loop's memory.

Nothing to install, no key, no sign-up. The Hacker News API is free and
public.

## See it work right now (by hand, no schedule yet)

```bash
python3 .claude/skills/morning-brief/scripts/brief.py
```

On the first run, you'll see the top 10 stories, all marked as new — this
is the baseline.

## Feel the spine — this is the whole lesson

**Run it again, right away:**

```bash
python3 .claude/skills/morning-brief/scripts/brief.py
```

Unless a story genuinely dropped off the top 10 and a new one entered
(Hacker News updates constantly), you should mostly see **"nothing new
since last brief ✓"**. The loop *remembered* — it wrote the story IDs it
showed you into `seen-stories.txt` and read them back.

```bash
cat seen-stories.txt
```

**Now delete the memory and run it again:**

```bash
rm seen-stories.txt
python3 .claude/skills/morning-brief/scripts/brief.py
```

Every story comes back as "new." You just made the loop forget
everything. **No spine, no loop** — that one file is what turns separate
runs into progress.

## Turn it into a real, unattended loop

```bash
claude
```

Say **yes** when Claude asks whether you trust the folder. Try it once by
hand first:

```
give me this morning's brief
```

Once that reads right, put it on a schedule:

```
/schedule every weekday at 9am, run the morning-brief skill and give me the brief
```

Close your laptop. Every weekday morning, a machine that was never yours
checks Hacker News and reports only what's genuinely new — even though
you never told it what was already shown. The `seen-stories.txt` file,
committed to the repo, is what makes that possible.

**To rehearse without waiting until 9am tomorrow**, fire a one-off test
first:

```
/schedule in 2 minutes, run the morning-brief skill
```

One-offs don't count against your daily Routine cap.

## Why this project needs BOTH concept 6 and concept 12

Compare this to Sky Watch (Project 3 in the official set): Sky Watch
reprints *today's* full forecast every run — it needs no memory. This
project shows only what's *new since last time* — it **cannot work**
without the spine. Same heartbeat (daily schedule), opposite memory need.
That contrast is exactly when you know a loop needs a spine.

## What ships in this folder

| File | Job |
|---|---|
| `.claude/skills/morning-brief/` | Owns the logic: fetch, compare, report |
| `.claude/skills/morning-brief/scripts/brief.py` | Fetches HN; fails loudly rather than inventing headlines |
| `.claude/settings.json` | Pre-grants the permissions the loop needs |
| `AGENTS.md` / `CLAUDE.md` | Point any agent at the skill |
| `seen-stories.txt` | **The spine** — created after the first run |
