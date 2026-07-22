"""
Data-loading module.

Provides utilities for loading, normalising, and inspecting
row-oriented text data.  Each row is a list of cell values
produced by splitting on commas.
"""


def compute_value(x):
    """Normalise a raw value.

    If *x* is a string the value is stripped of leading/trailing
    whitespace and lowercased.  Non-string values are returned
    unchanged so that numeric data passes through untouched.

    Args:
        x: The raw value to normalise.

    Returns:
        The normalised value.
    """
    if isinstance(x, str):
        return x.strip().lower()
    return x


def load_rows(text):
    """Split *text* into rows of normalised cells.

    The input is split on newlines; each line is then split on
    commas and every resulting cell is passed through
    :func:`compute_value` for normalisation.

    Args:
        text: A multi-line string where columns are
              comma-separated.

    Returns:
        A list of lists, one inner list per non-empty line.
    """
    rows = []
    for line in text.splitlines():
        if not line.strip():
            continue
        cells = [compute_value(cell) for cell in line.split(",")]
        rows.append(cells)
    return rows


def count_rows(rows):
    """Return the number of rows.

    Args:
        rows: A list of row lists as returned by :func:`load_rows`.

    Returns:
        An integer count.
    """
    return len(rows)


def first_row(rows):
    """Return the first row, or ``None`` if *rows* is empty.

    Args:
        rows: A list of row lists as returned by :func:`load_rows`.

    Returns:
        The first row list, or ``None``.
    """
    if rows:
        return rows[0]
    return None


def preprocess(x):
    """Pre-process a single value by normalising it.

    Delegates to :func:`compute_value` for the actual normalisation.

    Args:
        x: The raw value to pre-process.

    Returns:
        The normalised value.
    """
    return compute_value(x)
