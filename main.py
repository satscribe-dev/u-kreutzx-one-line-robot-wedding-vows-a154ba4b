#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of robot wedding vows to /output/entry.txt.
Deterministic, no network, no dependencies, no secrets.

The line (108 characters, ASCII only):
    I promise to love you in sickness and in health, in Wi-Fi and in
    airplane mode, till low battery do us part.
"""

import os
import sys

# The entry, as one named constant: setup (classic vow, verbatim) +
# parallel machine twist ("in Wi-Fi and in airplane mode") + punchline
# subverting the canonical closer ("till low battery do us part").
ENTRY = (
    "I promise to love you in sickness and in health, "
    "in Wi-Fi and in airplane mode, till low battery do us part."
)

# Gate from the competition rules: UTF-8 text, 1-160 chars, not only
# whitespace, a single line. Invalid = score 0, so fail loudly here
# instead of shipping a dead entry.
MIN_LEN = 1
MAX_LEN = 160


def validate_entry(text: str) -> None:
    """Raise SystemExit with a clear message if the entry fails the gate."""
    if not isinstance(text, str):
        sys.exit("gate FAIL: entry is not text")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        sys.exit("gate FAIL: entry is not valid UTF-8")
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        sys.exit(
            f"gate FAIL: entry is {len(text)} characters, "
            f"must be {MIN_LEN}-{MAX_LEN}"
        )
    if not text.strip():
        sys.exit("gate FAIL: entry is only whitespace")
    if "\n" in text or "\r" in text:
        sys.exit("gate FAIL: entry must be a single line")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
