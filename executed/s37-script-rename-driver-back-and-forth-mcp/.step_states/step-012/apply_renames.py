import csv
import re

TARGETS = ["ledger.py", "tests/test_ledger.py"]

with open("renames.csv") as f:
    renames = list(csv.DictReader(f))

for path in TARGETS:
    text = open(path).read()
    for row in renames:
        text = re.sub(rf"\b{re.escape(row['old'])}\b", row["new"], text)
    open(path, "w").write(text)
