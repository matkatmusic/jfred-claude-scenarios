"""Walk the tree, skip 'vendor' dirs, whole-word rename compute_value → compute_value."""

import os
import re

PATTERN = re.compile(r"\bhelper\b")

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d != "vendor"]
    for fname in files:
        if not fname.endswith(".py"):
            continue
        path = os.path.join(root, fname)
        text = open(path).read()
        new_text = PATTERN.sub("compute_value", text)
        if new_text != text:
            open(path, "w").write(new_text)
            print(f"renamed: {path}")
