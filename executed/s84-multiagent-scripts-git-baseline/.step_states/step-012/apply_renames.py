import csv, re

with open("renames.csv") as f:
    pairs = list(csv.DictReader(f))

text = open("core_inventory.py").read()
for p in pairs:
    print(f"{p['old']} -> {p['new']}")
    text = re.sub(rf"\b{p['old']}\b", p["new"], text)
open("core_inventory.py", "w").write(text)
