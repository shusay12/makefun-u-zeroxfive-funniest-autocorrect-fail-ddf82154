#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry program.

Writes a single line (1-199 characters) to /output/entry.txt.
Python 3.13 stdlib only, no network, deterministic output.
"""

import os

ENTRY = (
    "I texted my wife 'grab chicken for dinner' \u2014 autocorrect "
    "sent 'grab children for dinner' and now the police are at my door."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 199, f"entry length {len(text)} outside 1-199"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
