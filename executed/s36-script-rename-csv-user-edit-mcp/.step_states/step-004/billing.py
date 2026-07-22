"""
Billing utilities.

Prices are floats. Items are dicts with at minimum "price", "qty",
and optionally "stock" keys. Discounts are percentages (0-100).
"""


def calc_tot(items):
    """Sum of price * qty for each item in the list.

    Args:
        items: list of dicts, each with "price" (float) and "qty" (int).

    Returns:
        float: the total before discounts.

    Raises:
        ValueError: if any item has negative price or qty.
    """
    total = 0.0
    for item in items:
        price = item["price"]
        qty = item["qty"]
        if price < 0 or qty < 0:
            raise ValueError(f"Negative value: price={price}, qty={qty}")
        total += price * qty
    return total


def fmt_money(n):
    """Format a number as a dollar string.

    Args:
        n: numeric value to format.

    Returns:
        str: formatted as "$X.XX", e.g. "$9.99".
             Negative values get "$-X.XX".
    """
    if n < 0:
        return f"$-{abs(n):.2f}"
    return f"${n:.2f}"


def chk_stock(item, qty):
    """Check whether the requested qty is available in stock.

    Args:
        item: dict with a "stock" key (int).
        qty: requested quantity (int).

    Returns:
        bool: True if qty <= item["stock"], False otherwise.
    """
    return qty <= item["stock"]


def apply_disc(total, pct):
    """Apply a percentage discount to a total.

    Args:
        total: pre-discount amount (float).
        pct: discount percentage, 0-100. Values outside
             this range are clamped.

    Returns:
        float: the discounted total.
    """
    # ponytail: clamp instead of raising — caller doesn't need to guard
    pct = max(0, min(100, pct))
    return total * (1 - pct / 100)


def validate(items):
    """Raise ValueError if any item lacks a "price" key.

    Args:
        items: list of item dicts.

    Returns:
        True if all items valid.

    Raises:
        ValueError: if any item is missing "price".
    """
    for item in items:
        if "price" not in item:
            raise ValueError(f"Item missing 'price' key: {item}")
    return True


def gen_invoice(items, disc_pct=0):
    """Build a plain-text invoice string.

    Args:
        items: list of item dicts with "name", "price", "qty".
        disc_pct: optional discount percentage (0-100).

    Returns:
        str: multi-line invoice with line items, subtotal,
             discount (if any), and final total.
    """
    lines = ["INVOICE", "=" * 40]
    subtotal = calc_tot(items)

    for item in items:
        line_total = item["price"] * item["qty"]
        lines.append(
            f"  {item['name']:<20} "
            f"{item['qty']:>3} x {fmt_money(item['price']):>8} = "
            f"{fmt_money(line_total):>10}"
        )

    lines.append("-" * 40)
    lines.append(f"  {'Subtotal':<30} {fmt_money(subtotal):>10}")

    if disc_pct > 0:
        final = apply_disc(subtotal, disc_pct)
        lines.append(f"  {'Discount (' + str(disc_pct) + '%)':<30} {fmt_money(subtotal - final):>10}")
        lines.append(f"  {'Total':<30} {fmt_money(final):>10}")
    else:
        lines.append(f"  {'Total':<30} {fmt_money(subtotal):>10}")

    lines.append("=" * 40)
    return "\n".join(lines)


if __name__ == "__main__":
    sample = [
        {"name": "Widget", "price": 9.99, "qty": 3, "stock": 10},
        {"name": "Gadget", "price": 24.50, "qty": 1, "stock": 5},
    ]
    assert calc_tot(sample) == 9.99 * 3 + 24.50
    assert fmt_money(9.99) == "$9.99"
    assert fmt_money(0) == "$0.00"
    assert chk_stock(sample[0], 10) is True
    assert chk_stock(sample[0], 11) is False
    assert apply_disc(100, 25) == 75.0
    print(gen_invoice(sample, disc_pct=10))
    print("\nAll assertions passed.")
