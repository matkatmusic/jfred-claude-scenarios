"""Dict-based inventory module.

Stores items as dicts with at least 'name' and 'stock' keys
in a list-based store.
"""


def insert_item(store, item):
    """Append an item dict to the store list."""
    store.append(item)


def check_quantity(item, n):
    """Return True if item has at least n units in stock."""
    return n <= item["stock"]


def lookup_item(store, name):
    """Return the first item matching name, or None."""
    for item in store:
        if item["name"] == name:
            return item
    return None


def restock(store, name, n):
    """Restock an item by name, adding n units.

    If the item exists and check_quantity shows stock < n, increase stock to n.
    If the item does not exist, insert a new item with stock set to n.
    """
    item = lookup_item(store, name)
    if item is None:
        insert_item(store, {"name": name, "stock": n})
    elif not check_quantity(item, n):
        item["stock"] = n
# reviewed by ops
