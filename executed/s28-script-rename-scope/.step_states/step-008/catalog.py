"""Catalog loader.

Reads JSON catalog files where each file contains an array of entry objects.
Each entry has at minimum a 'name' key. Entries are normalized on load:
names are lowercased/stripped, missing optional fields get defaults.
"""

import json
from pathlib import Path


def load_catalog(path):
    """Load every .json catalog file under *path*, return a flat list of normalized entries.

    Each JSON file must contain a top-level list of objects.
    Files that fail to parse are skipped with a warning printed to stderr.

    Args:
        path: Directory (str or Path) containing .json catalog files.

    Returns:
        List of normalized entry dicts, sorted by name.
    """
    path = Path(path)
    if not path.is_dir():
        raise NotADirectoryError(f"{path} is not a directory")

    entries = []
    for fp in sorted(path.glob("*.json")):
        try:
            raw = json.loads(fp.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            import sys
            print(f"warning: skipping {fp.name}: {exc}", file=sys.stderr)
            continue

        if not isinstance(raw, list):
            import sys
            print(f"warning: skipping {fp.name}: top-level value is not a list", file=sys.stderr)
            continue

        for item in raw:
            if isinstance(item, dict):
                entries.append(normalize_entry(item))

    entries.sort(key=lambda e: e["name"])
    return entries


def normalize_entry(entry):
    """Normalize a single catalog entry.

    - Strip and lowercase the name.
    - Default 'tags' to an empty list.
    - Default 'active' to True.
    - Coerce 'price' to float if present, else 0.0.
    """
    out = dict(entry)
    out["name"] = str(out.get("name", "")).strip().lower()
    out.setdefault("tags", [])
    out.setdefault("active", True)

    try:
        out["price"] = float(out.get("price", 0))
    except (TypeError, ValueError):
        out["price"] = 0.0

    return out


def filter_active(entries):
    """Return only entries where 'active' is truthy.

    Args:
        entries: List of normalized entry dicts.

    Returns:
        Filtered list (new list, does not mutate input).
    """
    return [e for e in entries if e.get("active")]


def group_by_tag(entries):
    """Group entries by tag. An entry with multiple tags appears in each group.

    Args:
        entries: List of normalized entry dicts.

    Returns:
        Dict mapping tag (str) -> list of entries.
    """
    groups = {}
    for entry in entries:
        for tag in entry.get("tags", []):
            groups.setdefault(tag, []).append(entry)
    return groups


def summarize(entries):
    """Return a compact summary dict for a list of entries.

    Keys:
        total: number of entries
        active: number of active entries
        price_min: lowest price (or None if empty)
        price_max: highest price (or None if empty)
        tags: sorted list of unique tags across all entries

    Args:
        entries: List of normalized entry dicts.

    Returns:
        Summary dict.
    """
    if not entries:
        return {"total": 0, "active": 0, "price_min": None, "price_max": None, "tags": []}

    prices = [e.get("price", 0.0) for e in entries]
    all_tags = set()
    for e in entries:
        all_tags.update(e.get("tags", []))

    return {
        "total": len(entries),
        "active": sum(1 for e in entries if e.get("active")),
        "price_min": min(prices),
        "price_max": max(prices),
        "tags": sorted(all_tags),
    }


def count_entries(path):
    """Return the number of catalog entries under *path*."""
    return len(load_catalog(path))
