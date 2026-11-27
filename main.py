import os
import sys
from pathlib import Path

TEXT = """One page after another, all day. Your eyes are tired in a way you have stopped noticing, and the room has gone quiet around you. This one will not ask anything of you.

Somewhere, someone set a glass of water beside a person working late. The water was never drunk. It sat there all evening, catching the light, doing nothing at all — except being there, in case it was wanted. That is the whole of it.

You already know what it costs to keep going when no one is watching. But the glass is still there. And the light is still on. And for a moment, before the next page, you can stop here a while, and breathe, and rest.

That is all this is. A small pause, left on the table for you."""


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")

    data = out_path.read_bytes()
    text = data.decode("utf-8")
    n = len(text)
    if not (1 <= n <= 1000):
        print(f"entry.txt has {n} characters, outside 1-1000", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt is whitespace-only", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({n} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
