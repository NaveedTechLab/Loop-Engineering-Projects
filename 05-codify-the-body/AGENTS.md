# Agent Instructions

This project has three independent modules under `modules/`, each with its
own buggy source file and its own test file:

- `modules/module_a/calc.py` — a power function
- `modules/module_b/strings.py` — a slugify function
- `modules/module_c/dates.py` — a days-between-dates function

## Rules

- Never edit any `test_*.py` file.
- Fix each function according to its docstring — the docstring is the
  spec.
- Modules are independent. A fix in one module should never require
  touching another module's files.
- There is a reusable command at `.claude/commands/fix-all-modules.md`
  that codifies the whole fix-and-verify workflow — use `/fix-all-modules`
  to run it.
