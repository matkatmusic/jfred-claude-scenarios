from inventory import qty_chk, tot_value


def test_qty_chk_enough():
    assert qty_chk({"stock": 10}, 10) is True


def test_qty_chk_not_enough():
    assert qty_chk({"stock": 5}, 6) is False


def test_qty_chk_zero():
    assert qty_chk({"stock": 0}, 0) is True


def test_tot_value_empty():
    assert tot_value([]) == 0


def test_tot_value_single():
    store = [{"price": 3.0, "stock": 4}]
    assert tot_value(store) == 12.0


def test_tot_value_multiple():
    store = [
        {"price": 1.50, "stock": 10},
        {"price": 2.00, "stock": 5},
    ]
    assert tot_value(store) == 25.0
