"""
greeter.py — a small, fully WORKING loop. Nothing here is buggy.

This project is different from Projects 2 and 4: the code already works.
The point isn't to fix it — it's to break specific pieces of the loop
on purpose, one at a time, and learn to recognize which layer broke from
the symptom alone. See README.md for the exercises.
"""

import sys
from pathlib import Path

CUSTOMERS_FILE = Path(__file__).resolve().parent.parent / "customers.txt"
PROGRESS_FILE = Path(__file__).resolve().parent.parent / "progress.md"


def read_customers() -> list[str]:
    if not CUSTOMERS_FILE.exists():
        return []
    return [
        line.strip()
        for line in CUSTOMERS_FILE.read_text().splitlines()
        if line.strip()
    ]


def read_greeted() -> set[str]:
    """Read the spine: which customers have already been greeted."""
    if not PROGRESS_FILE.exists():
        return set()
    greeted = set()
    for line in PROGRESS_FILE.read_text().splitlines():
        line = line.strip()
        if line.startswith("- "):
            greeted.add(line[2:].strip())
    return greeted


def make_greeting(name: str) -> str:
    return f"Hello, {name}! Thanks for choosing our service."


def write_progress(greeted: set[str]) -> None:
    lines = ["# progress.md — the spine", "", "## Already greeted", ""]
    for name in sorted(greeted):
        lines.append(f"- {name}")
    PROGRESS_FILE.write_text("\n".join(lines) + "\n")


def main() -> None:
    customers = read_customers()
    already_greeted = read_greeted()

    new_customers = [c for c in customers if c not in already_greeted]

    print("  👋  CUSTOMER GREETER")
    print("  " + "─" * 40)

    if not new_customers:
        print("     No new customers to greet.")
    else:
        for name in new_customers:
            print(f"     {make_greeting(name)}")

    print("  " + "─" * 40)

    all_greeted = already_greeted | set(new_customers)
    write_progress(all_greeted)


if __name__ == "__main__":
    main()
