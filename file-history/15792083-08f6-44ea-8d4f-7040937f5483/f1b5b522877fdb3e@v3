from billing import calculate_total, format_currency


class TestCalcTot:
    def test_single_item(self):
        assert calculate_total([{"price": 10.0, "qty": 3}]) == 30.0

    def test_multiple_items(self):
        items = [{"price": 5.0, "qty": 2}, {"price": 3.0, "qty": 4}]
        assert calculate_total(items) == 22.0

    def test_empty_list(self):
        assert calculate_total([]) == 0

    def test_zero_qty(self):
        assert calculate_total([{"price": 99.99, "qty": 0}]) == 0.0

    def test_fractional_price(self):
        assert calculate_total([{"price": 0.01, "qty": 1}]) == 0.01


class TestFmtMoney:
    def test_whole_number(self):
        assert format_currency(10) == "$10.00"

    def test_cents(self):
        assert format_currency(9.99) == "$9.99"

    def test_zero(self):
        assert format_currency(0) == "$0.00"

    def test_large(self):
        assert format_currency(1234567.89) == "$1234567.89"

    def test_negative(self):
        assert format_currency(-5.50) == "$-5.50"
