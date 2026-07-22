def square(n):
    return n * n


def cube(n):
    return n * n * n


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def is_even(n):
    return n % 2 == 0


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
