# Agent Instructions

This project has two separate skills that must never be merged into one:

- `draft-proposal` — ONLY drafts. Never executes.
- `execute-approved` — ONLY executes an already-approved proposal, and
  only when explicitly fired by a human's approval action. Never runs on
  a schedule.

This separation IS the human gate. Do not suggest combining them "for
convenience" — that would remove the one safeguard this project exists to
demonstrate.
