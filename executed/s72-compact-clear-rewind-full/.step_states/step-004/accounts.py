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


def balance_of(acct):
    """Return the account's balance."""
    return acct["balance"]
