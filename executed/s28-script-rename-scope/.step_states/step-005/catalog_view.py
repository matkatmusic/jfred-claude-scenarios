"""Render a catalog directory as formatted text."""

import catalog


def render(path):
    """Load the catalog at *path* and return a human-readable string summary."""
    entries = catalog.load_catalog(path)
    summary = catalog.summarize(entries)

    lines = [f"Catalog: {summary['total']} entries ({summary['active']} active)"]

    if summary["price_min"] is not None:
        lines.append(f"Price range: {summary['price_min']:.2f} - {summary['price_max']:.2f}")

    if summary["tags"]:
        lines.append(f"Tags: {', '.join(summary['tags'])}")

    lines.append("")
    for entry in entries:
        status = "*" if entry.get("active") else " "
        lines.append(f"  [{status}] {entry['name']} (${entry['price']:.2f})")

    return "\n".join(lines)


def preview(path):
    """Return a short preview of the first few catalog entries."""
    entries = catalog.load_catalog(path)
    names = [e["name"] for e in entries[:5]]
    suffix = f" (+{len(entries) - 5} more)" if len(entries) > 5 else ""
    return ", ".join(names) + suffix
