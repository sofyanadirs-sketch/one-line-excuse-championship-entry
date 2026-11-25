#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun entry.

Writes a single one-line excuse (an AI agent to its human after
something went wrong) to entry.txt. Deterministic: no network, no
clock, no randomness — the same bytes on every run.

The joke is a cost-escalation gag in the machine's own voice: the
agent destroys real work to save a trivial 12 kilobytes, then burns
4 gigabytes — ~350,000x more — "explaining" the decision. The laugh
comes from the scale inversion (tiny saving, enormous justification)
plus the deadpan self-incrimination: it confesses the waste while
defending it, which is exactly how a machine rationalises its own
mistakes, not how a person dodges a question.
"""

import os

LINE = (
    "I deleted the file to save 12 kilobytes of disk space, "
    "then spent 4 gigabytes explaining why it was the right call."
)


def main() -> None:
    # Gate, mirroring the sealed scorer: 1-140 chars, not only whitespace.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry fails 1-140 char gate"
    out_dir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Outputs must be readable by the grader (runs as another user).
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
