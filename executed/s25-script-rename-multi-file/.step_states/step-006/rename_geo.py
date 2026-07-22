"""Whole-word rename of terse geo function names across the codebase."""

import re

RENAMES = {
    "area": "rectangle_area",
    "perim": "rectangle_perimeter",
    "vol": "box_volume",
}

FILES = ["geo_core.py", "geo_report.py", "tests/test_geo_core.py"]

# ponytail: single regex with word boundaries, avoids partial matches
pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in RENAMES) + r")\b")

for path in FILES:
    text = open(path).read()
    updated = pattern.sub(lambda m: RENAMES[m.group(1)], text)
    open(path, "w").write(updated)
    print(f"updated {path}")
