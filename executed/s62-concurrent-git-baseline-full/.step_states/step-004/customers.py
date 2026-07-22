"""Customer utilities."""


def names(customers):
    """Return a list of each customer's 'name'."""
    return [c["name"] for c in customers]
