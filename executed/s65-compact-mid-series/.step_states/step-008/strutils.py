def reverse(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    return sum(c in 'aeiouAEIOU' for c in s)

def capitalize_words(s):
    return s.title()

def strip_digits(s):
    return ''.join(c for c in s if not c.isdigit())
