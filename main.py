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
MAX_DIMENSION = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def png_dimensions(path: str) -> tuple[int, int]:
    """Read width/height from the PNG IHDR chunk (no Pillow needed)."""
    with open(path, "rb") as f:
        data = f.read(33)
    if len(data) < 33 or data[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file")
    if data[12:16] != b"IHDR":
        raise ValueError("PNG has no IHDR chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    return width, height


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")

    try:
        width, height = png_dimensions(src)
    except ValueError as exc:
        print(f"entry.png is not a valid PNG: {exc}", file=sys.stderr)
        return 1
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(
            f"entry.png is {width}x{height}, over the {MAX_DIMENSION}x"
            f"{MAX_DIMENSION} gate",
            file=sys.stderr,
        )
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
