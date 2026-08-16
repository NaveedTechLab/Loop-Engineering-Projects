---
name: draft-proposal
description: >-
  Drafts a proposed action and writes it to proposal.md with status
  PENDING APPROVAL. Never executes anything. Use for the "Routine A"
  drafter step of the two-routine gate.
---

# Draft Proposal

Run the script and report exactly what it wrote. This skill NEVER takes
any real action — it only ever produces a draft for a human to review.

```bash
python3 .claude/skills/draft-proposal/scripts/draft_proposal.py
```

## Rules

- Never execute the proposed action yourself, under any circumstance.
- Never mark a proposal as approved or executed — only a human, by firing
  the executor Routine, can do that.
- Report the proposal's content plainly so the human has what they need
  to decide.
