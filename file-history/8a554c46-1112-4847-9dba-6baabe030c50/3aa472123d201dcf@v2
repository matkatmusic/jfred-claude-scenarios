"""Tests for billing.calc_tot and billing.fmt_money."""

from billing import calc_tot, fmt_money


def test_calc_tot_basic():
    items = [{"price": 10.0, "qty": 2}, {"price": 5.50, "qty": 1}]
    assert calc_tot(items) == 25.50


def test_calc_tot_empty():
    assert calc_tot([]) == 0.0


def test_calc_tot_single_item():
    assert calc_tot([{"price": 99.99, "qty": 1}]) == 99.99


def test_calc_tot_fractional_rounding():
    items = [{"price": 0.1, "qty": 3}]
    assert calc_tot(items) == 0.30


def test_fmt_money_positive():
    assert fmt_money(25.50) == "$25.50"


def test_fmt_money_zero():
    assert fmt_money(0) == "$0.00"


def test_fmt_money_negative():
    assert fmt_money(-5) == "-$5.00"


def test_fmt_money_rounds_to_cents():
    assert fmt_money(1.999) == "$2.00"
