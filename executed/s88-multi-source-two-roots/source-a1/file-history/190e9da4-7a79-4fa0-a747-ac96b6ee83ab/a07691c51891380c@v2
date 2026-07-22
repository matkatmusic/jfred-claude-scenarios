"""Dict-based inventory module.

Stores items as dicts with at least 'name' and 'stock' keys
in a list-based store.
"""


def add_item(store, item):
    """Append an item dict to the store list."""
    store.append(item)


def qty_chk(item, n):
    """Return True if item has at least n units in stock."""
    return n <= item["stock"]


def find_item(store, name):
    """Return the first item matching name, or None."""
    for item in store:
        if item["name"] == name:
            return item
    return None
