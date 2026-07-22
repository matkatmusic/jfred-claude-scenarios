"""Tests for base_price and round_price."""

import pytest

from pricing import base_price, round_price


class TestBasePrice:
    def test_returns_float(self):
        assert base_price({"price": 10}) == 10.0

    def test_int_value(self):
        assert base_price({"price": 5}) == 5.0

    def test_float_value(self):
        assert base_price({"price": 19.99}) == 19.99

    def test_zero(self):
        assert base_price({"price": 0}) == 0.0

    def test_missing_key_raises(self):
        with pytest.raises(KeyError):
            base_price({"name": "oops"})

    def test_non_numeric_raises(self):
        with pytest.raises(TypeError):
            base_price({"price": "free"})


class TestRoundPrice:
    def test_rounds_down(self):
        assert round_price(1.111) == 1.11

    def test_rounds_up(self):
        assert round_price(1.119) == 1.12

    def test_already_two_decimals(self):
        assert round_price(5.25) == 5.25

    def test_integer_input(self):
        assert round_price(7) == 7.0

    def test_negative(self):
        assert round_price(-3.456) == -3.46
