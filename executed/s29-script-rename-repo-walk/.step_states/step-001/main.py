"""
Entry point that exercises the data-loading pipeline.

Imports :func:`pkg.a.helper` directly and uses it inside
:func:`run` to normalise raw text input.
"""

from pkg.a import helper


def run(text):
    """Normalise a raw text value.

    Delegates to :func:`pkg.a.helper` for the actual
    normalisation (strip whitespace, lowercase strings).

    Args:
        text: A raw text value to normalise.

    Returns:
        The normalised value.
    """
    return helper(text)


if __name__ == "__main__":
    sample = "  Hello, World  "
    print(f"Input:  {sample!r}")
    print(f"Output: {run(sample)!r}")
