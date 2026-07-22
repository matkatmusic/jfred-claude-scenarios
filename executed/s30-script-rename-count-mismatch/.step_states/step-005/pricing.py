"""
pricing — minimal pricing helpers.

Functions
---------
base_price(item)    → raw price from an item dict
net_price(item, pct) → price after a percentage discount
bulk_price(items)   → sum of net prices across a list of items
round_to_cents(n)      → round a float to two decimal places (cents)
tax_price(n, rate)  → price with tax applied

Every money result passes through round_to_cents before it leaves.
"""

from __future__ import annotations

from typing import Any


def base_price(item: dict[str, Any]) -> float:
    """Return the raw price of *item*.

    Expects *item* to carry a ``"price"`` key with a numeric value.
    Raises ``KeyError`` if the key is missing, ``TypeError`` if the
    value isn't numeric.

    >>> base_price({"name": "widget", "price": 9.99})
    9.99
    """
    price = item["price"]
    if not isinstance(price, (int, float)):
        raise TypeError(f"price must be numeric, got {type(price).__name__}")
    return float(price)


def round_to_cents(n: float) -> float:
    """Round *n* to two decimal places (i.e. to the cent).

    Uses built-in ``round`` which does banker's rounding — good enough
    for display prices.  For ledger-grade rounding, switch to
    ``decimal.Decimal``.

    >>> round_to_cents(1.005)
    1.0
    >>> round_to_cents(3.14159)
    3.14
    """
    # ponytail: built-in round; use decimal.ROUND_HALF_UP if auditors care
    return round(n, 2)


def quote(item: dict[str, Any]) -> float:
    """Return the item's base price rounded to cents.

    >>> quote({"price": 12.3456})
    12.35
    """
    return round_to_cents(base_price(item))


def net_price(item: dict[str, Any], pct: float) -> float:
    """Apply a *pct* percent discount to *item* and return the result.

    *pct* is expressed as a plain number (e.g. 10 for 10 %).  The
    discount is clamped to [0, 100] so callers can't accidentally
    invert a price or make it free-and-then-some.

    Uses ``base_price`` to pull the raw value, then rounds through
    ``round_to_cents``.

    >>> net_price({"price": 100.0}, 25)
    75.0
    >>> net_price({"price": 50.0}, 0)
    50.0
    """
    pct = max(0.0, min(float(pct), 100.0))
    raw = base_price(item)
    discounted = raw * (1 - pct / 100)
    return round_to_cents(discounted)


def bulk_price(items: list[dict[str, Any]], pct: float = 0.0) -> float:
    """Sum the net prices of every item in *items*.

    Each item's price is obtained via ``base_price``, discounted by
    *pct* percent through ``net_price``, and the total is rounded
    once at the end by ``round_to_cents``.

    Returns ``0.0`` for an empty list — no items, no charge.

    >>> bulk_price([{"price": 10}, {"price": 20}], pct=10)
    27.0
    >>> bulk_price([])
    0.0
    """
    if not items:
        return 0.0
    total = sum(net_price(item, pct) for item in items)
    return round_to_cents(total)


def tax_price(n: float, rate: float) -> float:
    """Add tax at *rate* percent to amount *n*.

    *rate* is a percentage (e.g. 8.25 for 8.25 % sales tax).
    Negative rates are clamped to zero — tax refunds are a different
    workflow.

    >>> tax_price(100.0, 8.25)
    108.25
    >>> tax_price(0.0, 10)
    0.0
    """
    rate = max(0.0, float(rate))
    return round_to_cents(n * (1 + rate / 100))


# ------------------------------------------------------------------
# convenience helpers (all route through the core five above)
# ------------------------------------------------------------------

def line_item(item: dict[str, Any], pct: float = 0.0,
              tax_rate: float = 0.0) -> dict[str, Any]:
    """Build a receipt-style dict for one item.

    Pulls the starting figure from ``base_price``, applies discount
    via ``net_price``, then tax via ``tax_price``.  Every number is
    rounded to cents.

    >>> li = line_item({"name": "gizmo", "price": 80}, pct=25, tax_rate=10)
    >>> li["base"]
    80.0
    >>> li["final"]
    66.0
    """
    raw = base_price(item)
    after_discount = net_price(item, pct)
    after_tax = tax_price(after_discount, tax_rate)
    return {
        "base": round_to_cents(raw),
        "discount_pct": pct,
        "after_discount": after_discount,
        "tax_rate": tax_rate,
        "final": after_tax,
    }


def invoice_total(items: list[dict[str, Any]], pct: float = 0.0,
                  tax_rate: float = 0.0) -> float:
    """Grand total for a list of items after discount and tax.

    Each item goes through ``base_price`` → ``net_price`` → ``tax_price``,
    then the results are summed and rounded once.

    >>> invoice_total([{"price": 100}, {"price": 200}], pct=10, tax_rate=5)
    283.5
    """
    subtotal = bulk_price(items, pct)
    return tax_price(subtotal, tax_rate)
