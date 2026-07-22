"""Order processing utilities."""


def total(items):
    """Return the sum of each item's 'price' value."""
    return sum(item["price"] for item in items)
