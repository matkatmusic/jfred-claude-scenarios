"""
Inventory management module.

Provides helpers for managing a store's inventory — a list of item dicts.
Each item is a dict with at least: {"name": str, "price": float, "stock": int}.

Functions:
    qty_chk    — check whether requested quantity is in stock
    add_item   — append an item to the store
    rm_item    — remove an item by name
    find_item  — look up an item by name
    tot_value  — total inventory value (price * stock across all items)
"""


def qty_chk(item, n):
    """Return True if item has at least n units in stock.

    Args:
        item: dict with a "stock" key (int).
        n: requested quantity (int).

    Returns:
        bool: True when item["stock"] >= n.

    Raises:
        KeyError: if item has no "stock" key.
        TypeError: if n is not comparable to an int.
    """
    return item["stock"] >= n


def add_item(store, item):
    """Append an item dict to the store list.

    Args:
        store: list of item dicts.
        item: dict with at least "name", "price", "stock".

    Returns:
        None — mutates store in place.

    Raises:
        ValueError: if an item with the same name already exists.
    """
    if any(existing["name"] == item["name"] for existing in store):
        raise ValueError(f"Item '{item['name']}' already exists")
    store.append(item)


def rm_item(store, name):
    """Remove the first item matching name from the store.

    Args:
        store: list of item dicts.
        name: string name to match against item["name"].

    Returns:
        The removed item dict.

    Raises:
        KeyError: if no item with that name exists.
    """
    for i, item in enumerate(store):
        if item["name"] == name:
            return store.pop(i)
    raise KeyError(f"Item '{name}' not found")


def find_item(store, name):
    """Return the first item whose name matches, or None.

    Args:
        store: list of item dicts.
        name: string name to match.

    Returns:
        The matching item dict, or None if not found.
    """
    for item in store:
        if item["name"] == name:
            return item
    return None


def tot_value(store):
    """Sum of price * stock for every item in the store.

    Args:
        store: list of item dicts, each with "price" and "stock".

    Returns:
        float: total inventory value.

    Raises:
        KeyError: if any item is missing "price" or "stock".
    """
    return sum(item["price"] * item["stock"] for item in store)


if __name__ == "__main__":
    # ponytail: inline smoke test, no framework needed
    store = []
    add_item(store, {"name": "widget", "price": 2.50, "stock": 100})
    add_item(store, {"name": "gadget", "price": 15.00, "stock": 20})

    assert find_item(store, "widget")["stock"] == 100
    assert find_item(store, "missing") is None
    assert qty_chk(store[0], 50) is True
    assert qty_chk(store[0], 200) is False
    assert tot_value(store) == 2.50 * 100 + 15.00 * 20

    removed = rm_item(store, "widget")
    assert removed["name"] == "widget"
    assert len(store) == 1
    assert tot_value(store) == 300.00

    try:
        rm_item(store, "widget")
        assert False, "should have raised"
    except KeyError:
        pass

    try:
        add_item(store, {"name": "gadget", "price": 1.0, "stock": 1})
        assert False, "should have raised"
    except ValueError:
        pass

    print("all checks passed")
