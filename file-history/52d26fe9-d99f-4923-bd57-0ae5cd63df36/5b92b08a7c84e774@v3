"""String utilities — thin wrappers around Python stdlib str methods.

Each function is deliberately a one-liner. If you need the stdlib method
directly, use it — these exist for consistent naming across the codebase.
"""
# ponytail: every function here is a stdlib one-liner; module exists because it was requested

import re


def cap(s):
    """Capitalize the first character of a string.

    >>> cap('hello world')
    'Hello world'
    >>> cap('')
    ''
    """
    return s.capitalize()


def low(s):
    """Lowercase the entire string.

    >>> low('Hello World')
    'hello world'
    >>> low('ABC')
    'abc'
    """
    return s.lower()


def up(s):
    """Uppercase the entire string.

    >>> up('hello')
    'HELLO'
    >>> up('already UP')
    'ALREADY UP'
    """
    return s.upper()


def rev(s):
    """Reverse a string.

    >>> rev('abc')
    'cba'
    >>> rev('')
    ''
    """
    return s[::-1]


def trim(s):
    """Strip leading and trailing whitespace.

    >>> trim('  hello  ')
    'hello'
    >>> trim('no-space')
    'no-space'
    """
    return s.strip()


def pad(s, n):
    """Right-pad string with spaces to width n.

    >>> pad('hi', 5)
    'hi   '
    >>> pad('long enough', 3)
    'long enough'
    """
    return s.ljust(n)


def cnt(s, ch):
    """Count occurrences of ch in s.

    >>> cnt('banana', 'a')
    3
    >>> cnt('hello', 'z')
    0
    """
    return s.count(ch)


def idx(s, ch):
    """Return index of first occurrence of ch, or -1 if not found.

    >>> idx('hello', 'l')
    2
    >>> idx('hello', 'z')
    -1
    """
    return s.find(ch)


def rep(s, a, b):
    """Replace all occurrences of a with b in s.

    >>> rep('hello world', 'world', 'there')
    'hello there'
    >>> rep('aaa', 'a', 'b')
    'bbb'
    """
    return s.replace(a, b)


def splt(s, sep):
    """Split s by separator.

    >>> splt('a,b,c', ',')
    ['a', 'b', 'c']
    >>> splt('hello', ',')
    ['hello']
    """
    return s.split(sep)


def joi(parts, sep):
    """Join parts with separator.

    >>> joi(['a', 'b', 'c'], ',')
    'a,b,c'
    >>> joi([], '-')
    ''
    """
    return sep.join(parts)


def slug(s):
    """Lowercase, strip, replace spaces with hyphens, drop non-alnum chars.

    >>> slug('Hello World!')
    'hello-world'
    >>> slug('  Lots   of   spaces  ')
    'lots---of---spaces'
    """
    return re.sub(r'[^a-z0-9-]', '', s.lower().strip().replace(' ', '-'))


def normalize(s):
    """Trim whitespace and lowercase.

    >>> normalize('  Hello World  ')
    'hello world'
    """
    return low(trim(s))
