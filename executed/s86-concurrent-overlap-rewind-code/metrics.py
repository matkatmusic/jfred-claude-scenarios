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


def geometric_mean(values):
    """Return the geometric mean of values.

    Args:
        values: Iterable of numbers.

    Returns:
        The nth root of the product of all elements.

    Raises:
        ValueError: If values is empty or any value is not positive.
    """
    vals = list(values)
    if not vals:
        raise ValueError("values is empty")
    if any(v <= 0 for v in vals):
        raise ValueError("all values must be positive")
    product = 1
    for v in vals:
        product *= v
    return product ** (1 / len(vals))


def harmonic_mean(values):
    """Return the harmonic mean of values.

    Args:
        values: Iterable of numbers.

    Returns:
        n divided by the sum of reciprocals of all elements.

    Raises:
        ValueError: If values is empty or any value is zero.
    """
    vals = list(values)
    if not vals:
        raise ValueError("values is empty")
    if any(v == 0 for v in vals):
        raise ValueError("values must not contain zero")
    return len(vals) / sum(1 / v for v in vals)


def zscore(value, values):
    """Return the z-score of value within values.

    Args:
        value: The number to score.
        values: Iterable of numbers forming the population.

    Returns:
        (value - mean) / stddev of the population.

    Raises:
        ValueError: If standard deviation is zero.
    """
    mu = mean(values)
    sd = stddev(values)
    if sd == 0:
        raise ValueError("standard deviation is zero")
    return (value - mu) / sd


def percentile(values, p):
    """Return the value at the pth percentile using nearest-rank.

    Args:
        values: Iterable of numbers.
        p: Percentile to compute, between 0 and 100 inclusive.

    Returns:
        The value at the pth percentile of the sorted input.

    Raises:
        ValueError: If values is empty or p is outside 0-100.
    """
    vals = sorted(values)
    if not vals:
        raise ValueError("values is empty")
    if not 0 <= p <= 100:
        raise ValueError("p must be between 0 and 100")
    import math
    idx = max(0, math.ceil(len(vals) * p / 100) - 1)
    return vals[idx]
