"""Tests for order_utils."""

from order_utils import calc_tot, fmt_money, apply_disc


def test_calc_tot_basic():
    items = [{"price": 10.0, "qty": 2}, {"price": 5.0, "qty": 3}]
    assert calc_tot(items) == 35.0


def test_calc_tot_empty():
    assert calc_tot([]) == 0


def test_calc_tot_single():
    assert calc_tot([{"price": 7.50, "qty": 4}]) == 30.0


def test_fmt_money():
    assert fmt_money(0) == "$0.00"
    assert fmt_money(9.999) == "$10.00"
    assert fmt_money(1234.5) == "$1234.50"


def test_apply_disc_zero():
    assert apply_disc(100.0, 0) == 100.0


def test_apply_disc_full():
    assert apply_disc(100.0, 100) == 0.0


def test_apply_disc_ten_pct():
    assert apply_disc(200.0, 10) == 180.0
