"""
Geometry core — rectangle and box primitives.

Provides basic geometric calculations for rectangles and rectangular boxes:
rectangle_area, perimeter, volume, diagonal, and scaling.

All functions accept numeric arguments (int or float) and return
numeric results.

Usage:
    >>> from geo_core import rectangle_area, rectangle_perimeter, box_volume, diag, scale
    >>> rectangle_area(3, 4)
    12
    >>> diag(3, 4)
    5.0
"""

import math


def rectangle_area(w, h):
    """Return the rectangle_area of a rectangle.

    Args:
        w: Width of the rectangle.
        h: Height of the rectangle.

    Returns:
        The product w * h.

    >>> rectangle_area(3, 4)
    12
    >>> rectangle_area(0, 5)
    0
    >>> rectangle_area(2.5, 4)
    10.0
    """
    return w * h


def rectangle_perimeter(w, h):
    """Return the perimeter of a rectangle.

    Args:
        w: Width of the rectangle.
        h: Height of the rectangle.

    Returns:
        The perimeter 2 * (w + h).

    >>> rectangle_perimeter(3, 4)
    14
    >>> rectangle_perimeter(0, 5)
    10
    >>> rectangle_perimeter(1.5, 2.5)
    8.0
    """
    return 2 * (w + h)


def box_volume(w, h, d):
    """Return the volume of a rectangular box.

    Args:
        w: Width.
        h: Height.
        d: Depth.

    Returns:
        The product w * h * d.

    >>> box_volume(3, 4, 5)
    60
    >>> box_volume(0, 4, 5)
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


def bounding_box(points):
    """Return the axis-aligned bounding box of a sequence of (x, y) points.

    Args:
        points: Iterable of (x, y) tuples.

    Returns:
        A tuple (min_x, min_y, max_x, max_y).

    >>> bounding_box([(0, 0), (3, 4), (-1, 2)])
    (-1, 0, 3, 4)
    """
    xs, ys = zip(*points)
    return (min(xs), min(ys), max(xs), max(ys))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
