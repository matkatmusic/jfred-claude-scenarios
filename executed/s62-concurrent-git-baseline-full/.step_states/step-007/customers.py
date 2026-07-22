"""Customer utilities."""


def names(customers):
    """Return a list of each customer's 'name'."""
    return [c["name"] for c in customers]


def find(customers, name):
    """Return the first customer whose 'name' matches, or None."""
    return next((c for c in customers if c["name"] == name), None)
