"""Order and billing utilities.

Helpers for calculating totals, formatting currency, checking stock,
building orders, applying discounts, computing tax, parsing line input,
and summarizing orders.
"""

TAX_RATE = 0.08
CURRENCY = "USD"


def validate_items(items):
    """Raise ValueError if any item is missing 'price' or 'qty'."""
    for i, item in enumerate(items):
        for key in ("price", "qty"):
            if key not in item:
                raise ValueError(f"Item {i} missing '{key}'")
    return True


def calculate_total(items):
    """Return the sum of price * qty for every item in the list."""
    return sum(item["price"] * item["qty"] for item in items)


def format_currency(n):
    """Format a number as a dollar string like '$12.50'."""
    return f"${n:.2f}"


def check_stock(item, qty):
    """Return True if the requested qty is available in item's stock."""
    return qty <= item["stock"]


def order_line(item):
    """Return a one-line summary string for an item."""
    total = format_currency(item["price"] * item["qty"])
    in_stock = "In Stock" if check_stock(item, item["qty"]) else "Low Stock"
    return f"{item['name']}: {item['qty']} x {format_currency(item['price'])} = {total} [{in_stock}]"


def build_order(items):
    """Build an order dict with items, subtotal, tax, and total."""
    subtotal = calculate_total(items)
    order_tax = tax(subtotal)
    return {
        "items": items,
        "subtotal": subtotal,
        "tax": order_tax,
        "total": subtotal + order_tax,
        "currency": CURRENCY,
    }


def apply_discount(total, pct):
    """Return the total after applying a percentage discount.

    pct is a number between 0 and 100.
    """
    return total * (1 - pct / 100)


def apply_loyalty(total, member):
    """Return formatted total with a loyalty discount if member is True."""
    discounted = apply_discount(total, 10) if member else total
    return format_currency(discounted)


def tax(total):
    """Return the tax amount for a given total."""
    return total * TAX_RATE


def parse_line(line):
    """Parse a comma-separated 'name,price,qty' string into a dict.

    Returns a dict with keys 'name' (str), 'price' (float), 'qty' (int).
    """
    parts = line.strip().split(",")
    return {
        "name": parts[0],
        "price": float(parts[1]),
        "qty": int(parts[2]),
    }


def summarize(order):
    """Return a multi-line text summary of an order.

    Uses calculate_total, format_currency, and tax to build the summary.
    """
    lines = []
    lines.append("Order Summary")
    lines.append("=" * 40)

    for item in order["items"]:
        name = item.get("name", "Unknown")
        line_total = item["price"] * item["qty"]
        lines.append(f"  {name}: {item['qty']} x {format_currency(item['price'])} = {format_currency(line_total)}")

    subtotal = calculate_total(order["items"])
    order_tax = tax(subtotal)
    total = subtotal + order_tax

    lines.append("-" * 40)
    lines.append(f"  Subtotal: {format_currency(subtotal)}")
    lines.append(f"  Tax ({TAX_RATE:.0%}): {format_currency(order_tax)}")
    lines.append(f"  Total ({CURRENCY}): {format_currency(total)}")
    lines.append("=" * 40)

    return "\n".join(lines)


if __name__ == "__main__":
    sample_items = [
        {"name": "Widget", "price": 9.99, "qty": 2, "stock": 10},
        {"name": "Gadget", "price": 24.95, "qty": 1, "stock": 5},
    ]
    order = build_order(sample_items)
    print(summarize(order))
    print()
    print(f"After 10% discount: {format_currency(apply_discount(order['total'], 10))}")
    print(f"Widget in stock for 3? {check_stock(sample_items[0], 3)}")
    print(f"Parsed line: {parse_line('Bolt,1.50,100')}")
