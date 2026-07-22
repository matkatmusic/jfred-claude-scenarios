"""
Vendored utility module.

This module is maintained by an external vendor and must NOT
be modified by automated refactoring tools.  Its :func:`helper`
function intentionally shares a name with helpers in other
package modules but serves a distinct, vendor-specific purpose.
"""


def helper(x):
    """Vendor-specific value transform.

    Converts *x* to its string representation and wraps it in
    square brackets.  This is the vendor's canonical formatting
    convention used across their tooling.

    Args:
        x: Any value to wrap.

    Returns:
        A string like ``"[value]"``.
    """
    return f"[{x}]"


def vendor_render(items):
    """Render a list of items using the vendor format.

    Each item is passed through :func:`helper` and the results
    are joined with commas.

    Args:
        items: An iterable of values to render.

    Returns:
        A comma-separated string of bracketed values.
    """
    return ", ".join(helper(item) for item in items)


def vendor_header(title):
    """Create a vendor-style header.

    The title is uppercased and passed through :func:`helper`
    to apply the bracket-wrapping convention.

    Args:
        title: The header title string.

    Returns:
        A bracketed, uppercased header string.
    """
    return helper(title.upper())


def vendor_footer(count):
    """Create a vendor-style footer line.

    Combines the count with :func:`helper` formatting for
    consistent vendor output.

    Args:
        count: Number of records summarised.

    Returns:
        A string like ``"Records: [5]"``.
    """
    return f"Records: {helper(count)}"
