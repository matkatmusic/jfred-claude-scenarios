from inventory import check_quantity, tot_value


def test_qty_chk_available():
    assert check_quantity({"stock": 10}, 10) is True


def test_qty_chk_under():
    assert check_quantity({"stock": 10}, 5) is True


def test_qty_chk_over():
    assert check_quantity({"stock": 10}, 11) is False


def test_qty_chk_zero():
    assert check_quantity({"stock": 0}, 0) is True


def test_tot_value_multiple():
    store = [
        {"price": 10.0, "stock": 3},
        {"price": 5.0, "stock": 4},
    ]
    assert tot_value(store) == 50.0


def test_tot_value_empty():
    assert tot_value([]) == 0


def test_tot_value_single():
    assert tot_value([{"price": 7.5, "stock": 2}]) == 15.0
