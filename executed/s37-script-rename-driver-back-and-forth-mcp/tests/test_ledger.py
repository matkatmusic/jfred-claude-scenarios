from ledger import record_entry, bal


def _book(*entries):
    book = []
    for name, typ, amount in entries:
        record_entry(book, {"name": name, "type": typ, "amount": amount})
    return book


def test_bal_empty():
    assert bal([]) == 0


def test_bal_debits_only():
    book = _book(("a", "debit", 100), ("b", "debit", 50))
    assert bal(book) == 150


def test_bal_credits_only():
    book = _book(("a", "credit", 200))
    assert bal(book) == -200


def test_bal_mixed():
    book = _book(("rent", "debit", 1200), ("salary", "credit", 3000))
    assert bal(book) == -1800


def test_bal_zero():
    book = _book(("in", "credit", 500), ("out", "debit", 500))
    assert bal(book) == 0
