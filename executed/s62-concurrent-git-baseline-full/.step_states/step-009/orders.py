"""Order processing utilities."""


def total(items):
    """Sum the 'price' of each item."""
    return sum(item["price"] for item in items)


def count(items):
    """Return the number of items."""
    return len(items)


def cheapest(items):
    """Return the item with the lowest price."""
    return min(items, key=lambda item: item["price"])
