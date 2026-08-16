#!/usr/bin/env python3
"""
execute_approved.py — Routine B, the executor.

Only runs when explicitly fired (in a real setup, via an API trigger that
a human calls after reading the proposal). Reads proposal.md, and if it's
still PENDING APPROVAL, executes the action and marks it EXECUTED.

Safe to run more than once (idempotent): if the proposal is already
EXECUTED, it does nothing and says so, instead of executing twice. This
is the "writes must be safe to repeat" rule from Concept 10, applied here
because a retried API call should never double-execute an approved
action.
"""

from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
PROPOSAL_FILE = PROJECT_ROOT / "proposal.md"
LOG_FILE = PROJECT_ROOT / "executed-log.md"


def main() -> None:
    if not PROPOSAL_FILE.exists():
        print("  ❌  No proposal.md found. Nothing to execute.")
        return

    content = PROPOSAL_FILE.read_text()

    if "Status: EXECUTED" in content:
        print("  ⏭️   Already executed. Doing nothing (idempotent — safe to retry).")
        return

    if "Status: PENDING APPROVAL" not in content:
        print("  ❌  proposal.md has no recognizable PENDING APPROVAL status. Refusing to act.")
        return

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    log_line = f"- [{now}] Daily check completed. No issues found. (approved and executed)\n"

    if not LOG_FILE.exists():
        LOG_FILE.write_text("# executed-log.md\n\n")

    with LOG_FILE.open("a") as f:
        f.write(log_line)

    updated = content.replace(
        "**Status: PENDING APPROVAL**",
        f"**Status: EXECUTED** (at {now})",
    )
    PROPOSAL_FILE.write_text(updated)

    print("  ✅  EXECUTED")
    print("  " + "─" * 50)
    print(f"     Appended to executed-log.md")
    print(f"     proposal.md marked EXECUTED")
    print("  " + "─" * 50)


if __name__ == "__main__":
    main()
