"""Apply whole-word renames from renames.csv across core_*.py files."""
import csv, re, glob

with open("renames.csv") as f:
    pairs = [(r["old"], r["new"]) for r in csv.DictReader(f)]

for path in sorted(glob.glob("core_*.py")):
    text = open(path).read()
    for old, new in pairs:
        count = len(re.findall(rf"\b{re.escape(old)}\b", text))
        if count:
            text = re.sub(rf"\b{re.escape(old)}\b", new, text)
            print(f"  {old} -> {new} ({count} occurrence(s))")
    open(path, "w").write(text)
    print(f"updated {path}")
