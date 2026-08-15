import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, str(Path(__file__).resolve().parent))

from dates import days_between


def test_days_between_forward():
    assert days_between(date(2026, 1, 1), date(2026, 1, 10)) == 9


def test_days_between_backward():
    assert days_between(date(2026, 1, 10), date(2026, 1, 1)) == 9


def test_days_between_same_day():
    assert days_between(date(2026, 1, 1), date(2026, 1, 1)) == 0


def test_days_between_across_month():
    assert days_between(date(2026, 1, 28), date(2026, 2, 3)) == 6
