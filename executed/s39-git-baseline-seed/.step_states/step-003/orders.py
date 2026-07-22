"""Order utilities for extracting totals and names from item lists."""


def total(items):
    """Return the sum of each item's 'price'."""
    return sum(item["price"] for item in items)


def names(items):
    """Return a list of each item's 'name'."""
    return [item["name"] for item in items]


def count(items):
    """Return the number of items."""
    return len(items)  # ponytail: this is len(); delete wrapper if no caller needs it
