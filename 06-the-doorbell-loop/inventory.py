"""
inventory.py — a tiny sample module for testing the TODO Doorbell.

Edit this file in a pull request and add a `# TODO: ...` or
`# FIXME: ...` comment somewhere, then open the PR. The doorbell should
flag exactly the comment you added — nothing more, nothing less.
"""


def calculate_reorder_point(daily_usage: float, lead_time_days: int) -> float:
    """How many units to have on hand before placing a reorder."""
    return daily_usage * lead_time_days


def is_low_stock(current_stock: int, reorder_point: float) -> bool:
    """True if stock has fallen to or below the reorder point."""
    return current_stock <= reorder_point

# TODO: test the fixed workflow with id-token permission
