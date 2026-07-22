"""
Inventory management module.

Manages a store inventory represented as a list of item dicts.
Each item dict must have: {"name": str, "price": float, "stock": int}.

Usage:
    store = []
    insert_item(store, {"name": "Widget", "price": 9.99, "stock": 50})
    find_item(store, "Widget")  # -> {"name": "Widget", ...}
    tot_value(store)            # -> 499.5
"""


def check_quantity(item, n):
    """Check if requested quantity is available in stock.

    Args:
        item: Item dict with at least a "stock" key.
        n: Quantity requested.

    Returns:
        True if n units are available (n <= stock), False otherwise.

    Examples:
        >>> check_quantity({"name": "Bolt", "stock": 10}, 5)
        True
        >>> check_quantity({"name": "Bolt", "stock": 10}, 15)
        False
    """
    return n <= item["stock"]


def insert_item(store, item):
    """Append an item to the store inventory.

    Args:
        store: List of item dicts (modified in place).
        item: Dict with "name", "price", and "stock" keys.

    Examples:
        >>> store = []
        >>> insert_item(store, {"name": "Nail", "price": 0.10, "stock": 1000})
        >>> len(store)
        1
    """
    store.append(item)


def remove_item(store, name):
    """Remove an item from the store by name.

    Args:
        store: List of item dicts (modified in place).
        name: Name of the item to remove.

    Raises:
        ValueError: If no item with the given name exists.

    Examples:
        >>> store = [{"name": "Bolt", "price": 1.0, "stock": 5}]
        >>> remove_item(store, "Bolt")
        >>> len(store)
        0
    """
    item = find_item(store, name)
    if item is None:
        raise ValueError(f"Item '{name}' not found")
    store.remove(item)


def find_item(store, name):
    """Find and return an item by name.

    Args:
        store: List of item dicts.
        name: Name to search for.

    Returns:
        The matching item dict, or None if not found.

    Examples:
        >>> store = [{"name": "Gear", "price": 5.0, "stock": 20}]
        >>> find_item(store, "Gear")["price"]
        5.0
        >>> find_item(store, "Missing") is None
        True
    """
    # ponytail: linear scan, dict lookup if store grows past hundreds
    for item in store:
        if item["name"] == name:
            return item
    return None


def restock(store, name, n):
    """Ensure at least n units of an item are in stock.

    If the item doesn't exist, inserts it with stock=n and price=0.
    If it exists but stock < n, sets stock to n. No-op if already sufficient.

    Args:
        store: List of item dicts (modified in place).
        name: Item name.
        n: Minimum stock level to guarantee.
    """
    item = find_item(store, name)
    if item is None:
        insert_item(store, {"name": name, "price": 0.0, "stock": n})
        return
    if not check_quantity(item, n):
        item["stock"] = n


def tot_value(store):
    """Calculate total inventory value (sum of price * stock for all items).

    Args:
        store: List of item dicts with "price" and "stock" keys.

    Returns:
        Total value as a float.

    Examples:
        >>> store = [
        ...     {"name": "A", "price": 10.0, "stock": 3},
        ...     {"name": "B", "price": 5.0, "stock": 4},
        ... ]
        >>> tot_value(store)
        50.0
    """
    return sum(item["price"] * item["stock"] for item in store)


if __name__ == "__main__":
    store = []
    insert_item(store, {"name": "Widget", "price": 9.99, "stock": 50})
    insert_item(store, {"name": "Gadget", "price": 24.99, "stock": 10})
    insert_item(store, {"name": "Gizmo", "price": 4.50, "stock": 200})

    assert find_item(store, "Widget")["price"] == 9.99
    assert find_item(store, "Nope") is None

    assert check_quantity(find_item(store, "Widget"), 50) is True
    assert check_quantity(find_item(store, "Widget"), 51) is False

    assert tot_value(store) == (9.99 * 50) + (24.99 * 10) + (4.50 * 200)

    remove_item(store, "Gadget")
    assert len(store) == 2
    assert find_item(store, "Gadget") is None

    print("All checks passed.")
