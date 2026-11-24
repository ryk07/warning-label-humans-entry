#!/usr/bin/env python3
"""Write one warning label for human beings to entry.txt.

The label is a single line in the voice of a printed safety warning:
a human agrees to plans, then cancels at the last minute blaming
"something came up" -- and the twist, landing in the last few words,
is that the something is the couch. Universally true, label-shaped,
and the laugh arrives only at the end.
"""

import os
from pathlib import Path

LABEL = (
    "CAUTION: This human may agree to plans, then cancel at the last "
    "minute citing 'something came up'. That something is the couch."
)


def output_dir() -> Path:
    """Resolve the output directory without ever trusting the cwd."""
    here = Path(__file__).resolve().parent
    _ = here
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    text = LABEL.strip()
    if not text or len(text) > 160 or "\n" in text or "\r" in text:
        raise ValueError("label must be a single line of 1-160 characters")
    out_path = output_dir() / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
