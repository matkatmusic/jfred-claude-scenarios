"""Apply whole-word renames from scoped_renames.csv."""

import csv
import re
from pathlib import Path

ALL_FILES = ["catalog.py", "catalog_view.py", "tests/test_catalog.py"]


def apply_rename(old, new, files):
    pattern = re.compile(r"\b" + re.escape(old) + r"\b")
    for fp in files:
        p = Path(fp)
        if not p.exists():
            continue
        text = p.read_text()
        updated = pattern.sub(new, text)
        if updated != text:
            p.write_text(updated)
            print(f"  {fp}: renamed {old} -> {new}")


with open("scoped_renames.csv", newline="") as f:
    for row in csv.DictReader(f):
        old, new = row["old"], row["new"]
        exported = row["isExported"].strip().upper() == "Y"
        scope_file = row["file"].strip()

        if exported:
            targets = ALL_FILES
        else:
            targets = [scope_file] if scope_file else []

        print(f"Renaming '{old}' -> '{new}' ({'global' if exported else scope_file})")
        apply_rename(old, new, targets)
