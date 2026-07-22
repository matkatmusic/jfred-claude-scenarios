"""Account management utilities."""


def open_account(name, balance):
    """Create and return a new account dict with the given name and balance."""
    return {"name": name, "balance": balance}


def deposit(acct, amount):
    """Add amount to the account balance and return the account."""
    acct["balance"] += amount
    return acct


def withdraw(acct, amount):
    """Subtract amount from the account balance and return the account.

    Raises ValueError if the withdrawal would make the balance negative.
    """
    if amount > acct["balance"]:
        raise ValueError("Insufficient funds")
    acct["balance"] -= amount
    return acct


def close_account(acct):
    """Close the account by setting its balance to zero.

    Returns the withdrawn amount (the previous balance).
    """
    amount = acct["balance"]
    acct["balance"] = 0
    return amount


def is_overdrawn(acct):
    """Return True if the account balance is below zero."""
    return acct["balance"] < 0


def balance_of(acct):
    """Return the account's balance."""
    return acct["balance"]


def transfer(src, dst, amount):
    """Move amount from src account to dst account."""
    withdraw(src, amount)
    deposit(dst, amount)
# end of accounts module
