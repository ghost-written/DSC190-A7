import csv
from pathlib import Path


def main():
    src = Path("data/clean/events.csv")
    dst = Path("data/transformed/events.csv")
    dst.parent.mkdir(parents=True, exist_ok=True)

    with src.open(newline="") as f_in, dst.open("w", newline="") as f_out:
        reader = csv.DictReader(f_in)
        fieldnames = list(reader.fieldnames) + ["date"]
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            row["date"] = row["timestamp"][:10]
            writer.writerow(row)


if __name__ == "__main__":
    main()
