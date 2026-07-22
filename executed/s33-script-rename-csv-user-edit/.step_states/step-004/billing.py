"""
Billing module -- price calculation, formatting, stock checks, and discounts.

Functions:
    calc_tot(items)        Sum line items (price * qty).
    fmt_money(n)           Format a number as "$0.00".
    chk_stock(item, qty)   Check if requested qty is in stock.
    apply_disc(total, pct) Apply a percentage discount.
"""

from __future__ import annotations


def calc_tot(items: list[dict]) -> float:
    """Sum price * qty for each item in the list.

    Each item must be a dict with numeric 'price' and 'qty' keys.
    Returns 0.0 for an empty list.

    Args:
        items: List of dicts, each with 'price' and 'qty'.

    Returns:
        Total price as a float, rounded to 2 decimal places.

    Raises:
        KeyError: If an item is missing 'price' or 'qty'.
    """
    return round(sum(item["price"] * item["qty"] for item in items), 2)


def fmt_money(n: float) -> str:
    """Format a number as a US dollar string.

    Positive and zero values render as "$1.23" or "$0.00".
    Negative values render as "-$1.23".

    Args:
        n: Numeric value to format.

    Returns:
        Dollar-formatted string with exactly two decimal places.
    """
    if n < 0:
        return f"-${abs(n):.2f}"
    return f"${n:.2f}"


def chk_stock(item: dict, qty: int) -> bool:
    """Check whether the requested quantity is available in stock.

    Args:
        item: Dict with an integer 'stock' key.
        qty: Requested quantity.

    Returns:
        True if qty <= item['stock'], False otherwise.

    Raises:
        KeyError: If item has no 'stock' key.
    """
    return qty <= item["stock"]


def apply_disc(total: float, pct: float) -> float:
    """Apply a percentage discount to a total.

    Args:
        total: Original total amount.
        pct: Discount as a percentage (0-100 inclusive).

    Returns:
        Discounted total, rounded to 2 decimal places.

    Raises:
        ValueError: If pct is outside the 0-100 range.
    """
    if not 0 <= pct <= 100:
        raise ValueError(f"Discount must be 0-100, got {pct}")
    return round(total * (1 - pct / 100), 2)


def validate(items: list[dict]) -> bool:
    """Raise ValueError if any item lacks a 'price' key.

    Args:
        items: List of item dicts to validate.

    Returns:
        True if all items have a 'price' key.

    Raises:
        ValueError: If any item is missing 'price'.
    """
    for i, item in enumerate(items):
        if "price" not in item:
            raise ValueError(f"Item {i} missing 'price' key")
    return True


if __name__ == "__main__":
    # ponytail: self-check, not a test suite
    sample = [
        {"price": 10.00, "qty": 2},
        {"price": 5.50, "qty": 1},
    ]
    assert calc_tot(sample) == 25.50
    assert calc_tot([]) == 0.0

    assert fmt_money(25.50) == "$25.50"
    assert fmt_money(0) == "$0.00"
    assert fmt_money(-5) == "-$5.00"
    assert fmt_money(1000.1) == "$1000.10"

    assert chk_stock({"stock": 10}, 10) is True
    assert chk_stock({"stock": 10}, 11) is False
    assert chk_stock({"stock": 0}, 0) is True

    assert apply_disc(100.0, 10) == 90.0
    assert apply_disc(100.0, 0) == 100.0
    assert apply_disc(100.0, 100) == 0.0

    try:
        apply_disc(100, -1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    print("All checks passed.")
