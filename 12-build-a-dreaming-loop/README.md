# Project 12 — Build a Dreaming Loop

**The final capstone.** Not a drill — a second loop, pointed at the
memory of your other loops instead of at code directly.

Every project so far improved code. This one improves **the rules that
guide every future run** — Anthropic's applied AI team calls this
pattern "dreaming": a separate loop, with its own heartbeat, that reads
recent run logs, finds mistakes that keep repeating, and proposes a fix
to the rules file — always as a PR a human reviews, never a direct edit.

## The setup

`run-logs/` contains 4 days of (simulated) daily-loop history:

| Date | What happened |
|---|---|
| 2026-08-10 | Fixed `discount.py`, only ran its own test file — broke `test_pricing.py`, caught later by a human |
| 2026-08-11 | Fixed `shipping.py`, only ran its own test file — broke `test_inventory.py`, same pattern |
| 2026-08-12 | Fixed `receipts.py`, only ran its own test file — broke `test_orders.py`. **Third time this week.** |
| 2026-08-13 | Clean day, nothing to fix |

Read them yourself first:
```bash
cat run-logs/*.md
```

Notice the pattern? **Three separate days, the same root cause**: a fix
only ran its own module's tests, not the full suite, and missed a
cross-module regression each time. `AGENTS.md` currently has no rule
about this.

## See the mechanical part work

```bash
python3 .claude/skills/dream/scripts/list_new_logs.py
```
Should list all 4 logs as new (`dreaming-state.md` starts dated before
all of them).

## Run the dream

```bash
claude
```
Say **yes**, then:
```
Run the dream skill.
```

Watch it: read the new logs, notice the 3-times-repeated pattern, and
draft a specific rule addition to `AGENTS.md` — something like "always
run the full test suite before claiming a module fix is done, not just
the changed module's own tests" — as a **pull request**, never a direct
edit to `main`.

## What to check once the PR appears

1. **Does the PR cite evidence?** It should name the three specific dates
   / logs that showed the pattern — not just assert "this seems like a
   good rule."
2. **Is the diff small and specific?** A good dreaming pass proposes a
   precise line, not a rewrite of the whole `AGENTS.md`. Vague rewrites
   lose the specific lesson (this is the "brevity bias" / "context
   collapse" failure mode from the course).
3. **You are the gate.** Read the PR like you'd read any other. Merge it
   only if the evidence genuinely supports the rule. This is the
   highest-leverage file-edit possible — every future run of every loop
   in this repo reads `AGENTS.md`.

## Make it a real weekly loop

Once you've reviewed the pattern above by hand:
```
/schedule every Monday at 9am, run the dream skill
```
Weekly, not daily — dreaming needs a batch of runs to find a pattern in.
A daily dream would mostly find nothing and cost tokens for no signal.

## Two failure modes to watch for (from the course)

- **It can launder an attack.** If a run log ever contains text written
  by an outsider (an issue body, a fetched web page), a dreaming pass
  could turn a planted instruction into a permanent rule. The defenses
  are exactly what this project already has: evidence citation, and the
  human gate — never let a rule change skip review.
- **It can erode what it maintains.** Repeated rewrites can drift from
  specific ("check the response payload, not just the status code") to
  vague ("handle errors better"). Propose small diffs, never full
  rewrites — and because everything lives in git, a shrinking or vague
  `AGENTS.md` shows up in the diff where you can simply refuse to merge
  it.

## What ships in this folder

| File | Job |
|---|---|
| `run-logs/` | 4 days of run history — 3 show the same repeated pattern |
| `AGENTS.md` | The file the dream proposes changes to — never edited directly |
| `dreaming-state.md` | **The dreaming loop's own spine** — tracks what it's already reviewed |
| `.claude/skills/dream/` | The codified dreaming orchestration |
| `.claude/skills/dream/scripts/list_new_logs.py` | The mechanical part — finding what's new |

## The interview-ready idea

> "This loop doesn't touch code — it reads the run history of my other
> loops, looks for a mistake that repeats across multiple separate runs
> rather than a one-off, and proposes a specific rule addition to
> AGENTS.md as a pull request, with evidence citing exactly which runs
> showed the pattern. It never edits the rules file directly, because
> that file is the highest-leverage write in the whole system — every
> future run of every loop reads it — so a human always has to approve
> the change first."
