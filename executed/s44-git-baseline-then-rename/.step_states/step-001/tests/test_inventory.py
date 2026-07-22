from inventory import qty_chk, tot_value


def test_qty_chk_sufficient():
    assert qty_chk({"stock": 10}, 5) is True


def test_qty_chk_exact():
    assert qty_chk({"stock": 3}, 3) is True


def test_qty_chk_insufficient():
    assert qty_chk({"stock": 2}, 5) is False


def test_qty_chk_zero_request():
    assert qty_chk({"stock": 0}, 0) is True


def test_tot_value_basic():
    store = [
        {"name": "A", "price": 10.0, "stock": 2},
        {"name": "B", "price": 5.0, "stock": 4},
    ]
    assert tot_value(store) == 40.0


def test_tot_value_empty():
    assert tot_value([]) == 0.0


def test_tot_value_zero_stock():
    store = [{"name": "X", "price": 99.0, "stock": 0}]
    assert tot_value(store) == 0.0
