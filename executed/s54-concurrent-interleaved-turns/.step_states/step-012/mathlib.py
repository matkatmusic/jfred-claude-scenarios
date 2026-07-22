"""Math utilities."""


def add(a, b):
    """Return a + b."""
    return a + b


def sub(a, b):
    """Return a - b."""
    return a - b


def mul(a, b):
    """Return a * b."""
    return a * b


def div(a, b):
    """Return a / b. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def mod(a, b):
    """Return a % b."""
    return a % b
