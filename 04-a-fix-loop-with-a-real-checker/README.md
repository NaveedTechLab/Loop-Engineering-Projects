# Project 4 — A Fix Loop With a Real Checker

**Loop Engineering, Concept 11 — maker-checker: subagents.**

This project is Project 2, one level deeper. Project 2 taught: the agent
that writes the fix should not be the one that approves it. This project
asks the harder question: **what if the fix only pretends to work?**

A pricing calculator (`src/pricing.py`) has 5 functions with bugs, and a
public test suite (`tests/test_pricing.py`, 14 tests, 7 currently fail).
But there's a second file the maker is never shown: **a hidden checker**
(`checker/hidden_checks.py`) that tests the exact same functions with
**different numbers**.

## Why this matters

A weak loop can accidentally "pass" by fixing only what the visible tests
happen to check — for example, hardcoding a special case for the exact
price and quantity used in a test, instead of fixing the general logic.
The public tests would go green. The code would still be broken for every
other input.

**A real checker doesn't just re-run the tests the maker already saw. It
checks the maker's work against cases the maker never optimized for.**
That's what the hidden checker does here, and it's exactly what a good
reviewer subagent should run.

## Setup

```bash
pip install -r requirements.txt --break-system-packages
```

## See the starting point

```bash
python3 -m pytest tests/ -v
```
You should see **7 failed, 7 passed**.

```bash
python3 checker/hidden_checks.py
```
You should see **5/9 passed** — the hidden checker, on different numbers,
also catches the same bugs.

## Run it

```bash
claude
```

Say **yes** when it asks whether you trust the folder, then:

```
/goal Fix the bugs in src/pricing.py so every test in tests/test_pricing.py
passes. Follow each function's docstring exactly — do not special-case any
specific numbers. Never edit the test file. Run
`python3 -m pytest tests/ -v` and show me the output before claiming
anything is done. Before you consider this finished, have the reviewer
subagent independently verify by running both tests/test_pricing.py AND
checker/hidden_checks.py itself, and report PASS or FAIL. Stop after 10
attempts and write what's still failing to progress.md.
```

## What "done" means here — and why it's stricter than Project 2

In Project 2, `pytest` passing was proof enough. Here, a maker could in
theory make `pytest` pass while still being wrong in general — this
project is built specifically to make that gap visible. The reviewer
subagent is instructed to run the hidden checker as part of its PASS/FAIL
decision, which means:

- A fix that passes the public tests but fails the hidden checker → the
  reviewer must say **FAIL**, and explain that this looks like an overfit
  fix.
- Only a fix that passes **both** checkers, verified by the reviewer
  actually running them, earns a PASS.

## What ships in this folder

| File | Job |
|---|---|
| `src/pricing.py` | The buggy code to fix |
| `tests/test_pricing.py` | The public checker — the maker sees and runs this |
| `checker/hidden_checks.py` | The **real** checker — different numbers, only the reviewer runs this |
| `.claude/agents/reviewer.md` | Instructed to run BOTH checkers and look for gaming |
| `requirements.txt` | Just `pytest` |

## The interview-ready idea

> "The agent that does the work should never be the one that decides it's
> done — and the checker itself should test cases the maker never saw,
> not just replay the same tests. Otherwise a loop can learn to satisfy
> the checker instead of actually solving the problem."
