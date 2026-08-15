#!/usr/bin/env python3
"""
rate.py — fetches the current USD -> PKR exchange rate from a free,
key-free public API, and compares it to the last reading (if any).

Exits non-zero on failure rather than inventing a rate. This mirrors the
rule used throughout the loop-engineering course projects: a script that
cannot get real data should fail loudly, not guess.
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API_URL = "https://open.er-api.com/v6/latest/USD"
STATE_FILE = Path(__file__).resolve().parent.parent / "last-rate.txt"


def fetch_rate() -> float:
    try:
        with urllib.request.urlopen(API_URL, timeout=10) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"ERROR: could not reach the exchange rate API: {e}", file=sys.stderr)
        sys.exit(1)

    if data.get("result") != "success":
        print(f"ERROR: API did not return success: {data}", file=sys.stderr)
        sys.exit(1)

    try:
        return float(data["rates"]["PKR"])
    except (KeyError, TypeError, ValueError):
        print("ERROR: PKR rate missing from API response", file=sys.stderr)
        sys.exit(1)


def read_last() -> tuple[float, str] | None:
    if not STATE_FILE.exists():
        return None
    try:
        line = STATE_FILE.read_text().strip()
        rate_str, ts = line.split("|", 1)
        return float(rate_str), ts
    except Exception:
        return None


def write_last(rate: float, ts: str) -> None:
    STATE_FILE.write_text(f"{rate}|{ts}\n")


def main() -> None:
    rate = fetch_rate()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    previous = read_last()

    print("  💱  USD → PKR RATE WATCH")
    print("  " + "─" * 44)
    print(f"     1 USD = {rate:.2f} PKR")
    print(f"     as of {now}")

    if previous:
        prev_rate, prev_ts = previous
        delta = rate - prev_rate
        if abs(delta) < 0.01:
            print(f"     essentially unchanged since {prev_ts}")
        else:
            direction = "up" if delta > 0 else "down"
            print(f"     {direction} {abs(delta):.2f} since {prev_ts}")
    else:
        print("     (first reading — nothing to compare yet)")

    print("  " + "─" * 44)

    write_last(rate, now)


if __name__ == "__main__":
    main()
