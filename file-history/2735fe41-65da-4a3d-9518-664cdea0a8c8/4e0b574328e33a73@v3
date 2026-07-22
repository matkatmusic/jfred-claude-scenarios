"""Inventory helpers — add items and tally quantities."""


def add_item(items, name, qty):
    """Append an item dict with *name* and *qty* to *items* and return the list."""
    items.append({"name": name, "qty": qty})
    return items


def find_item(items, name):
    """Return the first item whose ``name`` matches, or ``None``."""
    return next((item for item in items if item["name"] == name), None)


def total_qty(items):
    """Return the sum of every item's ``qty``."""
    return sum(item["qty"] for item in items)
