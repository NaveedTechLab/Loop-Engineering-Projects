#!/usr/bin/env python3
"""
quick_check.py — deliberately trivial.

This project isn't about what the task does — it's about practicing the
REHEARSAL habit before trusting any Routine to run unattended overnight.
This script just proves a fresh run actually happened, with a real
timestamp, so you can tell a genuine fire from a stale cached result.
"""

from datetime import datetime, timezone

def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print("  ✅  QUICK CHECK")
    print("  " + "─" * 40)
    print(f"     This run fired at: {now}")
    print("     If you're reading this in a Routine's run history,")
    print("     compare this timestamp to when you fired it.")
    print("  " + "─" * 40)

if __name__ == "__main__":
    main()
