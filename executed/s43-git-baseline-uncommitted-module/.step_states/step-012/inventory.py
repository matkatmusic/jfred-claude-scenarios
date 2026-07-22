"""
Inventory module.

Items are dicts with at minimum: {"name": str, "price": float, "stock": int}.
A store is a list of items.
"""


def check_quantity(item, n):
    """Check whether `n` units of `item` are in stock.

    Args:
        item: Dict with a "stock" key.
        n: Requested quantity.

    Returns:
        True if stock >= n, False otherwise.
    """
    return n <= item["stock"]


def insert_item(store, item):
    """Append `item` to `store`.

    Args:
        store: List of item dicts.
        item: Dict with at least "name", "price", "stock".

    Returns:
        None. Mutates store in place.
    """
    store.append(item)


def remove_item(store, name):
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


def restock(store, name, n):
    """Add `n` units to item `name`, or insert it if missing.

    Uses check_quantity to decide whether restocking is needed,
    and insert_item to add a new entry when the item doesn't exist.

    Args:
        store: List of item dicts.
        name: Item name to restock.
        n: Units to add (or initial stock if new).

    Returns:
        True if stock was added, False if already sufficient.
    """
    item = find_item(store, name)
    if item is None:
        insert_item(store, {"name": name, "price": 0.0, "stock": n})
        return True
    if check_quantity(item, n):
        return False
    item["stock"] += n
    return True


def reorder(store, name, n):
    """Reorder `n` units of `name` if stock is insufficient."""
    item = find_item(store, name)
    if item and check_quantity(item, n):
        return False
    insert_item(store, {"name": name, "price": 0.0, "stock": n})
    return True


def low_stock(store, threshold):
    """Return items whose stock is below `threshold`.

    Args:
        store: List of item dicts.
        threshold: Stock level cutoff (exclusive).

    Returns:
        List of items where stock < threshold.
    """
    return [item for item in store if item["stock"] < threshold]


# ponytail: self-check, run with `python inventory.py`
if __name__ == "__main__":
    s = []
    insert_item(s, {"name": "bolt", "price": 0.50, "stock": 200})
    insert_item(s, {"name": "nut", "price": 0.25, "stock": 500})

    assert find_item(s, "bolt")["stock"] == 200
    assert find_item(s, "missing") is None
    assert check_quantity(s[0], 200) is True
    assert check_quantity(s[0], 201) is False
    assert tot_value(s) == 0.50 * 200 + 0.25 * 500

    remove_item(s, "bolt")
    assert len(s) == 1
    assert find_item(s, "bolt") is None

    try:
        remove_item(s, "ghost")
        assert False, "Should have raised"
    except ValueError:
        pass

    r = []
    assert reorder(r, "washer", 10) is True
    assert len(r) == 1 and r[0]["stock"] == 10
    assert reorder(r, "washer", 5) is False  # already have 10

    print("All checks passed.")
# reviewed by ops
