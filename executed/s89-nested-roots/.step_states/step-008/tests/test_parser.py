from parser import parse_line, count_tokens


class TestParseLine:
    def test_simple_line(self):
        result = parse_line("hello world")
        assert result["raw"] == "hello world"
        assert result["words"] == ["hello", "world"]

    def test_empty_string(self):
        result = parse_line("")
        assert result["raw"] == ""
        assert result["words"] == []

    def test_preserves_raw_whitespace(self):
        result = parse_line("  foo  bar  ")
        assert result["raw"] == "  foo  bar  "
        assert result["words"] == ["foo", "bar"]

    def test_single_word(self):
        result = parse_line("alone")
        assert result["words"] == ["alone"]

    def test_tabs_and_spaces(self):
        result = parse_line("a\tb\t c")
        assert result["words"] == ["a", "b", "c"]

    def test_empty_line(self):
        """A newline-only line preserves the raw string but yields no tokens."""
        result = parse_line("\n")
        assert result["raw"] == "\n"
        assert result["words"] == []


class TestCountTokens:
    def test_multiple_words(self):
        assert count_tokens("one two three") == 3

    def test_empty_string(self):
        assert count_tokens("") == 0

    def test_single_word(self):
        assert count_tokens("solo") == 1

    def test_extra_whitespace(self):
        assert count_tokens("  a  b  ") == 2

    def test_count_tokens_multiword(self):
        """Three-word input returns a count of 3."""
        assert count_tokens("foo bar baz") == 3
