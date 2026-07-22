"""Apply whole-word renames to inventory.py and tests/test_inventory.py."""

import re

RENAMES = [
    ("qty_chk", "check_quantity"),
    ("add_item", "insert_item"),
]

FILES = ["inventory.py", "tests/test_inventory.py"]

for path in FILES:
    text = open(path).read()
    for old, new in RENAMES:
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    open(path, "w").write(text)
