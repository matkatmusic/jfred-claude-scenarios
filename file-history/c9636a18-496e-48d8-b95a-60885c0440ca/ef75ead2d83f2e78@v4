"""Simple ledger utilities."""


def entry_total(entries):
    """Sum the 'amount' field across all entries."""
    return sum(e["amount"] for e in entries)


def entry_count(entries):
    """Return the number of entries."""
    return len(entries)


def largest_entry(entries):
    """Return the entry with the greatest 'amount'."""
    return max(entries, key=lambda e: e["amount"])
