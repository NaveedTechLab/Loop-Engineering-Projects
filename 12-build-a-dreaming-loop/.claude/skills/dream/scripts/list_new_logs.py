#!/usr/bin/env python3
"""
list_new_logs.py — the mechanical part of dreaming.

Reads dreaming-state.md for the last reviewed date, and lists every
run-logs/*.md file dated after that. Finding the PATTERN across those
logs is the agent's job, not this script's — this script only does the
boring, deterministic part: figuring out what's new.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
STATE_FILE = ROOT / "dreaming-state.md"
LOGS_DIR = ROOT / "run-logs"


def read_last_reviewed() -> str:
    if not STATE_FILE.exists():
        return "0000-00-00"
    text = STATE_FILE.read_text()
    match = re.search(r"last_reviewed_date:\s*(\d{4}-\d{2}-\d{2})", text)
    return match.group(1) if match else "0000-00-00"


def main() -> None:
    last_date = read_last_reviewed()

    if not LOGS_DIR.exists():
        print("ERROR: run-logs/ directory not found.", file=sys.stderr)
        sys.exit(1)

    all_logs = sorted(LOGS_DIR.glob("*.md"))
    new_logs = [f for f in all_logs if f.stem > last_date]

    print("  💭  DREAMING — new logs since last review")
    print("  " + "─" * 50)
    print(f"     Last reviewed date: {last_date}")
    print(f"     New logs found: {len(new_logs)}")
    print()

    if not new_logs:
        print("     Nothing new to dream about.")
    else:
        for log in new_logs:
            print(f"     - {log.name}")

    print("  " + "─" * 50)


if __name__ == "__main__":
    main()
