import csv
from datetime import datetime
from pathlib import Path


def main():
    src = Path("data/transformed/events.csv")
    dst = Path("data/features/events.csv")
    dst.parent.mkdir(parents=True, exist_ok=True)

    with src.open(newline="") as f_in, dst.open("w", newline="") as f_out:
        reader = csv.DictReader(f_in)
        fieldnames = list(reader.fieldnames) + ["duration_minutes", "weekday"]
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            row["duration_minutes"] = str(int(row["duration_seconds"]) / 60)
            row["weekday"] = datetime.strptime(row["date"], "%Y-%m-%d").strftime("%A")
            writer.writerow(row)


if __name__ == "__main__":
    main()
