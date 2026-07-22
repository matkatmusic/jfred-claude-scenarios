"""Build text reports from shape data using geo_core primitives."""

from geo_core import area, perim, vol


def build_report(shapes):
    """Produce a text report for a list of shapes.

    Each shape is a dict with keys 'name', 'w', 'h', and optional 'd'.
    If 'd' is present, volume is included.

    Args:
        shapes: List of shape dicts.

    Returns:
        A multi-line string report.
    """
    lines = []
    for s in shapes:
        w, h = s["w"], s["h"]
        lines.append(f"{s['name']}:")
        lines.append(f"  area  = {area(w, h)}")
        lines.append(f"  perim = {perim(w, h)}")
        if "d" in s:
            lines.append(f"  vol   = {vol(w, h, s['d'])}")
    return "\n".join(lines)
