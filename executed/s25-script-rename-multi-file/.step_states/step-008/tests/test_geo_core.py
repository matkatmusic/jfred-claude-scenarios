"""Tests for geo_core rectangle_area and rectangle_perimeter."""

from geo_core import rectangle_area, rectangle_perimeter


def test_area_positive():
    assert rectangle_area(3, 4) == 12


def test_area_zero():
    assert rectangle_area(0, 5) == 0


def test_area_float():
    assert rectangle_area(2.5, 4) == 10.0


def test_perim_positive():
    assert rectangle_perimeter(3, 4) == 14


def test_perim_zero():
    assert rectangle_perimeter(0, 5) == 10


def test_perim_float():
    assert rectangle_perimeter(1.5, 2.5) == 8.0
