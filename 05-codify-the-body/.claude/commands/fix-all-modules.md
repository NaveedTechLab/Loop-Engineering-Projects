---
description: Fix bugs in every module under modules/, verified independently by the reviewer subagent, one module at a time.
---

# Fix All Modules

This command codifies the whole "body" of a beat: find the broken
modules, fix each one, verify each one independently, and report a
summary. It is meant to be re-run any time new modules are added to
`modules/` — you should not have to re-explain these steps by hand.

## Steps

1. **Discover the work.** List every subfolder under `modules/`. Each one
   is an independent module with its own source file and its own test
   file (e.g. `modules/module_a/calc.py` and
   `modules/module_a/test_calc.py`).

2. **For each module, in isolation:**
   - Run its tests first: `python3 -m pytest modules/<name>/ -v`
   - If anything fails, read the source file's docstrings — they are the
     spec — and fix the bug(s). Do not touch the test file.
   - Re-run that module's tests until they pass.
   - Do not let work on one module leak into another. Each module's fix
     should only touch that module's own source file.

3. **Verify each module independently.** For every module you touched,
   invoke the `reviewer` subagent and tell it which module to check. Wait
   for its PASS or FAIL before moving to the next module.

4. **Report a summary table** at the end: one line per module, with its
   verdict (PASS/FAIL) and a one-line description of what was fixed.

## Rules

- Never edit any `test_*.py` file.
- Treat each module as independent — a bug or fix in one module must not
  reference or depend on another module.
- If a module's reviewer says FAIL, try again for that module specifically
  before moving on. Do not report a module as done until its reviewer says
  PASS.
