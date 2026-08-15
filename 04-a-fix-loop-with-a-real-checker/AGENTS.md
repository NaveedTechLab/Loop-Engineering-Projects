# Agent Instructions

This project has a pricing calculator at `src/pricing.py` with several
bugs, and a test suite at `tests/test_pricing.py` that defines what
"fixed" means.

## Rules

- Never edit `tests/test_pricing.py`.
- Fix each function according to its docstring in `src/pricing.py` — the
  docstring is the spec.
- Run `python3 -m pytest tests/ -v` and read the real output before
  claiming anything passes.
- Fix the actual logic described in each docstring. Do not special-case
  the specific numbers used in the tests.
