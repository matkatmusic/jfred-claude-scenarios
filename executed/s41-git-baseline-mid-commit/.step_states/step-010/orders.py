"""Order processing utilities."""


def total(items):
    """Return the sum of each item's 'price'."""
    return sum(item["price"] for item in items)


def subtotal(items, n):
    """Return the total price of the first n items."""
    return sum(item["price"] for item in items[:n])


def count(items):
    """Return the number of items."""
    return len(items)


def names(items):
    """Return a list of each item's 'name'."""
    return [item["name"] for item in items]
# reviewed by ops
# checked
