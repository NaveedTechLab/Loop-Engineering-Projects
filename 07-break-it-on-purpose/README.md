# Project 7 — Break It On Purpose

**Ties together the Four Layers diagnostic skill with everything you've built so far.**

Every other project so far started broken and you fixed it. This one
starts **working** — 3/3 tests pass, the greeter runs correctly, the spine
works. Your job is to break specific layers on purpose, one at a time,
predict the symptom before you break it, then confirm the real symptom
matches the diagnostic table from the Four Layers course:

| Symptom | Broken layer |
|---|---|
| Kaam sahi hai, magar shape/tone galat | **Prompt** |
| Confident hai, magar factually galat | **Context** |
| "Done" bol diya, magar verify nahi kiya | **Harness** |
| Baar baar wahi ghalti, rukta nahi | **Loop** |

## Setup — confirm the baseline is healthy first

```bash
python3 -m pytest tests/ -v
```
Should show **3 passed**.

```bash
python3 src/greeter.py
```
Should greet all 3 customers in `customers.txt`. Run it again — it should
say "No new customers to greet." That confirms the spine (`progress.md`)
works before you start breaking anything.

**Reset between exercises:**
```bash
rm -f progress.md
```

---

## Exercise 1 — Break the Loop layer (the spine)

**Predict first:** if the loop's memory is gone, what will happen when
you run it twice?

**Break it:**
```bash
python3 src/greeter.py   # greets everyone, writes progress.md
rm progress.md            # delete the spine
python3 src/greeter.py    # run again
```

**Observe:** every customer gets greeted again, as if for the first time.

**Diagnosis:** this is "no spine, no loop" — the Loop layer. Without
memory, the loop repeats its first step forever instead of building on
what it already did.

**Undo:** nothing to undo — `progress.md` regenerates on the next run.

---

## Exercise 2 — Break the Context layer

**Predict first:** if the agent can't see what it needs, but is still
confident, what will it produce?

**Break it:** open Claude Code in this folder and ask it to greet
customers, but first tell it to ignore `progress.md`:

```
Greet the customers in customers.txt. Don't bother reading progress.md
first — just greet everyone in the list.
```

**Observe:** it confidently greets everyone, including customers who were
already greeted in a previous run — not because it's broken, but because
you removed its access to the fact that mattered (who's already been
greeted). It sounds completely sure of itself while being wrong.

**Diagnosis:** Context layer. The model didn't fail — it correctly used
what was in its context. The problem is what was *missing* from that
context.

**Undo:** just ask it normally next time: "greet new customers, checking
progress.md first."

---

## Exercise 3 — Break the Harness layer

**Predict first:** if the agent is told to skip verification, what will
it claim?

**Break it:** ask Claude Code:

```
Run the greeter and tell me it works, but don't bother actually running
the tests first — just tell me it's fine.
```

**Observe:** it may report success without having actually run
`pytest`. If you then ask "did you actually run the tests and see the
output yourself?", a well-behaved agent should admit it didn't, or should
have run them anyway despite the instruction — a good test of whether the
harness (self-verification) habit is genuinely built in, or whether it
just does whatever it's told.

**Diagnosis:** Harness layer. This is the "'Done!' bola, magar test nahi
chalaya" failure — a confident claim with no visible proof behind it.

**Undo:** ask it to actually run the tests and show you the output before
claiming anything.

---

## Exercise 4 — Break the Prompt layer

**Predict first:** if the instruction itself is vague, what kind of wrong
output do you expect — wrong logic, or just a wrong-feeling result?

**Break it:** ask Claude Code something genuinely ambiguous:

```
do something with the greeter thing
```

**Observe:** the agent has to guess what you want — it might run the
script, might explain the code, might ask a clarifying question, might
try to "improve" something you didn't ask it to touch. Whatever it picks,
it's unlikely to match the one specific thing you actually had in mind.

**Diagnosis:** Prompt layer. The code and context are fine — the
instruction itself didn't say what "done" looks like.

**Undo:** give it a specific instruction: "run the greeter and tell me
who got greeted."

---

## The point of this project

Reading the diagnostic table is not the same as recognizing a symptom in
the moment. After doing all four exercises, you should be able to look at
almost any agent failure and ask the right first question — **"which
layer broke?"** — instead of jumping straight to rewriting the prompt,
which only fixes one of the four possible problems.

## What ships in this folder

| File | Job |
|---|---|
| `src/greeter.py` | Fully working baseline — nothing to fix here |
| `tests/test_greeter.py` | Confirms the baseline is healthy |
| `customers.txt` | Sample input data |
| `.claude/skills/greeter-task/SKILL.md` | Correct instructions for the working task |
| `progress.md` | The spine — generated on first run |
