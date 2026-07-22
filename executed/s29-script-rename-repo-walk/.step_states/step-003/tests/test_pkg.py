"""Tests for the data-loading compute_value."""

from pkg.a import compute_value


def test_helper_normalises_string():
    """compute_value strips whitespace and lowercases strings."""
    assert compute_value("  Hello  ") == "hello"


def test_helper_passes_through_non_strings():
    """compute_value returns non-string values unchanged."""
    assert compute_value(42) == 42
