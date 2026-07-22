from inventory import check_quantity, find_item


def test_qty_chk_sufficient():
    assert check_quantity({"name": "bolt", "stock": 10}, 5) is True


def test_qty_chk_exact():
    assert check_quantity({"name": "bolt", "stock": 5}, 5) is True


def test_qty_chk_insufficient():
    assert check_quantity({"name": "bolt", "stock": 3}, 5) is False


def test_find_item_exists():
    store = [{"name": "bolt", "stock": 10}, {"name": "nut", "stock": 4}]
    assert find_item(store, "nut")["stock"] == 4


def test_find_item_missing():
    store = [{"name": "bolt", "stock": 10}]
    assert find_item(store, "washer") is None
