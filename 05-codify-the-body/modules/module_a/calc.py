"""
calc.py — module A. One function, one bug.
"""


def power(base: int, exponent: int) -> int:
    """Raise base to exponent, for non-negative integer exponents.

    power(2, 3) -> 8    (2 * 2 * 2)
    power(5, 0) -> 1    (anything to the power 0 is 1)
    power(3, 1) -> 3
    """
    result = 1
    for _ in range(exponent):
        result *= base
    return result
