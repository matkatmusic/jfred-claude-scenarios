"""Order total calculation."""


def count(items):
    """Return the number of items."""
    return len(items)


def total(items):
    """Sum the 'price' of each item."""
    return sum(item["price"] for item in items)


def subtotal(items, n):
    """Sum the 'price' of the first n items."""
    return total(items[:n])
