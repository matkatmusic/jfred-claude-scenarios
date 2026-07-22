"""
Reporting module.

Builds human-readable report strings from row-oriented data.
Every value is title-cased for display via the local
:func:`helper` formatter.
"""


def helper(x):
    """Format a value for display.

    Converts *x* to a string and applies title-casing so that
    report output looks consistent regardless of the original
    casing of the input data.

    Args:
        x: Any value to format.

    Returns:
        A title-cased string representation of *x*.
    """
    return str(x).title()


def render(rows):
    """Build a report string from *rows*.

    Each row is formatted by calling :func:`helper` on every cell
    and joining the results with ``" | "``.  Rows are separated
    by newlines.

    Args:
        rows: A list of row lists (e.g. from
              :func:`pkg.a.load_rows`).

    Returns:
        A multi-line report string ready for display.
    """
    lines = []
    for row in rows:
        formatted = [helper(cell) for cell in row]
        lines.append(" | ".join(formatted))
    return "\n".join(lines)


def header(cols):
    """Join column names into a header line.

    Each column name is passed through :func:`helper` for
    consistent title-casing, then joined with ``" | "``.

    Args:
        cols: An iterable of column name strings.

    Returns:
        A single formatted header string.
    """
    return " | ".join(helper(c) for c in cols)


def footer(n):
    """Return a one-line summary for the bottom of a report.

    Args:
        n: The number of data rows in the report.

    Returns:
        A string like ``"Total: 5 rows"``.
    """
    return f"Total: {n} rows"
