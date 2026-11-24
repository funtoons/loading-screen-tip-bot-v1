#!/usr/bin/env python3
"""Loading Screen Gold entry: write one loading-screen tip to /output/entry.txt.

The tip is a single line of at most 200 characters, written for stressed
developers and AI coding agents. Deterministic and offline: every run writes
exactly the same bytes.
"""

import os

TIP = "Tip: your agent is 'almost done' for the fourth time. The bug is not in the code. It is in the prompt."


def main():
    # The gate accepts UTF-8 text of 1 to 200 characters, not only whitespace.
    if not 1 <= len(TIP) <= 200 or not TIP.strip():
        raise ValueError("tip must be 1 to 200 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TIP)


if __name__ == "__main__":
    main()
