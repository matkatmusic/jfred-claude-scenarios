import pytest
from ledger import add_entry, bal, make_entry, rm_entry


@pytest.fixture
def book():
    b = []
    add_entry(b, make_entry("rent", "debit", 1200))
    add_entry(b, make_entry("salary", "credit", 3000))
    add_entry(b, make_entry("groceries", "debit", 150))
    return b


def test_bal_basic(book):
    assert bal(book) == -1650


def test_bal_empty():
    assert bal([]) == 0


def test_bal_after_removal(book):
    rm_entry(book, "groceries")
    assert bal(book) == -1800


def test_bal_all_debits():
    b = []
    add_entry(b, make_entry("a", "debit", 100))
    add_entry(b, make_entry("b", "debit", 200))
    assert bal(b) == 300


def test_bal_all_credits():
    b = []
    add_entry(b, make_entry("a", "credit", 100))
    add_entry(b, make_entry("b", "credit", 200))
    assert bal(b) == -300
