"""Euclid Functions"""
def gcd_euclid(a: int, b: int) -> int:
    """Greatest common divisor via iterative Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int):
    """
    Extended Euclidean algorithm.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y

    return old_r, old_x, old_y


def modinv(a: int, m: int):
    """
    M	0odular inverse of a modulo m (i.e., a*x ≡ 1 (mod m)).
    Raises ValueError if inverse does not exist (when gcd(a, m) != 1).
    """
    g, x, _ = extended_gcd(a, m)
    if g != 1 and g != -1:
        raise ValueError(f"No modular inverse: gcd({a}, {m}) = {g} ≠ 1")
    return x % m

