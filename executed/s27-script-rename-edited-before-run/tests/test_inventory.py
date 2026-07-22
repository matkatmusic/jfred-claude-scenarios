"""Tests for qty_chk and tot_value."""

import pytest
from inventory import qty_chk, tot_value


# --- qty_chk ---

def test_qty_chk_exact_stock():
    assert qty_chk({"stock": 10}, 10) is True


def test_qty_chk_under_stock():
    assert qty_chk({"stock": 10}, 5) is True


def test_qty_chk_over_stock():
    assert qty_chk({"stock": 10}, 11) is False


def test_qty_chk_zero_requested():
    assert qty_chk({"stock": 0}, 0) is True


def test_qty_chk_zero_stock_nonzero_request():
    assert qty_chk({"stock": 0}, 1) is False


def test_qty_chk_missing_key():
    with pytest.raises(KeyError):
        qty_chk({}, 1)


# --- tot_value ---

def test_tot_value_empty_store():
    assert tot_value([]) == 0


def test_tot_value_single_item():
    store = [{"price": 5.0, "stock": 10}]
    assert tot_value(store) == 50.0


def test_tot_value_multiple_items():
    store = [
        {"price": 2.50, "stock": 100},
        {"price": 15.00, "stock": 20},
    ]
    assert tot_value(store) == 550.0


def test_tot_value_zero_stock():
    store = [{"price": 99.99, "stock": 0}]
    assert tot_value(store) == 0.0


def test_tot_value_zero_price():
    store = [{"price": 0.0, "stock": 1000}]
    assert tot_value(store) == 0.0
