"""Geometric shape calculations."""

import math


def circle_area(r):
    """Return the area of a circle with radius r."""
    return math.pi * r * r


def rect_area(w, h):
    """Return the area of a rectangle with width w and height h."""
    return w * h


def triangle_area(b, h):
    """Return the area of a triangle with base b and height h."""
    return b * h / 2
