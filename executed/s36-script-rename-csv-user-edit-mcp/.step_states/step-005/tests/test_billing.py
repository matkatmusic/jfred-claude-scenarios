import pytest
from billing import calculate_total, format_currency


class TestCalcTot:
    def test_single_item(self):
        assert calculate_total([{"price": 10.0, "qty": 2}]) == 20.0

    def test_multiple_items(self):
        items = [{"price": 5.0, "qty": 3}, {"price": 2.50, "qty": 4}]
        assert calculate_total(items) == 25.0

    def test_empty_list(self):
        assert calculate_total([]) == 0.0

    def test_zero_qty(self):
        assert calculate_total([{"price": 99.99, "qty": 0}]) == 0.0

    def test_negative_price_raises(self):
        with pytest.raises(ValueError):
            calculate_total([{"price": -1, "qty": 1}])

    def test_negative_qty_raises(self):
        with pytest.raises(ValueError):
            calculate_total([{"price": 1, "qty": -1}])


class TestFmtMoney:
    def test_whole_dollar(self):
        assert format_currency(5) == "$5.00"

    def test_cents(self):
        assert format_currency(9.99) == "$9.99"

    def test_zero(self):
        assert format_currency(0) == "$0.00"

    def test_negative(self):
        assert format_currency(-4.5) == "$-4.50"

    def test_rounds_to_two_decimals(self):
        assert format_currency(1.999) == "$2.00"
