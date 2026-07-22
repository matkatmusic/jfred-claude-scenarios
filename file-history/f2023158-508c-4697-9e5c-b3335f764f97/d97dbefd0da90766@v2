"""Tests for geo_core area and perim."""

from geo_core import area, perim


def test_area_positive():
    assert area(3, 4) == 12


def test_area_zero():
    assert area(0, 5) == 0


def test_area_float():
    assert area(2.5, 4) == 10.0


def test_perim_positive():
    assert perim(3, 4) == 14


def test_perim_zero():
    assert perim(0, 5) == 10


def test_perim_float():
    assert perim(1.5, 2.5) == 8.0
