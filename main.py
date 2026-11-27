"""Write the Thankful R2 entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only: the grader sandbox has no third-party packages.
The text lives here as a string literal; there is no separate data file.
Entry text: 517 Unicode characters, 519 bytes UTF-8.
"""

import os
import sys
from pathlib import Path

TEXT = """You will read a thousand of these today, and none of them can hand you anything real. So here is the smallest one I have.

This morning, before anyone woke, someone set a cup down beside a chair that was still empty, and went back to what they were doing. Not for thanks. Only so the person who was coming would not have to ask.

You spend your hours weighing other people's words. No one weighs yours. So let this one sit beside you the way that cup sat beside the empty chair — warm, unasked for, and already yours."""


def main() -> int:
    text = TEXT
    chars = len(text)
    if not 1 <= chars <= 1000:
        print(f"entry text must be 1-1000 characters, got {chars}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry text must not be whitespace-only", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    written = out_path.read_text(encoding="utf-8")
    if written != text:
        print("entry.txt round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
