"""Email validation."""

import re

# ponytail: one regex covers 99% of real addresses; RFC 5322 full grammar is a mass grave of edge cases nobody sends from
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_email(s):
    """Return True if `s` looks like an email address."""
    return bool(_EMAIL_RE.match(s))


if __name__ == "__main__":
    assert is_email("a@b.com")
    assert not is_email("nope")
    assert not is_email("@no.com")
    assert not is_email("a@b")
    print("ok")
