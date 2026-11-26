#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest -- make.fun entry.

Writes a single museum-placard line (at most 180 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "Sticky note, c. 2004. Paper, weak adhesive. Stuck to a monitor's edge, "
    "it bore the tribe's highest law: 'DO NOT TURN OFF \u2014 JENNY'. "
    "Gift of the IT department."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
