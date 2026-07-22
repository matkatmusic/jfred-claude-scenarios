"""Order processing utilities."""


def count(items):
    """Return the number of items."""
    return len(items)  # ponytail: this is len(); delete wrapper if unused


def names(items):
    """Return a list of each item's 'name' value."""
    return [item["name"] for item in items]


def subtotal(items, n):
    """Return the total of the first n items."""
    return total(items[:n])


def total(items):
    """Return the sum of each item's 'price' value."""
    return sum(item["price"] for item in items)
