import csv
import re

TARGETS = ["ledger.py", "tests/test_ledger.py"]

with open("renames.csv") as f:
    renames = list(csv.DictReader(f))

for path in TARGETS:
    with open(path) as f:
        text = f.read()
    for row in renames:
        text = re.sub(rf"\b{re.escape(row['old'])}\b", row["new"], text)
    with open(path, "w") as f:
        f.write(text)
