import csv
import json
from pathlib import Path

# Paths
ROOT = Path(__file__).parent
json_path = ROOT / "malayalam.json"
out_path = ROOT / "malayalam_data.csv"

# Configuration for new language entries
# LANG_CODE = "ML"  # ISO 639-1 for Malayalam
# SETTING = "one_shot"
# LABEL = 0  # 0 = idiomatic/non-literal in SubTask A convention


def main() -> None:
    with json_path.open(encoding="utf-8") as f:
        items = json.load(f)

    # Build rows matching SubTask A schema
    rows = []
    for idx, item in enumerate(items, start=1):
        data_id = f"ML.{idx:03d}.1"
        target_sentence = item.get("example", "").strip()
        rows.append(
            [
                data_id,
                "ML",
                item.get("idiom", "").strip(),
                "",  # Previous context unavailable
                target_sentence,
                "",  # Next context unavailable
            ]
        )

    # Write CSV
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["DataID", "Language", "MWE", "Previous", "Target", "Next"])
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out_path}")

if __name__ == "__main__":
    main()
