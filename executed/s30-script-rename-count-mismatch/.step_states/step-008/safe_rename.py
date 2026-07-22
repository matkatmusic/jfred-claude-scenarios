"""Read count_renames.csv, verify counts, apply safe whole-word renames."""

import csv
import re
from pathlib import Path

CSV = Path("count_renames.csv")
TARGETS = [Path("pricing.py"), Path("tests/test_pricing.py")]


def count_whole_word(text: str, word: str) -> int:
    return len(re.findall(rf"\b{re.escape(word)}\b", text))


rows = list(csv.DictReader(CSV.open()))
source = TARGETS[0].read_text()

approved = []
for row in rows:
    old, expected = row["old"], int(row["count"])
    actual = count_whole_word(source, old)
    if actual != expected:
        print(f"MISMATCH: '{old}' expected {expected}, found {actual} — skipping")
    else:
        approved.append((old, row["new"]))

for path in TARGETS:
    text = path.read_text()
    for old, new in approved:
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    path.write_text(text)
    print(f"wrote {path}")
