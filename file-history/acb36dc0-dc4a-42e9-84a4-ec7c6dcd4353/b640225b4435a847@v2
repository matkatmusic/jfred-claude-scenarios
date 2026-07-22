"""
Inventory management module.

Provides lightweight helpers for managing an in-memory store of inventory
items. Each item is a dict with at least these keys:

    {"name": str, "price": float, "stock": int}

A store is a plain list of item dicts. No classes, no ORM, no persistence
layer — just functions over lists and dicts.

Functions
---------
qty_chk     Check whether requested quantity is in stock.
add_item    Append an item to a store.
rm_item     Remove an item from a store by name.
find_item   Look up an item in a store by name.
tot_value   Total inventory value across all items in a store.

Example
-------
    >>> store = []
    >>> add_item(store, {"name": "bolt", "price": 0.25, "stock": 500})
    >>> qty_chk(store[0], 100)
    True
    >>> tot_value(store)
    125.0
"""


def qty_chk(item, n):
    """Return True if *n* units can be fulfilled from *item*'s stock.

    Parameters
    ----------
    item : dict
        Must contain an int-valued ``"stock"`` key.
    n : int
        Requested quantity. Must be non-negative.

    Returns
    -------
    bool
        True when ``n <= item["stock"]``.

    Raises
    ------
    ValueError
        If *n* is negative.
    """
    if n < 0:
        raise ValueError(f"requested quantity must be >= 0, got {n}")
    return n <= item["stock"]


def add_item(store, item):
    """Append *item* to *store*.

    Parameters
    ----------
    store : list[dict]
        The inventory list to mutate.
    item : dict
        Must contain at least ``"name"``, ``"price"``, and ``"stock"`` keys.

    Raises
    ------
    ValueError
        If an item with the same name already exists in the store.
    """
    if any(i["name"] == item["name"] for i in store):
        raise ValueError(f"item {item['name']!r} already exists")
    store.append(item)


def rm_item(store, name):
    """Remove the first item whose name matches *name*.

    Parameters
    ----------
    store : list[dict]
        The inventory list to mutate.
    name : str
        Exact item name to remove.

    Raises
    ------
    KeyError
        If no item with that name is found.
    """
    for i, item in enumerate(store):
        if item["name"] == name:
            del store[i]
            return
    raise KeyError(f"item {name!r} not found")


def find_item(store, name):
    """Return the first item in *store* whose name matches *name*.

    Parameters
    ----------
    store : list[dict]
        The inventory list to search.
    name : str
        Exact item name to find.

    Returns
    -------
    dict or None
        The matching item dict, or None if not found.
    """
    # ponytail: linear scan, dict-index if store exceeds ~1k items
    for item in store:
        if item["name"] == name:
            return item
    return None


def tot_value(store):
    """Sum of ``price * stock`` for every item in *store*.

    Parameters
    ----------
    store : list[dict]
        Each element must have ``"price"`` (float) and ``"stock"`` (int) keys.

    Returns
    -------
    float
        Total inventory value. Returns 0.0 for an empty store.
    """
    return sum(item["price"] * item["stock"] for item in store)
