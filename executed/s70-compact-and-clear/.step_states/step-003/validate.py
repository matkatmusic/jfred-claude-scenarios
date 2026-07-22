"""Email and phone validation."""

import re

# ponytail: one regex covers 99% of real addresses; RFC 5322 full grammar is a mass grave of edge cases nobody sends from
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_email(s):
    """Return True if `s` looks like an email address."""
    return bool(_EMAIL_RE.match(s))


def is_phone(s):
    """Return True if `s` looks like a 10-digit phone number."""
    # ponytail: strips common separators then checks for exactly 10 digits
    digits = re.sub(r"[\s()\-.]", "", s)
    return bool(re.fullmatch(r"\d{10}", digits))


if __name__ == "__main__":
    assert is_email("a@b.com")
    assert not is_email("nope")
    assert not is_email("@no.com")
    assert not is_email("a@b")
    assert is_phone("1234567890")
    assert is_phone("(123) 456-7890")
    assert is_phone("123.456.7890")
    assert not is_phone("123")
    assert not is_phone("12345678901")
    print("ok")
