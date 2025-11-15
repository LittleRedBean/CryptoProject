import random #generate random candidate primes using Miller-Rabin

def is_probable_prime(n: int, k: int = 10) -> bool:
    """Return True if n is probably prime, False if definitely composite."""
    if n < 2:
        return False

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n in small_primes:
        return True
    if any(n % p == 0 for p in small_primes):
        return False

    # write n-1 as 2^r * d with d odd
    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2
        
#Miller–Rabin loop
        
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

#generate prime

def generate_prime(bits: int = 64) -> int:
    """Generate a probable prime with given bit length."""
    if bits < 2:
        raise ValueError("bits must be >= 2")
    while True:
        # set top and bottom bits so it's the right size and odd
        n = random.getrandbits(bits)
        n |= (1 << (bits - 1)) | 1
        if is_probable_prime(n):
            return n

#generate safe prime
        
def generate_safe_prime(bits: int = 64):
    """
    Generate a safe prime p = 2q + 1 (and q).
    bits is for p. Use this for Diffie–Hellman.
    """
    if bits < 3:
        raise ValueError("bits must be >= 3 for a safe prime")
    while True:
        q = generate_prime(bits - 1)
        p = 2 * q + 1
        if is_probable_prime(p):
            return p, q
        
#find the generator 

def find_generator_safe_prime(p: int, q: int) -> int:
    """
    Find a generator g for the subgroup of order q in Z_p*,
    assuming p = 2q + 1 is safe prime.
    """
    if 2 * q + 1 != p:
        raise ValueError("p must be 2q + 1 (safe prime).")
    while True:
        g = random.randrange(2, p - 1)
        # g is good if it doesn't generate the small subgroups
        if pow(g, 2, p) != 1 and pow(g, q, p) != 1:
            return g

