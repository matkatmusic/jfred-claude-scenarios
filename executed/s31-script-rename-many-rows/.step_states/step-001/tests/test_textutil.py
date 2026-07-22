from textutil import cap, rev, slug


class TestCap:
    def test_basic(self):
        assert cap("hello") == "Hello"

    def test_empty(self):
        assert cap("") == ""

    def test_already_capped(self):
        assert cap("Hello") == "Hello"

    def test_all_lower(self):
        assert cap("hello world") == "Hello world"


class TestRev:
    def test_basic(self):
        assert rev("abc") == "cba"

    def test_empty(self):
        assert rev("") == ""

    def test_palindrome(self):
        assert rev("racecar") == "racecar"

    def test_single_char(self):
        assert rev("x") == "x"


class TestSlug:
    def test_basic(self):
        assert slug("Hello World") == "hello-world"

    def test_special_chars(self):
        assert slug("Hello, World!") == "hello-world"

    def test_leading_trailing_whitespace(self):
        assert slug("  spaced  ") == "spaced"

    def test_empty(self):
        assert slug("") == ""
