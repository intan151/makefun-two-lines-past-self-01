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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
