from billing import calc_tot, fmt_money


class TestCalcTot:
    def test_single_item(self):
        assert calc_tot([{"price": 10.0, "qty": 3}]) == 30.0

    def test_multiple_items(self):
        items = [{"price": 5.0, "qty": 2}, {"price": 3.0, "qty": 4}]
        assert calc_tot(items) == 22.0

    def test_empty_list(self):
        assert calc_tot([]) == 0

    def test_zero_qty(self):
        assert calc_tot([{"price": 99.99, "qty": 0}]) == 0.0

    def test_fractional_price(self):
        assert calc_tot([{"price": 0.01, "qty": 1}]) == 0.01


class TestFmtMoney:
    def test_whole_number(self):
        assert fmt_money(10) == "$10.00"

    def test_cents(self):
        assert fmt_money(9.99) == "$9.99"

    def test_zero(self):
        assert fmt_money(0) == "$0.00"

    def test_large(self):
        assert fmt_money(1234567.89) == "$1234567.89"

    def test_negative(self):
        assert fmt_money(-5.50) == "$-5.50"
