"""List utilities."""


def flatten(nested):
    """Flatten a list of lists into a single list."""
    return [x for sub in nested for x in sub]


def unique(items):
    """Return items with duplicates removed, preserving order."""
    return list(dict.fromkeys(items))


def chunk(items, size):
    """Split a list into sublists of the given size.

    The last chunk may contain fewer than `size` elements if the list
    length is not evenly divisible.

    Args:
        items: The list to split.
        size: Maximum number of elements per chunk.

    Returns:
        A list of sublists.
    """
    return [items[i:i + size] for i in range(0, len(items), size)]
