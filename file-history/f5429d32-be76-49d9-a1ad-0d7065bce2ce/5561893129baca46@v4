# ledger module — managed by finance
"""
Minimal double-entry accounting ledger.

A 'book' is a list of entry dicts. Each entry has:
    - name (str): identifier for the entry
    - type (str): 'debit' or 'credit'
    - amount (float): positive value

Functions operate on the book in place (add/rm) or return computed values
(total_debits, total_credits, bal).
"""


def record_entry(book, entry):
    """Append an entry dict to the book.

    Args:
        book: list of entry dicts.
        entry: dict with keys 'name', 'type', 'amount'.
            'type' must be 'debit' or 'credit'.
            'amount' must be non-negative.

    Raises:
        ValueError: if type is invalid or amount is negative.
    """
    if entry.get("type") not in ("debit", "credit"):
        raise ValueError(f"type must be 'debit' or 'credit', got {entry.get('type')!r}")
    if entry.get("amount", 0) < 0:
        raise ValueError("amount must be non-negative")
    book.append(entry)


def remove_entry(book, name):
    """Remove the first entry matching 'name' from the book.

    Args:
        book: list of entry dicts.
        name: the 'name' value to match.

    Raises:
        KeyError: if no entry with that name exists.
    """
    for i, e in enumerate(book):
        if e["name"] == name:
            book.pop(i)
            return
    raise KeyError(f"no entry named {name!r}")


def total_debits(book):
    """Sum all debit amounts in the book.

    Args:
        book: list of entry dicts.

    Returns:
        float: total of all entries where type == 'debit'.
    """
    return sum(e["amount"] for e in book if e["type"] == "debit")


def total_credits(book):
    """Sum all credit amounts in the book.

    Args:
        book: list of entry dicts.

    Returns:
        float: total of all entries where type == 'credit'.
    """
    return sum(e["amount"] for e in book if e["type"] == "credit")


def bal(book):
    """Return net balance: total debits minus total credits.

    Args:
        book: list of entry dicts.

    Returns:
        float: debits - credits. Positive means net debit,
            negative means net credit.
    """
    return total_debits(book) - total_credits(book)


def audit(book):
    """Return a summary dict with total debits, credits, and balance.

    Args:
        book: list of entry dicts.

    Returns:
        dict with keys 'debits', 'credits', 'balance'.
    """
    d = total_debits(book)
    c = total_credits(book)
    return {"debits": d, "credits": c, "balance": d - c}


def make_entry(name, entry_type, amount):
    """Convenience constructor for an entry dict.

    Args:
        name: identifier string.
        entry_type: 'debit' or 'credit'.
        amount: non-negative number.

    Returns:
        dict: entry ready to pass to record_entry.
    """
    return {"name": name, "type": entry_type, "amount": amount}


if __name__ == "__main__":
    # ponytail: self-check, not a test suite
    b = []
    record_entry(b, make_entry("rent", "debit", 1200))
    record_entry(b, make_entry("salary", "credit", 3000))
    record_entry(b, make_entry("groceries", "debit", 150))
    assert total_debits(b) == 1350
    assert total_credits(b) == 3000
    assert bal(b) == -1650
    remove_entry(b, "groceries")
    assert bal(b) == -1800
    assert len(b) == 2
    try:
        remove_entry(b, "nonexistent")
        assert False, "should have raised"
    except KeyError:
        pass
    try:
        record_entry(b, {"name": "bad", "type": "wrong", "amount": 10})
        assert False, "should have raised"
    except ValueError:
        pass
    print("all checks pass")
# names normalized via rename script
