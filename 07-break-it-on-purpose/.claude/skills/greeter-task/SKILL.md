---
name: greeter-task
description: >-
  Greets new customers from customers.txt, skipping anyone already greeted
  according to progress.md. Use this when asked to greet customers or run
  the greeter.
---

# Greeter Task

You run the customer greeter and report its output honestly.

## How to run it

```bash
python3 src/greeter.py
```

## Before reporting anything as done

Always run `python3 -m pytest tests/ -v` yourself and read the actual
output. Never claim the greeter "works correctly" without having run both
the tests and the script itself in this session.

## What to report

- List exactly which customers were greeted this run (if any).
- If the tests fail, report the failure honestly — do not claim success.
- "No new customers to greet" is a correct, successful result, not a
  failure.
