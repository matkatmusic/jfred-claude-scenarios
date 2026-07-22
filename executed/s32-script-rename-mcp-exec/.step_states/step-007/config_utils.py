"""Minimal nested-dict config helpers.

All key arguments support dot-notation for nested access
(e.g. ``"db.host"`` reaches ``cfg["db"]["host"]``).
"""


def _walk(cfg, parts):
    """Traverse *cfg* along *parts*, returning (parent_dict, final_key).

    Raises KeyError if an intermediate segment is missing.
    """
    node = cfg
    for p in parts[:-1]:
        node = node[p]
    return node, parts[-1]


def _split(key):
    """Split a dot-notation key into segments."""
    return key.split(".")


def get_value(cfg, key, default=None):
    """Return the value at *key*, or *default* if missing.

    Supports dot-notation for nested lookups::

        get_value(cfg, "db.host")  # cfg["db"]["host"]
    """
    try:
        node, last = _walk(cfg, _split(key))
        return node.get(last, default)
    except (KeyError, TypeError, AttributeError):
        return default


def set_value(cfg, key, value):
    """Set *key* to *value*, creating intermediate dicts as needed.

    ::

        set_value(cfg, "db.port", 5432)
        # cfg == {"db": {"port": 5432}}
    """
    parts = _split(key)
    node = cfg
    for p in parts[:-1]:
        if p not in node or not isinstance(node[p], dict):
            node[p] = {}
        node = node[p]
    node[parts[-1]] = value


def delete_value(cfg, key):
    """Remove *key* from *cfg*.

    Raises KeyError if the key does not exist.
    """
    node, last = _walk(cfg, _split(key))
    del node[last]


def has_val(cfg, key):
    """Return True if *key* exists in *cfg*."""
    try:
        node, last = _walk(cfg, _split(key))
        return last in node
    except (KeyError, TypeError):
        return False


def merge_val(a, b):
    """Deep-merge dict *b* into dict *a* (mutates *a*). Returns *a*.

    Non-dict values in *b* overwrite those in *a*.
    Sub-dicts are merged recursively::

        merge_val({"x": {"y": 1}}, {"x": {"z": 2}})
        # {"x": {"y": 1, "z": 2}}
    """
    for k, v in b.items():
        if k in a and isinstance(a[k], dict) and isinstance(v, dict):
            merge_val(a[k], v)
        else:
            a[k] = v
    return a


def get_or_default(cfg, key, default):
    """Return the value at *key* if it exists, otherwise *default*."""
    if has_val(cfg, key):
        return get_value(cfg, key)
    return default


def apply_overrides(cfg, overrides):
    """Apply *overrides* dict to *cfg*, printing each change."""
    for key, new in overrides.items():
        old = get_value(cfg, key)
        print(f"overriding {key}: {old} -> {new}")
        set_value(cfg, key, new)


def flatten_val(cfg, prefix=""):
    """Flatten a nested dict into dot-notation keys.

    ::

        flatten_val({"a": {"b": 1, "c": 2}})
        # {"a.b": 1, "a.c": 2}
    """
    out = {}
    for k, v in cfg.items():
        full = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten_val(v, full))
        else:
            out[full] = v
    return out
