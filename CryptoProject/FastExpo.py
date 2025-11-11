def fast_exp(base: int, exp: int, mod: int) -> int:
    """
    Fast exponentiation (Exponentiation by Squaring)
    Computes (base ** exp) % mod efficiently.
    If mod is None, computes normal power.
    """
    result = 1
    base = base % mod if mod else base  # handle modulus if provided

    while exp > 0:
        if exp % 2 == 1:  # if exponent is odd
            result = (result * base) % mod if mod else result * base
        exp //= 2
        base = (base * base) % mod if mod else base * base

    return result
