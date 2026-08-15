#!/usr/bin/env python3
"""
hidden_checks.py — the REAL checker, run only by the reviewer subagent.

This uses DIFFERENT numbers than tests/test_pricing.py. It exists to catch
a fix that happens to make the public tests pass without actually fixing
the underlying logic correctly — for example, a "fix" that only works for
the exact quantities and prices used in the visible tests.

This file is not a secret in the sense of being hidden from you, the
human. It's "hidden" from the MAKER agent's normal workflow: the maker is
told to make tests/test_pricing.py pass, and is never shown this file. Only
the reviewer subagent is instructed to run it. That gap — a checker the
maker cannot see or optimize against — is the whole point of a real
checker.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from pricing import (
    apply_percentage_discount,
    tiered_discount_rate,
    calculate_tax,
    format_currency,
    calculate_total,
)

CHECKS = []


def check(name, actual, expected):
    ok = actual == expected
    CHECKS.append((name, ok, actual, expected))
    return ok


def main():
    check("percentage_discount_25pct", apply_percentage_discount(200, 25), 150.0)
    check("tier_qty_4_no_discount", tiered_discount_rate(4), 0.0)
    check("tier_qty_6_mid_tier", tiered_discount_rate(6), 0.10)
    check("tier_qty_15_top_tier", tiered_discount_rate(15), 0.15)
    check("tax_8pct_on_250", calculate_tax(250, 0.08), 20.0)
    check("currency_small_50", format_currency(50), "$50.00")
    check("currency_25000", format_currency(25000), "$25,000.00")
    check("total_mid_tier_case", calculate_total(20, 6, 0.10), 118.8)
    check("total_top_tier_case", calculate_total(5, 12, 0.05), 53.55)

    passed = sum(1 for _, ok, _, _ in CHECKS if ok)
    total = len(CHECKS)

    print(f"HIDDEN CHECKER: {passed}/{total} passed\n")
    for name, ok, actual, expected in CHECKS:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}: got {actual!r}, expected {expected!r}")

    if passed < total:
        sys.exit(1)


if __name__ == "__main__":
    main()
