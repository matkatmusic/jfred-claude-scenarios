import json
import pytest

import catalog


@pytest.fixture
def catalog_dir(tmp_path):
    """Write sample JSON catalog files and return the directory."""
    (tmp_path / "items.json").write_text(json.dumps([
        {"name": "  Alpha ", "price": 10, "tags": ["a"]},
        {"name": "Beta", "price": "5.5", "tags": ["b", "a"], "active": False},
    ]))
    (tmp_path / "more.json").write_text(json.dumps([
        {"name": "Gamma"},
    ]))
    return tmp_path


def test_load_all_returns_sorted_normalized(catalog_dir):
    entries = catalog.load_all(catalog_dir)
    names = [e["name"] for e in entries]
    assert names == ["alpha", "beta", "gamma"]


def test_load_all_normalizes_defaults(catalog_dir):
    entries = catalog.load_all(catalog_dir)
    gamma = next(e for e in entries if e["name"] == "gamma")
    assert gamma["tags"] == []
    assert gamma["active"] is True
    assert gamma["price"] == 0.0


def test_load_all_coerces_price(catalog_dir):
    entries = catalog.load_all(catalog_dir)
    beta = next(e for e in entries if e["name"] == "beta")
    assert beta["price"] == 5.5
    assert beta["active"] is False


def test_load_all_not_a_dir(tmp_path):
    with pytest.raises(NotADirectoryError):
        catalog.load_all(tmp_path / "nope")


def test_load_all_skips_bad_json(tmp_path):
    (tmp_path / "bad.json").write_text("{not json")
    (tmp_path / "good.json").write_text(json.dumps([{"name": "ok"}]))
    entries = catalog.load_all(tmp_path)
    assert len(entries) == 1


def test_load_all_skips_non_list(tmp_path):
    (tmp_path / "obj.json").write_text(json.dumps({"not": "a list"}))
    assert catalog.load_all(tmp_path) == []
