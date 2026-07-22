"""Greeting utilities."""


def greet(name):
    """Return a greeting for name."""
    return "Hello, " + name


def farewell(name):
    """Return a farewell for name."""
    return "Goodbye, " + name


if __name__ == "__main__":
    print(greet("world"))
