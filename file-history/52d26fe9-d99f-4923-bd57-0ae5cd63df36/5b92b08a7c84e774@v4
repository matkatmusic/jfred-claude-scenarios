"""String utilities — thin wrappers around Python stdlib str methods.

Each function is deliberately a one-liner. If you need the stdlib method
directly, use it — these exist for consistent naming across the codebase.
"""
# ponytail: every function here is a stdlib one-liner; module exists because it was requested

import re


def capitalize(s):
    """Capitalize the first character of a string.

    >>> capitalize('hello world')
    'Hello world'
    >>> capitalize('')
    ''
    """
    return s.capitalize()


def lowercase(s):
    """Lowercase the entire string.

    >>> lowercase('Hello World')
    'hello world'
    >>> lowercase('ABC')
    'abc'
    """
    return s.lower()


def uppercase(s):
    """Uppercase the entire string.

    >>> uppercase('hello')
    'HELLO'
    >>> uppercase('already UP')
    'ALREADY UP'
    """
    return s.upper()


def reverse(s):
    """Reverse a string.

    >>> reverse('abc')
    'cba'
    >>> reverse('')
    ''
    """
    return s[::-1]


def strip(s):
    """Strip leading and trailing whitespace.

    >>> strip('  hello  ')
    'hello'
    >>> strip('no-space')
    'no-space'
    """
    return s.strip()


def pad_right(s, n):
    """Right-pad_right string with spaces to width n.

    >>> pad_right('hi', 5)
    'hi   '
    >>> pad_right('long enough', 3)
    'long enough'
    """
    return s.ljust(n)


def count(s, ch):
    """Count occurrences of ch in s.

    >>> count('banana', 'a')
    3
    >>> count('hello', 'z')
    0
    """
    return s.count(ch)


def index_of(s, ch):
    """Return index of first occurrence of ch, or -1 if not found.

    >>> index_of('hello', 'l')
    2
    >>> index_of('hello', 'z')
    -1
    """
    return s.find(ch)


def replace(s, a, b):
    """Replace all occurrences of a with b in s.

    >>> replace('hello world', 'world', 'there')
    'hello there'
    >>> replace('aaa', 'a', 'b')
    'bbb'
    """
    return s.replace(a, b)


def split(s, sep):
    """Split s by separator.

    >>> split('a,b,c', ',')
    ['a', 'b', 'c']
    >>> split('hello', ',')
    ['hello']
    """
    return s.split(sep)


def join(parts, sep):
    """Join parts with separator.

    >>> join(['a', 'b', 'c'], ',')
    'a,b,c'
    >>> join([], '-')
    ''
    """
    return sep.join(parts)


def slugify(s):
    """Lowercase, strip, replace spaces with hyphens, drop non-alnum chars.

    >>> slugify('Hello World!')
    'hello-world'
    >>> slugify('  Lots   of   spaces  ')
    'lots---of---spaces'
    """
    return re.sub(r'[^a-z0-9-]', '', s.lower().strip().replace(' ', '-'))


def normalize(s):
    """Trim whitespace and lowercase.

    >>> normalize('  Hello World  ')
    'hello world'
    """
    return lowercase(strip(s))
