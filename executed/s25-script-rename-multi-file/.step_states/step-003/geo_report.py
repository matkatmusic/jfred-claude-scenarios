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


def summary_line(shape):
    """Return a one-line summary with area and volume for a shape.

    Args:
        shape: Dict with keys 'name', 'w', 'h', and optional 'd'.

    Returns:
        A string like "Box: area=12, vol=60" (vol omitted if no 'd').
    """
    w, h = shape["w"], shape["h"]
    parts = [f"{shape['name']}: area={area(w, h)}"]
    if "d" in shape:
        parts.append(f"vol={vol(w, h, shape['d'])}")
    return ", ".join(parts)
