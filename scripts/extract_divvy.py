"""Download one month of Divvy trip data and unzip the CSV into data/.

Usage:
    python scripts/extract_divvy.py 2024 6      # June 2024
    python scripts/extract_divvy.py 2024 6 --out-dir some/folder

By default the CSV lands in data/raw/ (ignored by git, so raw data is
never pushed).
"""

import argparse
import sys
import urllib.request
import zipfile
from pathlib import Path

BASE_URL = "https://divvy-tripdata.s3.amazonaws.com"
DEFAULT_RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def download_month(year: int, month: int, raw_dir: Path = DEFAULT_RAW_DIR) -> Path:
    """Download and extract one monthly file. Returns the CSV path."""
    name = f"{year}{month:02d}-divvy-tripdata"
    url = f"{BASE_URL}/{name}.zip"
    raw_dir.mkdir(parents=True, exist_ok=True)
    zip_path = raw_dir / f"{name}.zip"

    print(f"Downloading {url}")
    urllib.request.urlretrieve(url, zip_path)

    with zipfile.ZipFile(zip_path) as zf:
        # Keep only the trip CSV; skip macOS metadata folders in the zip.
        csv_members = [
            m for m in zf.namelist()
            if m.endswith(".csv") and not m.startswith("__MACOSX")
        ]
        if not csv_members:
            sys.exit(f"No CSV found in {zip_path.name}")
        zf.extract(csv_members[0], raw_dir)
        csv_path = raw_dir / csv_members[0]

    zip_path.unlink()  # keep only the CSV
    print(f"Saved {csv_path}")
    return csv_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("year", type=int, help="e.g. 2024")
    parser.add_argument("month", type=int, choices=range(1, 13), help="1-12")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_RAW_DIR,
                        help="folder for the CSV (default: data/raw)")
    args = parser.parse_args()
    download_month(args.year, args.month, args.out_dir)


if __name__ == "__main__":
    main()
