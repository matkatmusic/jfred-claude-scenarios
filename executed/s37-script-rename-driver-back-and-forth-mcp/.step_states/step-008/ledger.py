# ledger module — managed by finance
"""
ledger — minimal double-entry accounting ledger.

A *book* is a plain list of entry dicts.  Each entry has at minimum:
    name   (str)  — unique identifier for the entry
    type   (str)  — "debit" or "credit"
    amount (float/int) — positive value

Functions operate on the book in place where possible and return
useful scalars otherwise.  No persistence, no formatting, no ORM —
bring your own storage.

Example
-------
>>> book = []
>>> record_entry(book, {"name": "rent", "type": "debit", "amount": 1200})
>>> record_entry(book, {"name": "salary", "type": "credit", "amount": 3000})
>>> bal(book)
-1800
"""


def record_entry(book, entry):
    """Append *entry* to *book*.

    Parameters
    ----------
    book  : list[dict] — the ledger.
    entry : dict       — must contain 'name', 'type', and 'amount'.

    Raises
    ------
    ValueError
        If required keys are missing or type is not 'debit'/'credit'.
    """
    missing = {"name", "type", "amount"} - entry.keys()
    if missing:
        raise ValueError(f"entry missing keys: {missing}")
    if entry["type"] not in ("debit", "credit"):
        raise ValueError(f"type must be 'debit' or 'credit', got {entry['type']!r}")
    book.append(entry)


def remove_entry(book, name):
    """Remove the first entry whose 'name' matches *name*.

    Parameters
    ----------
    book : list[dict] — the ledger.
    name : str        — the entry name to remove.

    Raises
    ------
    KeyError
        If no entry with that name exists.
    """
    for i, e in enumerate(book):
        if e["name"] == name:
            book.pop(i)
            return
    raise KeyError(name)


def total_debits(book):
    """Return the sum of all debit amounts in *book*.

    Parameters
    ----------
    book : list[dict] — the ledger.

    Returns
    -------
    float — total debits (zero if none).
    """
    return sum(e["amount"] for e in book if e["type"] == "debit")


def total_credits(book):
    """Return the sum of all credit amounts in *book*.

    Parameters
    ----------
    book : list[dict] — the ledger.

    Returns
    -------
    float — total credits (zero if none).
    """
    return sum(e["amount"] for e in book if e["type"] == "credit")


def bal(book):
    """Return debits minus credits.

    A positive balance means more has been debited than credited.
    A negative balance means credits exceed debits.

    Parameters
    ----------
    book : list[dict] — the ledger.

    Returns
    -------
    float — net balance (debits - credits).
    """
    return total_debits(book) - total_credits(book)


def audit(book):
    """Return a dict with total debits, credits, and balance.

    Parameters
    ----------
    book : list[dict] — the ledger.

    Returns
    -------
    dict — {'debits': float, 'credits': float, 'balance': float}
    """
    d = total_debits(book)
    c = total_credits(book)
    return {"debits": d, "credits": c, "balance": d - c}


# ponytail: no Entry class, no Book class, no serialization.
# Add when you need persistence or cross-entry validation.
