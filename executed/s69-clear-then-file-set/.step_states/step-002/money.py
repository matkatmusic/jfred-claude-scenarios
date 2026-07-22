"""USD formatting utilities."""


def format_usd(n):
    """Return n as a '$0.00'-style string."""
    return f"${n:,.2f}"


def parse_usd(s):
    """Parse a '$0.00'-style string and return a float."""
    return float(s.replace("$", "").replace(",", ""))
