#!/usr/bin/env python3
"""
check_secret.py — deliberately fails loudly if the secret isn't available
as an environment variable, instead of guessing or silently continuing.

This is the whole lesson of this project: a Routine's cloud clone never
sees your local .env file (it's gitignored, so it never reaches GitHub,
so the clone never has it). The only way a Routine gets a credential is
through its environment-variables panel.
"""

import os
import sys

SECRET_NAME = "DRILL_SECRET"


def main() -> None:
    value = os.environ.get(SECRET_NAME)

    if value is None:
        print(f"  ❌  {SECRET_NAME} is NOT set as an environment variable.", file=sys.stderr)
        print("  " + "─" * 56, file=sys.stderr)
        print("     This is the exact failure a Routine hits if a secret", file=sys.stderr)
        print("     lives only in a .env file: .env is gitignored, so it", file=sys.stderr)
        print("     never reaches the cloud clone, and the Routine finds", file=sys.stderr)
        print("     nothing here — even though it works fine locally.", file=sys.stderr)
        print("  " + "─" * 56, file=sys.stderr)
        sys.exit(1)

    masked = value[:2] + "*" * max(0, len(value) - 2)
    print("  ✅  SECRET FOUND")
    print("  " + "─" * 56)
    print(f"     {SECRET_NAME} = {masked}  (masked, {len(value)} chars)")
    print("     Read from the environment — never hardcoded, never from .env.")
    print("  " + "─" * 56)


if __name__ == "__main__":
    main()
