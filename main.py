#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261122.

Copies the poster image (entry.png, drawn for this entry) to the output
directory as entry.png. Standard library only, no network, deterministic:
the copied bytes are exactly the bytes in this repository.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    if len(sys.argv) > 1:
        out_dir = Path(sys.argv[1])
    else:
        out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
