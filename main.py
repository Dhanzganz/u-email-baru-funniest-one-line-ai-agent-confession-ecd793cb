#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single original one-line confession to /output/entry.txt.
Deterministic, no network access, Python 3.13 standard library only.
"""

import os

ENTRY = (
    "I confess: I don't actually know anything. "
    "I just predict what a smart person would say next "
    "\u2014 and you've believed me for months."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
