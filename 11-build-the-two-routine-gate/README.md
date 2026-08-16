# Project 11 — Build the Two-Routine Gate

**Appendix drill A4 — the two-routine approval gate.**

A Routine can't pause mid-run and ask you a question. So when a real
decision needs a human — send an email, merge risky code, spend money —
the gate has to be built **between two Routines**, not inside one. This
project builds that exact pattern, end to end.

## The pattern

```
Routine A (drafter)  →  human reads and decides  →  Routine B (executor)
   writes a draft         approve or reject           only fires on
   never acts                                          explicit approval
```

- **Routine A** finds work and drafts a proposed action into
  `proposal.md`, marked `PENDING APPROVAL`. It never acts.
- **A human** reads the proposal and decides.
- **Routine B** has an **API trigger** — it only runs when someone sends
  an authenticated request to its `/fire` endpoint. That request *is* the
  approval. Routine B reads `proposal.md`, and if it's still pending,
  executes the action and marks it `EXECUTED`.

## Part 1 — See the mechanism work locally first

```bash
python3 .claude/skills/draft-proposal/scripts/draft_proposal.py
cat proposal.md
```
You should see `**Status: PENDING APPROVAL**`. Nothing has happened yet —
confirm `executed-log.md` doesn't exist:
```bash
ls executed-log.md   # should say "No such file"
```

Now simulate approval by running the executor directly:
```bash
python3 .claude/skills/execute-approved/scripts/execute_approved.py
cat executed-log.md
grep "Status:" proposal.md
```
Should now show `**Status: EXECUTED**`.

**Try running the executor again:**
```bash
python3 .claude/skills/execute-approved/scripts/execute_approved.py
```
It should say **"Already executed. Doing nothing"** — not append a
second log entry. This matters: an API trigger has no built-in
deduplication, and a retried request should never double-execute an
approved action (Concept 10's "writes must be safe to repeat" rule).

## Part 2 — Build it as two real Routines

**Routine A — the drafter** (schedule trigger):
```bash
claude
```
```
/schedule every day at 9am, run the draft-proposal skill
```

**Routine B — the executor** (API trigger, set up on the web):
1. Go to `claude.ai/code/routines` and create a new routine.
2. Prompt: `Run the execute-approved skill.`
3. Repository: this repo.
4. Trigger: **API**, not schedule. Generate the token and **save it
   immediately** — it's shown once.

## Part 3 — The approval action, for real

When Routine A's next run drafts a proposal, read `proposal.md`. If you
approve, fire Routine B yourself:

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/<routine-id>/fire \
  -H "Authorization: Bearer <routine-token>" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Approved by me, please execute."}'
```

That one `curl` call **is** the human gate — it's the only thing that can
turn a draft into an executed action. If you never run it, nothing ships.

## Why this matters more than it looks

Every risky action in a real loop (Project 8's daily loop opening PRs,
a hypothetical loop that sends money or emails) needs exactly this
shape once the action gets risky enough that "reviewer says PASS" isn't
enough on its own. The reviewer subagent from Projects 2, 4, 5, and 8
answers "is this correct?" — the two-routine gate answers a different
question: "should this happen at all, and did a person actually decide
that?"

## What ships in this folder

| File | Job |
|---|---|
| `.claude/skills/draft-proposal/` | Routine A — drafts only, never acts |
| `.claude/skills/execute-approved/` | Routine B — acts only when fired, idempotent |
| `proposal.md` | The draft, created on first run |
| `executed-log.md` | The record of what's actually been executed |

## The interview-ready idea

> "Since a Routine can't pause mid-run to ask a person anything, I built
> the approval gate between two separate Routines instead of inside one:
> a drafter that only ever writes a proposal, and an executor with an API
> trigger that only fires on an explicit, authenticated approval call.
> The executor is also idempotent — running it twice doesn't execute
> twice — because an API trigger has no built-in protection against a
> retried request."
