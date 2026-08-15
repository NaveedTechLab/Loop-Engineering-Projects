# Agent Instructions

This project has a text-processing library at `src/text_utils.py` with
several bugs, and a test suite at `tests/test_text_utils.py` that defines
exactly what "fixed" means.

## Rules

- Never edit `tests/test_text_utils.py`. If a test looks wrong, the bug is
  in `src/text_utils.py`, not the test.
- Fix each function according to its docstring in `src/text_utils.py` —
  the docstring is the spec.
- Run `python3 -m pytest tests/ -v` yourself and read the real output
  before claiming anything passes.
- Keep fixes minimal. Do not rewrite functions that already pass their
  tests.
