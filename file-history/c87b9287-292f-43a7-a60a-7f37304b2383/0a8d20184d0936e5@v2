"""Customer name extraction."""


def names(customers):
    """Return a list of each customer's 'name'."""
    return [c["name"] for c in customers]


def emails(customers):
    """Return a list of each customer's 'email'."""
    return [c["email"] for c in customers]


def find(customers, name):
    """Return the customer with the given 'name', or None."""
    return next((c for c in customers if c["name"] == name), None)
