#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes two lines to ``entry.txt``. Line 1 explains one everyday thing
-- a traffic jam -- to a 10-year-old in a single vivid sentence built
on an analogy. Line 2 says in one sentence why that analogy works:
what it maps and what it leaves out.

The analogy is a canteen queue: everyone hungry, nobody moving, one
slow decider at the front. A 10-year-old knows that queue; the jam
becomes the same wait with cars instead of trays. The second line is
honest about the limit -- a queue ends in lunch, a jam ends in more
cars -- which is exactly what the brief asks the second line to do.

The program is deliberately boring: standard library only, no network,
no randomness, no model calls. It checks both lines against the
competition gate (UTF-8, one sentence each, at most 200 characters
per line) and writes exactly those bytes, joined by a single newline
and with no trailing newline, so the byte count the judge's tie-break
reads is the two lines themselves.

Output destination, in order:
  1. the first command-line argument, when given;
  2. ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when the variable is set;
  3. ``/output/entry.txt``.
"""

import os
import sys

# Line 1: the analogy -- a traffic jam as a canteen queue, in one
# vivid sentence a 10-year-old can picture.
# Line 2: the honest limit -- what the analogy maps, and what it
# leaves out (lunch).
LINES = (
    "A traffic jam is like a queue at the canteen where everyone is hungry, nobody moves, and the person at the front is still deciding.",
    "It works because both are stuck waiting on one slow thing in front, but a jam has no lunch at the end, only more cars.",
)

MAX_CHARS = 200
MIN_CHARS = 1
DEFAULT_PATH = "/output/entry.txt"
FILE_NAME = "entry.txt"


def text_of(lines):
    """Join the lines with one newline between them, none after."""
    return "\n".join(lines)


def validate(lines):
    """Check *lines* against the competition gate; return problems."""
    problems = []
    if len(lines) != 2:
        problems.append("entry must have exactly two lines, got %d" % len(lines))
    for index, line in enumerate(lines, start=1):
        if not isinstance(line, str):
            problems.append("line %d is not text" % index)
            continue
        if len(line) < MIN_CHARS:
            problems.append("line %d is empty" % index)
        if len(line) > MAX_CHARS:
            problems.append(
                "line %d is %d characters, over the %d-character limit"
                % (index, len(line), MAX_CHARS)
            )
        if line.strip() == "":
            problems.append("line %d is only whitespace" % index)
        if "\n" in line or "\r" in line:
            problems.append("line %d spans more than one line" % index)
        # One sentence per line, as the brief requires: the line must
        # end with a full stop and contain no ". " (period-space).
        if not line.endswith("."):
            problems.append("line %d does not end with a full stop" % index)
        if ". " in line:
            problems.append("line %d contains more than one sentence" % index)
        try:
            line.encode("utf-8")
        except UnicodeEncodeError:
            problems.append("line %d is not valid UTF-8" % index)
    return problems


def resolve_output(argv):
    """Pick the output path: argv[1], then $MAKEFUN_OUTPUT_DIR, then default."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, FILE_NAME)
    return DEFAULT_PATH


def write_entry(path, lines):
    """Write the lines as exact UTF-8 bytes (no trailing newline)."""
    problems = validate(lines)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = text_of(lines).encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    print(text_of(lines))
    print(
        "wrote %d lines / %d bytes to %s" % (len(lines), len(data), path)
    )
    return 0


def main(argv):
    return write_entry(resolve_output(argv), LINES)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
