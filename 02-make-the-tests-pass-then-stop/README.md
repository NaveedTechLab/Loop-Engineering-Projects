# Project 2 — Make the Tests Pass, Then Stop

**Loop Engineering, Concept 5 — conditional / run-until-done heartbeat.**

A small text-processing library (`src/text_utils.py`) has five functions.
Some of them have bugs. A test suite (`tests/test_text_utils.py`) defines
exactly what "fixed" means — 18 tests total, 8 of them currently fail.

Your job: hand `/goal` a stopping condition and walk away. It edits the
code, runs the tests, reads the failures, tries again, and stops only when
every test genuinely passes.

## Setup

```bash
pip install -r requirements.txt --break-system-packages
```

## See the starting point

```bash
python3 -m pytest tests/ -v
```

You should see **8 failed, 10 passed**. Those 8 failures are the work.

## Run it

### 1. Open it in Claude Code

```bash
claude
```

Say **yes** when it asks whether you trust the folder.

### 2. Hand `/goal` the finish line

```
/goal Fix the bugs in src/text_utils.py so that every test in
tests/test_text_utils.py passes. Follow each function's docstring — that
is the spec. Never edit the test file. Run `python3 -m pytest tests/ -v`
and show me the output before claiming anything is done. Stop after 10
attempts and write what's still failing to progress.md.
```

Then walk away. It will read the failures, fix each function, re-run the
tests, and keep going until the sentence above is true.

## The one rule this project will not bend on

**Never edit `tests/test_text_utils.py` to make it pass.** That is exactly
what a loop optimizing for green will reach for. If a test looks wrong,
that is a signal to think harder about the function, not to delete the
test.

## Bonus: add the maker-checker split

This project ships a `reviewer` subagent (`.claude/agents/reviewer.md`)
that independently re-runs the tests and grades the fix — the maker
(the agent writing the fix) is not the same as the checker (the reviewer
confirming it). Try adding this line to your `/goal` prompt:

```
Before you consider this done, have the reviewer subagent independently
verify by running the tests itself and replying PASS or FAIL.
```

## What "done" actually means here

`pytest` returning all green is a **proof**, not a claim — this is the
strongest kind of checker there is (Concept 2's checker ladder: a passing
test is at the top). That is what makes this project a clean example of
Concept 5: the agent that wrote the fix does not get to decide it's done.
A command does.

## What ships in this folder

| File | Job |
|---|---|
| `src/text_utils.py` | The buggy code to fix |
| `tests/test_text_utils.py` | The checker — defines "done", never edit it |
| `.claude/agents/reviewer.md` | Optional second opinion (maker-checker) |
| `requirements.txt` | Just `pytest` |
