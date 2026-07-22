"""Order helpers — price totals and name extraction."""


def total(items):
    """Return the sum of each item's 'price'."""
    return sum(item["price"] for item in items)


def names(items):
    """Return a list of each item's 'name'."""
    return [item["name"] for item in items]
