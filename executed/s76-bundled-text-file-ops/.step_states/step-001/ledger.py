"""Simple ledger utilities."""


def entry_total(entries):
    """Sum the 'amount' field across all entries."""
    return sum(e["amount"] for e in entries)
