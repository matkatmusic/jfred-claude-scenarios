"""Inventory management utilities."""


def add_item(store, item):
    """Append an item to the store list."""
    store.append(item)


def remove_item(store, name):
    """Remove the first item from *store* whose ``"name"`` matches *name*."""
    store[:] = [i for i in store if i["name"] != name]
