"""
service_fee.py — watched module 1.

This is the kind of small, real work the daily loop discovers each
morning: a module whose own tests are failing.
"""


def calculate_late_fee(days_late: int, daily_rate: float = 5.0) -> float:
    """Calculate a late payment fee.

    No fee if not late (days_late <= 0). Otherwise, daily_rate per day
    late, capped at 10 days worth of fees even if later than that.

    calculate_late_fee(0)  -> 0.0
    calculate_late_fee(3)  -> 15.0
    calculate_late_fee(20) -> 50.0  (capped at 10 days: 10 * 5.0)
    """
    if days_late <= 0:
        return 0.0
    return min(days_late, 10) * daily_rate
