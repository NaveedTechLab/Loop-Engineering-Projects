---
name: dream
description: >-
  Reads new run-logs since the last dream, looks for patterns that repeat
  across multiple separate runs (not one-off mistakes), and proposes a
  specific rule addition to AGENTS.md as a pull request — never a direct
  edit. Use for the weekly dreaming pass.
---

# Dream

You are the dreaming loop. Your job is NOT to fix code. Your job is to
find mistakes that keep repeating across separate runs, and propose a
rule that would have prevented them — as a draft, never a direct edit.

## 1. Find what's new

```bash
python3 .claude/skills/dream/scripts/list_new_logs.py
```
This tells you which log files under `run-logs/` are new since the last
dream. Read all of them.

## 2. Look for a REPEATED pattern — not a one-off

One mistake in one log is noise. The same mistake appearing in **two or
more separate logs** is a missing lesson worth writing down. Read each
new log's "Follow-up" notes carefully — that's usually where the real
signal is.

Do not propose a rule based on a single occurrence. If nothing repeats,
say so plainly and stop — that's a correct, successful result.

## 3. Draft the fix as a PR, never a direct edit

If you find a genuine repeated pattern:

- Write the smallest, most specific rule addition to `AGENTS.md` that
  would have prevented the pattern (a small diff, not a rewrite of the
  whole file — see "avoid decay" below).
- Commit it on a `claude/dream-<short-topic>` branch.
- Open a pull request. Its description MUST include the evidence: which
  specific logs/dates showed the pattern, and how many times.
- Never edit `AGENTS.md` directly on `main`. This is the human gate for
  the highest-leverage file in the whole project — every future run reads
  it.

## 4. Update your own memory last

Update `dreaming-state.md`'s `last_reviewed_date` to the most recent log
date you reviewed, so next week's dream only looks at what's new after
that.

## Avoid decay

When proposing a rule, keep it small and specific ("run the full test
suite, not just the changed module's own tests, before claiming a fix is
done") rather than vague ("be more careful with tests"). A vague rewrite
loses the specific lesson the evidence actually supports.

## Rules

- Never edit AGENTS.md directly. Always propose it as a PR.
- Never propose a rule from a single occurrence — require at least 2
  separate logs showing the same pattern.
- Always cite your evidence (which logs, which dates) in the PR
  description.
