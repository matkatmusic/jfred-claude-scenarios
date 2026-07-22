"""Build text reports from shape data using geo_core primitives."""

from geo_core import rectangle_area, rectangle_perimeter, box_volume


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
        lines.append(f"  rectangle_area  = {rectangle_area(w, h)}")
        lines.append(f"  rectangle_perimeter = {rectangle_perimeter(w, h)}")
        if "d" in s:
            lines.append(f"  box_volume   = {box_volume(w, h, s['d'])}")
    return "\n".join(lines)


def summary_line(shape):
    """Return a one-line summary with rectangle_area and volume for a shape.

    Args:
        shape: Dict with keys 'name', 'w', 'h', and optional 'd'.

    Returns:
        A string like "Box: rectangle_area=12, box_volume=60" (box_volume omitted if no 'd').
    """
    w, h = shape["w"], shape["h"]
    parts = [f"{shape['name']}: rectangle_area={rectangle_area(w, h)}"]
    if "d" in shape:
        parts.append(f"box_volume={box_volume(w, h, shape['d'])}")
    return ", ".join(parts)


def totals(shapes):
    """Return summed rectangle_area and box_volume across all shapes.

    Args:
        shapes: List of shape dicts with 'w', 'h', and optional 'd'.

    Returns:
        Dict with 'total_area' and 'total_volume' keys.
    """
    total_area = sum(rectangle_area(s["w"], s["h"]) for s in shapes)
    total_volume = sum(box_volume(s["w"], s["h"], s["d"]) for s in shapes if "d" in s)
    return {"total_area": total_area, "total_volume": total_volume}
