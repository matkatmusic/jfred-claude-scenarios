"""Tests for config_utils — get_value and set_value."""

from config_utils import get_value, set_value


class TestGetVal:
    def test_flat_key(self):
        assert get_value({"a": 1}, "a") == 1

    def test_nested_key(self):
        assert get_value({"a": {"b": 2}}, "a.b") == 2

    def test_missing_returns_default(self):
        assert get_value({}, "x") is None

    def test_custom_default(self):
        assert get_value({}, "x", 42) == 42

    def test_missing_intermediate(self):
        assert get_value({"a": 1}, "a.b") is None

    def test_deeply_nested(self):
        cfg = {"a": {"b": {"c": {"d": 99}}}}
        assert get_value(cfg, "a.b.c.d") == 99


class TestSetVal:
    def test_flat_key(self):
        cfg = {}
        set_value(cfg, "a", 1)
        assert cfg == {"a": 1}

    def test_nested_creates_intermediates(self):
        cfg = {}
        set_value(cfg, "a.b.c", 3)
        assert cfg == {"a": {"b": {"c": 3}}}

    def test_overwrites_existing(self):
        cfg = {"a": 1}
        set_value(cfg, "a", 2)
        assert cfg == {"a": 2}

    def test_overwrites_non_dict_intermediate(self):
        cfg = {"a": 1}
        set_value(cfg, "a.b", 2)
        assert cfg == {"a": {"b": 2}}

    def test_preserves_siblings(self):
        cfg = {"a": {"x": 10}}
        set_value(cfg, "a.y", 20)
        assert cfg == {"a": {"x": 10, "y": 20}}
