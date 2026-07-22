from inventory import check_quantity, lookup_item, restock


def test_qty_chk_sufficient():
    assert check_quantity({"name": "bolt", "stock": 10}, 5) is True


def test_qty_chk_exact():
    assert check_quantity({"name": "bolt", "stock": 5}, 5) is True


def test_qty_chk_insufficient():
    assert check_quantity({"name": "bolt", "stock": 3}, 5) is False


def test_check_quantity_zero_stock():
    """Item with zero stock should fail any positive quantity check."""
    assert check_quantity({"name": "bolt", "stock": 0}, 1) is False


def test_find_item_exists():
    store = [{"name": "bolt", "stock": 10}, {"name": "nut", "stock": 4}]
    assert lookup_item(store, "nut")["stock"] == 4


def test_find_item_missing():
    store = [{"name": "bolt", "stock": 10}]
    assert lookup_item(store, "washer") is None


def test_restock_existing_item():
    """Restocking an existing item with insufficient stock should raise it to n."""
    store = [{"name": "bolt", "stock": 3}]
    restock(store, "bolt", 10)
    assert store[0]["stock"] == 10
# tests updated
