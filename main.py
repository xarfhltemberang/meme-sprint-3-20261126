#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — entry program.

Writes the pre-rendered meme image (entry.png, shipped in this repo) to
/output/entry.png. Deterministic: the same file is copied on every run.

Stdlib only — the grader runs Python 3.13 slim with no Pillow.
"""

import os
import shutil
import sys

# Gate limits from the competition kit: at most 1 MiB, at most 1024x1024 px.
MAX_BYTES = 1_048_576
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")

    with open(src, "rb") as f:
        header = f.read(len(PNG_SIGNATURE))
    if header != PNG_SIGNATURE:
        print("entry.png is not a valid PNG", file=sys.stderr)
        return 1

    size = os.path.getsize(src)
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB gate", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)

    written = os.path.getsize(dst)
    print(f"wrote {dst} ({written} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
