
from FastExpo import *
from primes import *

def GenPrime(bits: int):
    p = generate_prime(bits)
    print(f"Random {bits}-bit prime: {p}")

    p_safe, q = generate_safe_prime(bits)
    print("\nSafe prime p:", p_safe)
    print("q:", q)

    g = find_generator_safe_prime(p_safe, q)
    print("Generator g:", g)
    return p, p_safe, q , g

def str_to_int(plaintext: str):
    plaintext_bytes = plaintext.encode('utf-8')
    plaintext_int = int.from_bytes(plaintext_bytes, byteorder='big')
    return plaintext_int

def int_to_str(number: int):
    length= (number.bit_length() + 7)//8
    plaintext_bytes=number.to_bytes(length,byteorder='big')
    plaintext=plaintext_bytes.decode('utf-8')
    return plaintext

def GenPubKey(generator:int,privatekey:int,Prime:int):
    return fast_exp(generator,privatekey,Prime)