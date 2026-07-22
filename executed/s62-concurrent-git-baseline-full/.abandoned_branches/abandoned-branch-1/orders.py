"""Order processing utilities."""


def total(items):
    """Sum the 'price' of each item."""
    return sum(item["price"] for item in items)


def count(items):
    """Return the number of items."""
    return len(items)


def subtotal(items, n):
    """Return the total of the first n items."""
    return total(items[:n])


def most_expensive(items):
    """Return the item with the highest price."""
    return max(items, key=lambda item: item["price"])
