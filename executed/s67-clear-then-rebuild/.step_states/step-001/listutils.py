"""List utilities."""


def flatten(nested):
    """Flatten a list of lists into a single list."""
    return [x for sub in nested for x in sub]
