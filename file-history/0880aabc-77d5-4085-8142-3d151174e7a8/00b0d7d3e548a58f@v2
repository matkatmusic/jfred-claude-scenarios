"""Whole-word rename of config_utils helpers across source and test files."""

import re

RENAMES = {
    r"\bget_val\b": "get_value",
    r"\bset_val\b": "set_value",
    r"\bdel_val\b": "delete_value",
}

FILES = ["config_utils.py", "tests/test_config_utils.py"]

for path in FILES:
    text = open(path).read()
    for pattern, replacement in RENAMES.items():
        text = re.sub(pattern, replacement, text)
    open(path, "w").write(text)
    print(f"renamed in {path}")
