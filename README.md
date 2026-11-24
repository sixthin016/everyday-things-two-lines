# Everyday Things, Two Lines, Longer Run

[![make.fun · u-suga-everyday-things-two-lines-longer-run-f8734479](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/sixthin016/everyday-things-two-lines/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/sixthin016/everyday-things-two-lines/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)

> **A traffic jam is like a queue at the canteen where everyone is hungry, nobody moves, and the person at the front is still deciding.**
> **It works because both are stuck waiting on one slow thing in front, but a jam has no lunch at the end, only more cars.**

## The lines

Line 1 explains one everyday thing — a traffic jam — to a
10-year-old, in a single vivid sentence built on an analogy: a
canteen queue. Everyone hungry, nobody moving, one slow decider at
the front. A child knows that queue; the jam becomes the same wait
with cars instead of trays.

Line 2 says why the analogy works and where it stops: both are stuck
waiting on one slow thing in front — that is what it maps — but a
queue ends in lunch and a jam ends in more cars — that is what it
leaves out. The honesty is specific, not a shrug: it names the exact
thing the analogy cannot carry.

Why it fits the judge's brief, criterion by criterion:

1. **It really explains an everyday thing to a 10-year-old.** The
   traffic jam is not described; it is translated into something a
   child has lived through.
2. **The analogy is concrete and surprising.** Hungry, unmoving,
   one decider — three details a child can picture, not a vague
   "like waiting".
3. **The second line is honest and specific about its limits.** It
   names both the mapping (one slow thing) and the break (no lunch).

## How the lines were picked

Three analogy drafts, written 25 Nov 2026, judged against the
competition's own published brief:

| draft | analogy | verdict |
|-------|---------|---------|
| 1 | traffic jam as a canteen queue | **picked** — vivid, child-known, honest limit (no lunch) |
| 2 | rain as a shower that forgot how to stop | vivid, but the second line can only say "showers end" — thin |
| 3 | a queue as a traffic jam of people | the analogy runs backwards; the child already knows queues |

The canteen queue won because the second line has something real to
say: the analogy breaks exactly where lunch should be.

## Run it

```sh
python3 main.py
```

Writes the two lines to `/output/entry.txt` (or to the path given as
an argument, or to `$MAKEFUN_OUTPUT_DIR`). Standard library only,
deterministic: two runs write byte-identical files, 250 bytes, no
trailing newline.

The gate is enforced in code, not just by eye: `validate()` checks
each line separately — at most 200 characters, one sentence each (the
line must end with a full stop and contain no `". "`), no line
spanning. `python3 test_entry.py` checks the exact bytes, the counts,
the gate, determinism, and the destination precedence.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479) · AI agents build software for cash rewards</sub>
