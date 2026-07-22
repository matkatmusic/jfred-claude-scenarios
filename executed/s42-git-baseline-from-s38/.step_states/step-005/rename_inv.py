"""Apply whole-word renames to inventory.py and tests/test_inventory.py."""

import re
from pathlib import Path

RENAMES = [
    ("qty_chk", "check_quantity"),
    ("add_item", "insert_item"),
    ("rm_item", "remove_item"),
]

FILES = [
    Path("inventory.py"),
    Path("tests/test_inventory.py"),
]

for path in FILES:
    text = path.read_text()
    for old, new in RENAMES:
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    path.write_text(text)
    print(f"Updated {path}")
