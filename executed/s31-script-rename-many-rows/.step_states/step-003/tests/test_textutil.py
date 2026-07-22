from textutil import capitalize, reverse, slugify


class TestCap:
    def test_basic(self):
        assert capitalize("hello") == "Hello"

    def test_empty(self):
        assert capitalize("") == ""

    def test_already_capped(self):
        assert capitalize("Hello") == "Hello"

    def test_all_lower(self):
        assert capitalize("hello world") == "Hello world"


class TestRev:
    def test_basic(self):
        assert reverse("abc") == "cba"

    def test_empty(self):
        assert reverse("") == ""

    def test_palindrome(self):
        assert reverse("racecar") == "racecar"

    def test_single_char(self):
        assert reverse("x") == "x"


class TestSlug:
    def test_basic(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_chars(self):
        assert slugify("Hello, World!") == "hello-world"

    def test_leading_trailing_whitespace(self):
        assert slugify("  spaced  ") == "spaced"

    def test_empty(self):
        assert slugify("") == ""
