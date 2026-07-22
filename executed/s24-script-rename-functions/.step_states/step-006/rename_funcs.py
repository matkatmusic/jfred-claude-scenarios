"""Whole-word rename of terse function names in order_utils.py."""
import re

RENAMES = {
    "calc_tot": "calculate_total",
    "fmt_money": "format_currency",
    "chk_stock": "check_stock",
    "mk_order": "build_order",
    "apply_disc": "apply_discount",
}

path = "order_utils.py"
text = open(path).read()

for old, new in RENAMES.items():
    text = re.sub(rf"\b{old}\b", new, text)

open(path, "w").write(text)
print("Done — renames applied.")
