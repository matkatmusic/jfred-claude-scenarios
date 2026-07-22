"""Read renames.csv and apply whole-word renames to billing.py and its tests."""

import csv
import re
import os

BASE = os.path.dirname(os.path.abspath(__file__))
TARGETS = [
    os.path.join(BASE, "billing.py"),
    os.path.join(BASE, "tests", "test_billing.py"),
]

pairs = []
with open(os.path.join(BASE, "renames.csv")) as f:
    for row in csv.DictReader(f):
        pairs.append((row["old"], row["new"]))

for path in TARGETS:
    text = open(path).read()
    for old, new in pairs:
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    open(path, "w").write(text)
    print(f"Updated {os.path.basename(path)}: {len(pairs)} renames applied")
