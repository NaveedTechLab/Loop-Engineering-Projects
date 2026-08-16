#!/usr/bin/env python3
"""
draft_proposal.py — Routine A, the drafter.

Drafts a proposed action and writes it to proposal.md with status
PENDING APPROVAL. This script NEVER executes anything by itself — it
only ever writes a draft for a human to read.
"""

from datetime import datetime, timezone
from pathlib import Path

PROPOSAL_FILE = Path(__file__).resolve().parent.parent.parent.parent.parent / "proposal.md"


def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    content = f"""# Proposal — drafted {now}

**Status: PENDING APPROVAL**

## Proposed action

Append the following line to `executed-log.md`:

> "Daily check completed at {now}. No issues found."

## Why

This is a drill proposal — in a real Routine, this section would explain
what was found and why this action is being proposed (e.g. "found 3
overnight CI failures, drafted fixes, all passed review").

## What happens next

This file is a DRAFT ONLY. Nothing has been executed. A human must read
this proposal and, if they approve, fire the executor Routine via its API
trigger (see README.md for the exact command). Only that explicit action
will cause anything to actually happen.
"""

    PROPOSAL_FILE.write_text(content)

    print("  📝  PROPOSAL DRAFTED")
    print("  " + "─" * 50)
    print(f"     Written to: {PROPOSAL_FILE.name}")
    print("     Status: PENDING APPROVAL")
    print("     Nothing has been executed. Waiting for human approval.")
    print("  " + "─" * 50)


if __name__ == "__main__":
    main()
