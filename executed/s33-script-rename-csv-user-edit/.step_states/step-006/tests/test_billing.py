"""Tests for billing.calculate_total and billing.format_currency."""

from billing import calculate_total, format_currency


def test_calc_tot_basic():
    items = [{"price": 10.0, "qty": 2}, {"price": 5.50, "qty": 1}]
    assert calculate_total(items) == 25.50


def test_calc_tot_empty():
    assert calculate_total([]) == 0.0


def test_calc_tot_single_item():
    assert calculate_total([{"price": 99.99, "qty": 1}]) == 99.99


def test_calc_tot_fractional_rounding():
    items = [{"price": 0.1, "qty": 3}]
    assert calculate_total(items) == 0.30


def test_fmt_money_positive():
    assert format_currency(25.50) == "$25.50"


def test_fmt_money_zero():
    assert format_currency(0) == "$0.00"


def test_fmt_money_negative():
    assert format_currency(-5) == "-$5.00"


def test_fmt_money_rounds_to_cents():
    assert format_currency(1.999) == "$2.00"
