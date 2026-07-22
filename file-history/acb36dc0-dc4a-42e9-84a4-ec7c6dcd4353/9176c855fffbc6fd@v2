from inventory import qty_chk, tot_value
import pytest


def _item(name="widget", price=10.0, stock=5):
    return {"name": name, "price": price, "stock": stock}


class TestQtyChk:
    def test_exact_stock(self):
        assert qty_chk(_item(stock=5), 5) is True

    def test_under_stock(self):
        assert qty_chk(_item(stock=5), 3) is True

    def test_over_stock(self):
        assert qty_chk(_item(stock=5), 6) is False

    def test_zero_requested(self):
        assert qty_chk(_item(stock=0), 0) is True

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            qty_chk(_item(), -1)


class TestTotValue:
    def test_empty_store(self):
        assert tot_value([]) == 0.0

    def test_single_item(self):
        assert tot_value([_item(price=2.5, stock=4)]) == 10.0

    def test_multiple_items(self):
        store = [_item(price=10, stock=2), _item(name="gear", price=5, stock=3)]
        assert tot_value(store) == 35.0

    def test_zero_stock_contributes_nothing(self):
        assert tot_value([_item(stock=0)]) == 0.0
