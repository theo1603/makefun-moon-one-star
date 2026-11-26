"""The Moon Gets One Star - make.fun entry.

Writes exactly one line: the funniest one-star review of the Moon.
Python 3.13, stdlib only, no network, fully deterministic.
"""

import os
from pathlib import Path

REVIEW = (
    "One star. It moved the entire ocean onto my picnic, then ghosted "
    "me for a fortnight. Zero accountability."
)

OUTPUT_PATH = Path(
    os.environ.get("ENTRY_OUTPUT")
    or os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
