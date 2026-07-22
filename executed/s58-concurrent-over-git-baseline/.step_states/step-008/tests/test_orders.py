from orders import total


def test_total_sums_prices():
    assert total([{"price": 10}, {"price": 20}]) == 30


def test_total_empty():
    assert total([]) == 0
