# Loop Engineering Projects

Hands-on implementations of five core loop engineering patterns — built while completing the [GIAIC Final Marathon](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course) Loop Engineering crash course. Each project is a working, deployed example of a different **heartbeat** (what starts a loop) and the **spine** (how it remembers between runs).

## What's a Loop?

A loop is a system that starts itself, checks its own work, records progress, and repeats — without a human driving each step. The four layers that make this possible:

- **Prompt** — a single message to the model
- **Context** — what the model can see in that moment
- **Harness** — one complete beat: instruction → tool use → self-verification → stop
- **Loop** — the system that starts, judges, and remembers multiple beats over time

## Projects

| # | Project | Heartbeat | What It Demonstrates |
|---|---------|-----------|----------------------|
| [01](./01-iss-loop) | **ISS Loop** | In-session | Runs only while the terminal is open — closing it ends the loop. The simplest possible heartbeat. |
| [02](./02-portfolio) | **Portfolio Builder** | Conditional (`/goal`) | A loop that runs until a *provable* condition is met (`20/20` on a mechanical checker), verified by a separate reviewer agent — maker-checker in practice. |
| [03](./03-sky-watch) | **Sky Watch** | Scheduled | A cloud Routine that runs every night at midnight regardless of whether my laptop is on. Reports "all clear" as a valid, successful result — not a failure. |
| [04](./04-doorbell) | **Doorbell** | Event-driven | Zero cost until a pull request is opened — then a fresh GitHub Actions runner reviews the code within a minute, using nothing but the git history to reconstruct context it never directly saw. |
| [05](./05-paper-watch) | **Paper Watch** | Scheduled + Spine | Tracks new arXiv papers on a topic, remembering what's already been shown via a `progress.md` file. Delete that file and everything looks "new" again — a live demonstration of *"no spine, no loop."* |

## Core Concepts Covered

- **Maker-checker** — the agent that does the work is never the one that approves it
- **Human gate** — when a decision is genuinely ambiguous, the loop stops and asks rather than guessing (see Project 02, where the agent found an environment bug and asked for sign-off before touching a protected file)
- **Spine** — persistent state between beats, without which a loop can't tell what it already did (Project 05)
- **Heartbeat types** — in-session, conditional, scheduled, and event-driven, each suited to a different kind of task

## Stack

- [Claude Code](https://code.claude.com) — `/loop`, `/goal`, `/schedule`, and Routines
- GitHub Actions (event-driven trigger for Project 04)
- Public APIs: Open Notify (ISS position), NASA NeoWs (asteroid data), arXiv

## Author

Muhammad — AI Automation Engineer, [NaveedTechLab](https://github.com/NaveedTechLab)
