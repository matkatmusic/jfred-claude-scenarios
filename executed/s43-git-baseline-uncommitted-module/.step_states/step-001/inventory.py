"""
Inventory module.

Items are dicts with at minimum: {"name": str, "price": float, "stock": int}.
A store is a list of items.
"""


def qty_chk(item, n):
    """Check whether `n` units of `item` are in stock.

    Args:
        item: Dict with a "stock" key.
        n: Requested quantity.

    Returns:
        True if stock >= n, False otherwise.
    """
    return n <= item["stock"]


def add_item(store, item):
    """Append `item` to `store`.

    Args:
        store: List of item dicts.
        item: Dict with at least "name", "price", "stock".

    Returns:
        None. Mutates store in place.
    """
    store.append(item)


def rm_item(store, name):
    """Remove the first item matching `name` from `store`.

    Args:
        store: List of item dicts.
        name: Name string to match against item["name"].

    Raises:
        ValueError: If no item with that name exists.
    """
    for i, item in enumerate(store):
        if item["name"] == name:
            store.pop(i)
            return
    raise ValueError(f"Item '{name}' not found")


def find_item(store, name):
    """Return the first item matching `name`, or None.

    Args:
        store: List of item dicts.
        name: Name string to match.

    Returns:
        The matching item dict, or None if not found.
    """
    for item in store:
        if item["name"] == name:
            return item
    return None


def tot_value(store):
    """Sum of price * stock for every item in `store`.

    Args:
        store: List of item dicts, each with "price" and "stock".

    Returns:
        Total inventory value as a float.
    """
    return sum(item["price"] * item["stock"] for item in store)


# ponytail: self-check, run with `python inventory.py`
if __name__ == "__main__":
    s = []
    add_item(s, {"name": "bolt", "price": 0.50, "stock": 200})
    add_item(s, {"name": "nut", "price": 0.25, "stock": 500})

    assert find_item(s, "bolt")["stock"] == 200
    assert find_item(s, "missing") is None
    assert qty_chk(s[0], 200) is True
    assert qty_chk(s[0], 201) is False
    assert tot_value(s) == 0.50 * 200 + 0.25 * 500

    rm_item(s, "bolt")
    assert len(s) == 1
    assert find_item(s, "bolt") is None

    try:
        rm_item(s, "ghost")
        assert False, "Should have raised"
    except ValueError:
        pass

    print("All checks passed.")
