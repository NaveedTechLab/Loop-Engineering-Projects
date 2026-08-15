# Project 5 — Codify the Body

**Loop Engineering, Interlude — codify the body, with dynamic workflows.**

So far, "the body of a beat" (find the work, fix it, verify it) has been
something the agent puts together turn by turn, guided by your prompt. This
project asks a different question: **what if that whole orchestration was
written down once, as a re-runnable script — instead of re-explained every
time?**

## The setup

Three completely independent modules live under `modules/`, each with its
own bug and its own test file:

| Module | File | Bug |
|---|---|---|
| `module_a` | `calc.py` | `power()` adds instead of multiplying |
| `module_b` | `strings.py` | `slugify()` doesn't lowercase, strip punctuation, or collapse spaces |
| `module_c` | `dates.py` | `days_between()` returns a negative number when the dates are reversed |

Run `python3 -m pytest modules/module_a/ modules/module_b/ modules/module_c/ -v`
to see all three fail.

## The codified body

Instead of typing "fix module A, then check it, then fix module B, then
check it..." every time, this project ships a **saved command**:
`.claude/commands/fix-all-modules.md`. It writes the whole loop body down
once — discover the modules, fix each one, verify each one independently
with the reviewer, report a summary — so it's a single command you can
re-run any time new modules get added.

This is the same shape as the maker-checker split from Project 4, plus the
worktree-style isolation from Concept 8, packed into one repeatable unit.

## Run it

```bash
pip install -r requirements.txt --break-system-packages
claude
```

Say **yes** when it asks whether you trust the folder, then:

```
/fix-all-modules
```

That's it — one command runs the whole codified body: it discovers all
three modules, fixes each one according to its docstring, has the
reviewer subagent independently verify each one in isolation, and reports
a summary table at the end.

## What to notice

1. **Isolation held.** Ask the agent afterward: did fixing `module_b`
   ever touch `module_a` or `module_c`'s files? It shouldn't have — each
   module was fixed and verified independently, the same idea as a
   worktree keeping parallel agents from colliding.
2. **The workflow is reusable.** If you add a `module_d/` folder with its
   own bug and test file tomorrow, `/fix-all-modules` should handle it
   without you rewriting any instructions — the orchestration was codified
   once, not re-explained per run.
3. **This is the body of ONE beat, not a loop.** `/fix-all-modules` does
   real work when you run it, but it has no heartbeat and no spine of its
   own. To make it a loop instead of a one-off, you'd pair it with a
   trigger — for example: `/schedule every time a PR touches modules/, run
   /fix-all-modules` — which is exactly the "workflow is the engine, the
   Routine turns the key" idea from the course.

## What ships in this folder

| File | Job |
|---|---|
| `modules/module_a/`, `module_b/`, `module_c/` | Three independent buggy modules, each with its own tests |
| `.claude/commands/fix-all-modules.md` | **The codified body** — the whole fix-and-verify workflow, written once |
| `.claude/agents/reviewer.md` | Checks one module at a time, independently |
| `requirements.txt` | Just `pytest` |
