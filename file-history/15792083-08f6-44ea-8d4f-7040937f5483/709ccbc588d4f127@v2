"""
Billing module.

Provides helpers for building simple orders:
pricing, stock checks, discounts, and formatting.
"""


def calc_tot(items):
    """Sum price * qty for each item in the list.

    Args:
        items: list of dicts, each with "price" (float) and "qty" (int).

    Returns:
        float: total price across all items.
    """
    return sum(item["price"] * item["qty"] for item in items)


def fmt_money(n):
    """Format a number as a dollar string.

    Args:
        n: numeric value to format.

    Returns:
        str: formatted as "$X.XX", e.g. "$9.99".
    """
    return f"${n:.2f}"


def chk_stock(item, qty):
    """Check whether the requested qty is available in stock.

    Args:
        item: dict with a "stock" key (int).
        qty: requested quantity (int).

    Returns:
        bool: True if qty <= item["stock"].
    """
    return qty <= item["stock"]


def apply_disc(total, pct):
    """Apply a percentage discount to a total.

    Args:
        total: original total (float).
        pct: discount percentage, e.g. 10 for 10%.

    Returns:
        float: discounted total.
    """
    return total * (1 - pct / 100)


def mk_order(items):
    """Build an order dict from a list of items.

    Computes the subtotal, checks stock for every item,
    and bundles everything into a single order structure.

    Args:
        items: list of dicts, each with "name", "price", "qty", "stock".

    Returns:
        dict with keys:
            - "items": the input list
            - "subtotal": result of calc_tot
            - "subtotal_fmt": formatted subtotal string
            - "all_in_stock": bool, True if every item passes chk_stock
    """
    subtotal = calc_tot(items)
    return {
        "items": items,
        "subtotal": subtotal,
        "subtotal_fmt": fmt_money(subtotal),
        "all_in_stock": all(chk_stock(i, i["qty"]) for i in items),
    }


if __name__ == "__main__":
    sample = [
        {"name": "Widget", "price": 9.99, "qty": 2, "stock": 10},
        {"name": "Gadget", "price": 24.50, "qty": 1, "stock": 5},
    ]
    order = mk_order(sample)
    assert order["subtotal"] == 9.99 * 2 + 24.50
    assert order["subtotal_fmt"] == "$44.48"
    assert order["all_in_stock"] is True
    assert apply_disc(100, 10) == 90.0
    assert fmt_money(0) == "$0.00"
    print("OK")
