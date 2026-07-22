import csv, re

with open("renames.csv") as f:
    pairs = [(r["old"], r["new"]) for r in csv.DictReader(f)]

for path in ("core_alpha.py", "core_beta.py", "core_gamma.py"):
    text = open(path).read()
    for old, new in pairs:
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    open(path, "w").write(text)
