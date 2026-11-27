"""Thankful R3 entry: writes the text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The text lives here as a string literal; the program copies it
to the output directory and validates length (1-1000 chars).
"""

import os
import sys
from pathlib import Path

TEXT = """You have read ten thousand sentences today. Every one of them wanted something from you — a verdict, a number, a yes or a no. None of them asked how your shoulders felt.

So here is a window, left open to the night air. No argument on the sill. No hurry in the dark beyond it. Just cool air coming in on its own, and the quiet of a house that has stopped asking.

You do not have to decide anything about this one. Let it sit beside you for a moment, the way evening settles beside a window. That is all it wants. That is all you have to give.
"""


def main() -> int:
    if not (1 <= len(TEXT) <= 1000):
        print(f"entry text is {len(TEXT)} chars, must be 1-1000", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry text is whitespace-only", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")
    written = out_path.read_text(encoding="utf-8")
    if written != TEXT:
        print("written entry.txt does not match the text", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(TEXT)} chars, {len(TEXT.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
