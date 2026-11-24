#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of robot wedding vows to /output/entry.txt.
Deterministic, no network, no dependencies, no secrets.

The line (108 characters, ASCII only):
    I promise to love you in sickness and in health, in Wi-Fi and in
    airplane mode, till low battery do us part.
"""

import os

ENTRY = (
    "I promise to love you in sickness and in health, "
    "in Wi-Fi and in airplane mode, till low battery do us part."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
