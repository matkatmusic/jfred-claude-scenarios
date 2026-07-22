import csv
import re

FILES = ["textutil.py", "tests/test_textutil.py"]

with open("many_renames.csv") as f:
    renames = list(csv.DictReader(f))

ok = 0
for row in renames:
    old, new = row["old"], row["new"]
    pattern = re.compile(r"\b" + re.escape(old) + r"\b")
    for path in FILES:
        with open(path) as f:
            text = f.read()
        text = pattern.sub(new, text)
        with open(path, "w") as f:
            f.write(text)
    print(f"OK {old} -> {new}")
    ok += 1

print(f"{ok} OK")
