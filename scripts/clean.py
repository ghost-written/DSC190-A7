import csv
from datetime import datetime
from pathlib import Path

VALID_EVENT_TYPES = {"click", "login", "scroll", "view", "buy", "purchase"}

TIMESTAMP_FORMATS = [
    "%Y-%m-%dT%H:%M:%S.%f",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M:%S.%f",
    "%Y-%m-%d %H:%M:%S",
    "%m/%d/%Y %H:%M:%S",
]


def parse_timestamp(s):
    for fmt in TIMESTAMP_FORMATS:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def main():
    src = Path("data/raw/events.csv")
    dst = Path("data/clean/events.csv")
    dst.parent.mkdir(parents=True, exist_ok=True)

    with src.open(newline="") as f_in, dst.open("w", newline="") as f_out:
        reader = csv.DictReader(f_in)
        writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if any(v is None or v == "" for v in row.values()):
                continue
            if row["event_type"] not in VALID_EVENT_TYPES:
                continue
            try:
                duration = int(row["duration_seconds"])
            except ValueError:
                continue
            if duration <= 0:
                continue
            ts = parse_timestamp(row["timestamp"])
            if ts is None:
                continue
            row["timestamp"] = ts.strftime("%Y-%m-%dT%H:%M:%S")
            row["duration_seconds"] = str(duration)
            writer.writerow(row)


if __name__ == "__main__":
    main()
