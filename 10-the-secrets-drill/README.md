# Project 10 — The Secrets Drill

**Appendix drill A4 — secrets, state, and identity.**

This drill reproduces one of the most common first-time Routine failures,
on purpose, so you recognize it instantly if you ever hit it for real:
**a Routine finds no credentials and fails, even though the exact same
script works perfectly on your own machine.**

## The mechanism (read this before doing the drill)

- `.env` files are the normal way to keep secrets out of git locally.
- `.gitignore` in this project excludes `.env` — which means `.env`
  **never reaches GitHub**, gitignored or not.
- A cloud Routine works from a **fresh clone of your GitHub repo**. If
  `.env` never reached GitHub, the clone doesn't have it either.
- Result: the Routine fires, finds no credential, and fails — or worse,
  an agent might improvise something plausible-sounding instead of
  failing honestly. This script is written to fail loudly instead
  (Concept 12's "never invent a fact" habit, applied to secrets).

## Part 1 — Prove it works locally

```bash
cp .env.example .env
```
Edit `.env` and set `DRILL_SECRET` to any test value.

Now load it into your shell and run the check:
```bash
# macOS/Linux
export $(cat .env | xargs)
python3 .claude/skills/secret-check/scripts/check_secret.py
```
```powershell
# Windows PowerShell
Get-Content .env | ForEach-Object {
  if ($_ -match '^([^=]+)=(.*)$') {
    [System.Environment]::SetEnvironmentVariable($matches[1], $matches[2])
  }
}
python3 .claude/skills/secret-check/scripts/check_secret.py
```

You should see **✅ SECRET FOUND**, with the value masked.

## Part 2 — Confirm `.env` never reaches GitHub

```bash
git status
```
`.env` should **not** appear as a file git wants to commit — `.gitignore`
is doing its job. This is the exact reason a Routine can't see it.

## Part 3 — Watch it fail as a Routine (the actual drill)

```bash
claude
```
Say **yes**, then:
```
/schedule in 2 minutes, run the secret-check skill
```

**Do NOT set anything in the environment-variables panel yet.** Wait for
the one-off to fire, then check its run output (`/schedule list`, or
`claude.ai/code/routines`).

**You should see it fail** — `❌ DRILL_SECRET is NOT set` — even though
Part 1 just proved the exact same script works fine locally. This is the
failure the appendix warns about, reproduced on purpose where it's safe.

## Part 4 — Fix it the right way

Go to your Routine's settings (`claude.ai/code/routines` → this
routine → Environment) and add `DRILL_SECRET` with a test value in the
**environment variables panel** — never in a committed file.

Fire another one-off:
```
/schedule in 2 minutes, run the secret-check skill
```

This time it should succeed.

## The two-line summary

> Secrets go in the Routine's environment-variables panel. Never in
> `.env` — `.env` is gitignored, so it never reaches the clone a Routine
> runs from.

If you ever build a Routine that needs a real credential, add one clear
line to its prompt too: *"credentials are available as environment
variables; do not look for a .env file"* — without it, an agent may still
try the `.env` path out of habit.

## What ships in this folder

| File | Job |
|---|---|
| `.claude/skills/secret-check/scripts/check_secret.py` | Fails loudly if the secret isn't in the environment — never guesses |
| `.env.example` | A safe-to-commit template (no real secret) |
| `.gitignore` | Excludes the real `.env` — this is the whole mechanism |

## The interview-ready idea

> "I reproduced the classic Routine secrets failure on purpose: a script
> that works locally via a `.env` file fails in the cloud, because `.env`
> is gitignored and never reaches the Routine's fresh clone. The fix is
> to put secrets in the Routine's own environment-variables panel, which
> is separate from the repo entirely — and to tell the prompt explicitly
> not to go looking for a `.env` file, since an agent might otherwise try
> out of habit."
