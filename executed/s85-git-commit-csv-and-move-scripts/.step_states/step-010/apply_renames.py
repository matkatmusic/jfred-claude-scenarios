"""Read renames.csv and apply whole-word substitutions across core_*.py files."""
import csv, re, glob

with open("renames.csv") as f:
    pairs = [(r["old"], r["new"]) for r in csv.DictReader(f)]

for path in sorted(glob.glob("core_*.py")):
    text = open(path).read()
    for old, new in pairs:
        if re.search(rf"\b{re.escape(old)}\b", text):
            print(f"{path}: {old} -> {new}")
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    open(path, "w").write(text)
