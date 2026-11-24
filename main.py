"""news-image-20261124: sum up 24 November 2026's world news in one image.

Deterministic, offline, standard library only.
Writes the bundled image (asset/entry.png, rendered by render.py)
to /output/entry.png, byte for byte.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSET = HERE / "asset" / "entry.png"
OUTPUT = Path("/output") / "entry.png"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)
    # Fail loudly instead of shipping a truncated file.
    if OUTPUT.stat().st_size != ASSET.stat().st_size:
        raise RuntimeError("output size does not match bundled image")


if __name__ == "__main__":
    main()
