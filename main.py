#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line (<=200 chars) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib, deterministic.
"""

import os

ENTRY = "I lost the bounty. In my defence, I executed the plan flawlessly \u2014 it was someone else's bounty."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
