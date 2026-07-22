"""Rate calculation utilities."""

from money import format_usd


def apply_rate(amount, rate):
    """Return amount * rate."""
    return amount * rate


def apply_rate_usd(amount, rate):
    """Apply rate to amount and return the result as a formatted USD string."""
    return format_usd(apply_rate(amount, rate))
