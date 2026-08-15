"""
test_greeter.py — confirms the baseline actually works.

This project's code starts CORRECT (unlike Projects 2 and 4). Run this
once at the start to confirm the baseline is healthy before you start
breaking things on purpose.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from greeter import make_greeting, read_customers, read_greeted


def test_make_greeting():
    assert make_greeting("Ahmed") == "Hello, Ahmed! Thanks for choosing our service."


def test_read_customers_returns_list():
    customers = read_customers()
    assert isinstance(customers, list)
    assert len(customers) > 0


def test_read_greeted_returns_set_when_no_file():
    # This test assumes progress.md may or may not exist — either way,
    # read_greeted() should return a set, never crash.
    result = read_greeted()
    assert isinstance(result, set)
