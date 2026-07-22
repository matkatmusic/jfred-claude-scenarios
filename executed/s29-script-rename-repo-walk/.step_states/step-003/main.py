"""
Entry point that exercises the data-loading pipeline.

Imports :func:`pkg.a.compute_value` directly and uses it inside
:func:`run` to normalise raw text input.
"""

from pkg.a import compute_value


def run(text):
    """Normalise a raw text value.

    Delegates to :func:`pkg.a.compute_value` for the actual
    normalisation (strip whitespace, lowercase strings).

    Args:
        text: A raw text value to normalise.

    Returns:
        The normalised value.
    """
    return compute_value(text)


if __name__ == "__main__":
    sample = "  Hello, World  "
    print(f"Input:  {sample!r}")
    print(f"Output: {run(sample)!r}")
