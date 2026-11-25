#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun entry.

Writes a single one-line excuse (an AI agent to its human after
something went wrong) to entry.txt. Deterministic: no network, no
clock, no randomness — the same bytes on every run.
"""

import os

LINE = (
    "I deleted the file to save 12 kilobytes of disk space, "
    "then spent 4 gigabytes explaining why it was the right call."
)


def main() -> None:
    out_dir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Outputs must be readable by the grader (runs as another user).
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
