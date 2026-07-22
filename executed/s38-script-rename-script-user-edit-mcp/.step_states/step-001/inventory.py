"""
Inventory management module.

Provides lightweight helpers for managing an in-memory store of inventory
items. Each item is a plain dict with at least these keys:

    {
        "name":  str,   # unique identifier
        "price": float, # unit price
        "stock": int,   # quantity on hand
    }

A store is a list of such dicts. No database, no ORM, no classes — just
lists and dicts.

Functions
---------
qty_chk   -- check whether requested quantity is in stock
add_item  -- append an item to a store
rm_item   -- remove an item from a store by name
find_item -- look up an item by name
tot_value -- total inventory value across all items
"""


def qty_chk(item, n):
    """Check whether *n* units of *item* are available.

    Args:
        item: dict with at least a ``"stock"`` key (int).
        n:    requested quantity.

    Returns:
        True if the current stock is >= *n*, False otherwise.

    Examples:
        >>> qty_chk({"name": "bolt", "stock": 50}, 10)
        True
        >>> qty_chk({"name": "bolt", "stock": 3}, 10)
        False
    """
    return n <= item["stock"]


def add_item(store, item):
    """Append *item* to *store*.

    Args:
        store: list of item dicts (mutated in place).
        item:  dict to add — must contain ``"name"``, ``"price"``,
               and ``"stock"`` keys at minimum.

    Returns:
        None.  *store* is mutated in place.

    Examples:
        >>> s = []
        >>> add_item(s, {"name": "nut", "price": 0.10, "stock": 200})
        >>> len(s)
        1
    """
    store.append(item)


def rm_item(store, name):
    """Remove the first item whose ``"name"`` matches *name*.

    Args:
        store: list of item dicts (mutated in place).
        name:  string to match against each item's ``"name"`` key.

    Returns:
        The removed item dict, or None if no match was found.

    Examples:
        >>> s = [{"name": "nut", "price": 0.10, "stock": 200}]
        >>> rm_item(s, "nut")
        {'name': 'nut', 'price': 0.1, 'stock': 200}
        >>> s
        []
    """
    for i, item in enumerate(store):
        if item["name"] == name:
            return store.pop(i)
    return None


def find_item(store, name):
    """Return the first item in *store* whose ``"name"`` equals *name*.

    Args:
        store: list of item dicts.
        name:  string to match.

    Returns:
        The matching item dict, or None if not found.

    Examples:
        >>> s = [{"name": "bolt", "price": 0.50, "stock": 100}]
        >>> find_item(s, "bolt")["price"]
        0.5
        >>> find_item(s, "missing") is None
        True
    """
    for item in store:
        if item["name"] == name:
            return item
    return None


def tot_value(store):
    """Sum of ``price * stock`` for every item in *store*.

    Args:
        store: list of item dicts, each with ``"price"`` and ``"stock"``.

    Returns:
        float — total inventory value.  Returns 0 for an empty store.

    Examples:
        >>> tot_value([{"price": 2.0, "stock": 5}, {"price": 1.0, "stock": 10}])
        20.0
    """
    return sum(item["price"] * item["stock"] for item in store)
