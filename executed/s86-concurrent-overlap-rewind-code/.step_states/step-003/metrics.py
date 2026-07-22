"""Basic sequence metrics."""


def total(values):
    """Return the sum of values.

    Args:
        values: Iterable of numbers.

    Returns:
        Sum of all elements.

    Raises:
        ValueError: If values is empty.
    """
    vals = list(values)
    if not vals:
        raise ValueError("values is empty")
    return sum(vals)


def mean(values):
    """Return the arithmetic mean of values.

    Args:
        values: Iterable of numbers.

    Returns:
        Arithmetic mean of all elements.

    Raises:
        ValueError: If values is empty.
    """
    vals = list(values)
    if not vals:
        raise ValueError("values is empty")
    return sum(vals) / len(vals)


def variance(values):
    """Return the population variance of values.

    Args:
        values: Iterable of numbers.

    Returns:
        Population variance of all elements.

    Raises:
        ValueError: If values is empty.
    """
    vals = list(values)
    if not vals:
        raise ValueError("values is empty")
    mu = sum(vals) / len(vals)
    return sum((x - mu) ** 2 for x in vals) / len(vals)
