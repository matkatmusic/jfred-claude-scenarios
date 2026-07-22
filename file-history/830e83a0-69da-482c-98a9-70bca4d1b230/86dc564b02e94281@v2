"""Simple inventory tracking."""


def add_item(items, name, qty):
    """Append an item dict with 'name' and 'qty' keys, return the list."""
    items.append({"name": name, "qty": qty})
    return items


def total_qty(items):
    """Return the sum of every item's 'qty'."""
    return sum(item["qty"] for item in items)
