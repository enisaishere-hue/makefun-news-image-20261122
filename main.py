#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261122.

Copies the poster image (entry.png, drawn for this entry) to the output
directory as entry.png. Standard library only, no network, deterministic:
the copied bytes are exactly the bytes in this repository.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    here = Path(__file__).resolve().parent
    if len(sys.argv) > 1:
        out_dir = Path(sys.argv[1])
    else:
        out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = here / "entry.png"
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if sha256_file(source) != sha256_file(target):
        print("error: copied entry.png does not match source", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
