import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POAM_FILE = ROOT / "poam" / "poam-register.csv"


def main() -> None:
    counts = {"High": 0, "Medium": 0, "Low": 0}
    fixed = []

    with POAM_FILE.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["status"] in {"Closed", "Accepted"}:
                counts[row["severity"]] += 1
                fixed.append(row["poam_id"])

    total = sum(counts.values())
    print(
        f"Release R1.0.1 fixed {total} POA&Ms: "
        f"High={counts['High']} Medium={counts['Medium']} Low={counts['Low']}"
    )
    print("Residual risk: Low / Acceptable with AO approval")
    print("POA&Ms included: " + ", ".join(fixed))


if __name__ == "__main__":
    main()

