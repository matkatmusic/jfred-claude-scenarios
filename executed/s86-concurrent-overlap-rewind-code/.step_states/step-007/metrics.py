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


def stddev(values):
    """Return the population standard deviation of values.

    Args:
        values: Iterable of numbers.

    Returns:
        Population standard deviation of all elements.

    Raises:
        ValueError: If values is empty.
    """
    return variance(values) ** 0.5


def median(values):
    """Return the median of values.

    Args:
        values: Iterable of numbers.

    Returns:
        Middle value of the sorted input. For even-length inputs,
        returns the mean of the two middle values.

    Raises:
        ValueError: If values is empty.
    """
    vals = sorted(values)
    if not vals:
        raise ValueError("values is empty")
    n = len(vals)
    mid = n // 2
    if n % 2:
        return vals[mid]
    return (vals[mid - 1] + vals[mid]) / 2


def mode(values):
    """Return the most common value in values.

    Args:
        values: Iterable of numbers.

    Returns:
        Most frequently occurring value. If multiple values share the
        highest frequency, returns the one that appears first.

    Raises:
        ValueError: If values is empty.
    """
    vals = list(values)
    if not vals:
        raise ValueError("values is empty")
    # ponytail: O(n²) scan, use collections.Counter if perf matters
    return max(set(vals), key=lambda v: (vals.count(v), -vals.index(v)))


def value_range(values):
    """Return the range of values (max minus min).

    Args:
        values: Iterable of numbers.

    Returns:
        Difference between the largest and smallest elements.

    Raises:
        ValueError: If values is empty.
    """
    vals = list(values)
    if not vals:
        raise ValueError("values is empty")
    return max(vals) - min(vals)
