from inventory import check_quantity, tot_value


def test_qty_chk_sufficient():
    assert check_quantity({"stock": 10}, 5) is True


def test_qty_chk_exact():
    assert check_quantity({"stock": 5}, 5) is True


def test_qty_chk_insufficient():
    assert check_quantity({"stock": 3}, 10) is False


def test_qty_chk_zero_request():
    assert check_quantity({"stock": 0}, 0) is True


def test_tot_value_basic():
    store = [
        {"price": 2.0, "stock": 5},
        {"price": 1.0, "stock": 10},
    ]
    assert tot_value(store) == 20.0


def test_tot_value_empty():
    assert tot_value([]) == 0


def test_tot_value_single():
    assert tot_value([{"price": 9.99, "stock": 1}]) == 9.99
