"""
Geometry core — rectangle and box primitives.

Provides basic geometric calculations for rectangles and rectangular boxes:
area, perimeter, volume, diagonal, and scaling.

All functions accept numeric arguments (int or float) and return
numeric results.

Usage:
    >>> from geo_core import area, perim, vol, diag, scale
    >>> area(3, 4)
    12
    >>> diag(3, 4)
    5.0
"""

import math


def area(w, h):
    """Return the area of a rectangle.

    Args:
        w: Width of the rectangle.
        h: Height of the rectangle.

    Returns:
        The product w * h.

    >>> area(3, 4)
    12
    >>> area(0, 5)
    0
    >>> area(2.5, 4)
    10.0
    """
    return w * h


def perim(w, h):
    """Return the perimeter of a rectangle.

    Args:
        w: Width of the rectangle.
        h: Height of the rectangle.

    Returns:
        The perimeter 2 * (w + h).

    >>> perim(3, 4)
    14
    >>> perim(0, 5)
    10
    >>> perim(1.5, 2.5)
    8.0
    """
    return 2 * (w + h)


def vol(w, h, d):
    """Return the volume of a rectangular box.

    Args:
        w: Width.
        h: Height.
        d: Depth.

    Returns:
        The product w * h * d.

    >>> vol(3, 4, 5)
    60
    >>> vol(0, 4, 5)
    0
    """
    return w * h * d


def diag(w, h):
    """Return the diagonal of a rectangle.

    Args:
        w: Width of the rectangle.
        h: Height of the rectangle.

    Returns:
        The length of the diagonal, sqrt(w**2 + h**2).

    >>> diag(3, 4)
    5.0
    >>> diag(0, 5)
    5.0
    """
    return math.hypot(w, h)


def scale(w, h, k):
    """Return (w, h) scaled by factor k.

    Args:
        w: Width.
        h: Height.
        k: Scale factor.

    Returns:
        A tuple (w * k, h * k).

    >>> scale(3, 4, 2)
    (6, 8)
    >>> scale(1.0, 2.0, 0.5)
    (0.5, 1.0)
    """
    return (w * k, h * k)


def midpoint(x1, y1, x2, y2):
    """Return the midpoint of two points.

    Args:
        x1: X coordinate of the first point.
        y1: Y coordinate of the first point.
        x2: X coordinate of the second point.
        y2: Y coordinate of the second point.

    Returns:
        A tuple ((x1 + x2) / 2, (y1 + y2) / 2).

    >>> midpoint(0, 0, 4, 6)
    (2.0, 3.0)
    >>> midpoint(-1, -1, 1, 1)
    (0.0, 0.0)
    """
    return ((x1 + x2) / 2, (y1 + y2) / 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
