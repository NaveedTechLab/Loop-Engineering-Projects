"""
dates.py — module C. One function, one bug.
"""

from datetime import date


def days_between(start: date, end: date) -> int:
    """Return the number of whole days between two dates.

    Always returns a non-negative number, regardless of which date comes
    first — days_between(later, earlier) should equal
    days_between(earlier, later).

    days_between(date(2026, 1, 1), date(2026, 1, 10)) -> 9
    days_between(date(2026, 1, 10), date(2026, 1, 1)) -> 9
    days_between(date(2026, 1, 1), date(2026, 1, 1))  -> 0
    """
    delta = end - start
    return abs(delta.days)
