# Project 9 — Rehearse a Routine for Free

**Appendix drill A3 — one-off schedules.**

This project has no real work in it on purpose. The lesson is entirely
about a habit: **prove a schedule fires correctly, fast, before you ever
trust it to run overnight unattended.**

## The problem this solves

A scheduled Routine is slow to prove — you can't watch midnight arrive.
If you set `/schedule every day at 9am` and just wait, you won't know if
it's actually going to work until tomorrow morning, and if it's broken,
you've burned a whole day finding out.

## The fix: one-off schedules

A one-off schedule fires once, at a time you choose — including "in 2
minutes" — and then turns itself off. Critically: **one-off runs do not
count against your daily Routine cap.** So you can rehearse as many times
as you need, for free, before committing to a real recurring schedule.

## The drill

### Step 1 — Fire a fast one-off

```bash
claude
```
Say **yes** when it asks whether you trust the folder, then:
```
/schedule in 2 minutes, run the quick-check skill
```

### Step 2 — Note the time you fired it

Write down (or just remember) the clock time right now.

### Step 3 — Wait, then check the run history

After about 2 minutes, check the Routine's run history (either in the
CLI with `/schedule list`, or at `claude.ai/code/routines`).

### Step 4 — Compare timestamps

The timestamp the script printed should be about 2 minutes after the time
you fired the command. **This is the proof.** If it matches, you've
confirmed:
- The schedule mechanism actually works in this environment.
- The skill runs correctly when triggered by a schedule (not just when
  you type the prompt by hand).
- You didn't just see a cached or imagined result — the timestamp is
  real evidence of a fresh run.

### Step 5 — Now, and only now, set a real recurring schedule

```
/schedule every day at 9am, run the quick-check skill
```

## Why this matters more than it looks

This is Part 6's rule, made physical: **prove it fast and watched before
you trust it slow and unattended.** Every project so far that used a
schedule (Sky Watch, the Morning Brief, the Daily Loop) benefits from this
habit — rehearsing with a 2-minute one-off before committing to a real
cadence is cheap insurance against discovering a broken schedule the hard
way, a day (or several) later.

## What ships in this folder

| File | Job |
|---|---|
| `.claude/skills/quick-check/` | A deliberately trivial, timestamped task |
| `.claude/skills/quick-check/scripts/quick_check.py` | Proves a real run happened, via its timestamp |

## The interview-ready idea

> "Before trusting any schedule to run overnight, I rehearse it with a
> one-off fire a couple of minutes out — which doesn't count against the
> daily run cap — and compare the timestamp it produces against when I
> fired it. That's cheap, fast proof the schedule actually works, instead
> of finding out it's broken the next morning."
