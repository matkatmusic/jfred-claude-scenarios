"""Tests for the data-loading helper."""

from pkg.a import helper


def test_helper_normalises_string():
    """helper strips whitespace and lowercases strings."""
    assert helper("  Hello  ") == "hello"


def test_helper_passes_through_non_strings():
    """helper returns non-string values unchanged."""
    assert helper(42) == 42
