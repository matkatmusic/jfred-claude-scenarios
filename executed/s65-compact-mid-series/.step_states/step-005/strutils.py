def reverse(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    return sum(c in 'aeiouAEIOU' for c in s)

def capitalize_words(s):
    return s.title()
