"""Two Lines to Your Past Self — make.fun entry.

Deterministic, no network, no randomness: writes one fixed two-line
entry to /output/entry.txt.
"""

import os

ENTRY = (
    "Don't co-sign your cousin's motorbike loan outside the bank on 12 June.\n"
    "His three missed payments became your debt, and you spent two years "
    "paying for a bike you never rode.\n"
)


def main() -> None:
    # Self-check the competition gate before writing: exactly two
    # non-empty lines, total at most 280 characters (output unchanged).
    lines = ENTRY.split("\n")
    assert len(lines) == 3 and lines[2] == "", "entry must be exactly two lines"
    assert all(line.strip() for line in lines[:2]), "each line must be non-empty"
    assert len(ENTRY) <= 280, "entry must be at most 280 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
