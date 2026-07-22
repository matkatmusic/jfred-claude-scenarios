import re

RENAMES = [
    ("add_item", "insert_item"),
]

with open("inventory.py") as f:
    text = f.read()

for old, new in RENAMES:
    text = re.sub(rf"\b{re.escape(old)}\b", new, text)

with open("inventory.py", "w") as f:
    f.write(text)
