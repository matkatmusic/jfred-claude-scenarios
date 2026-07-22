import pytest
from billing import calc_tot, fmt_money


class TestCalcTot:
    def test_single_item(self):
        assert calc_tot([{"price": 10.0, "qty": 2}]) == 20.0

    def test_multiple_items(self):
        items = [{"price": 5.0, "qty": 3}, {"price": 2.50, "qty": 4}]
        assert calc_tot(items) == 25.0

    def test_empty_list(self):
        assert calc_tot([]) == 0.0

    def test_zero_qty(self):
        assert calc_tot([{"price": 99.99, "qty": 0}]) == 0.0

    def test_negative_price_raises(self):
        with pytest.raises(ValueError):
            calc_tot([{"price": -1, "qty": 1}])

    def test_negative_qty_raises(self):
        with pytest.raises(ValueError):
            calc_tot([{"price": 1, "qty": -1}])


class TestFmtMoney:
    def test_whole_dollar(self):
        assert fmt_money(5) == "$5.00"

    def test_cents(self):
        assert fmt_money(9.99) == "$9.99"

    def test_zero(self):
        assert fmt_money(0) == "$0.00"

    def test_negative(self):
        assert fmt_money(-4.5) == "$-4.50"

    def test_rounds_to_two_decimals(self):
        assert fmt_money(1.999) == "$2.00"
