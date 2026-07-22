"""Simple inventory tracking."""


def add_item(items, name, qty):
    """Append an item dict with 'name' and 'qty' keys, return the list."""
    items.append({"name": name, "qty": qty})
    return items


def find_item(items, name):
    """Return the first item matching 'name', or None."""
    return next((item for item in items if item["name"] == name), None)


def remove_item(items, name):
    """Remove the first item matching 'name' and return the list."""
    item = find_item(items, name)
    if item is not None:
        items.remove(item)
    return items


def restock(items, name, qty):
    """Increase the matching item's 'qty' by 'qty'."""
    item = find_item(items, name)
    if item is not None:
        item["qty"] += qty


def total_qty(items):
    """Return the sum of every item's 'qty'."""
    return sum(item["qty"] for item in items)
