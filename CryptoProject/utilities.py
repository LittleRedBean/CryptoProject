
from FastExpo import *
from primes import *
from euclid_functions import *
import time
from functools import wraps

def find_first_match(lst, target):
    for i, value in enumerate(lst):
        if value == target:
            return value, i
    return None, None

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
    length = max(1, (number.bit_length() + 7) // 8)
    plaintext_bytes = number.to_bytes(length, byteorder='big')

    try:
        return plaintext_bytes.decode('utf-8')
    except UnicodeDecodeError:
        hex_repr = plaintext_bytes.hex()
        try:
            latin1_text = plaintext_bytes.decode('latin-1')
        except Exception:
            latin1_text = None

        print("[int_to_str] can not decode UTF-8.")
        print(f"[int_to_str] Raw bytes (hex): {hex_repr}")
        if latin1_text is not None:
            print(f"[int_to_str] Latin-1 fallback: {latin1_text!r}")
            
        return hex_repr

def GenPubKey(generator: int, privatekey: int, Prime: int):
    return fast_exp(generator,privatekey,Prime)

def genKey_RSA(bits: int, privatekey: int):

    prime1,_=generate_safe_prime(bits)
    prime2,_=generate_safe_prime(bits)
    Prime = prime1 * prime2
    phi = (prime1-1)*(prime2-1)
    publickey=modinv(privatekey,phi)
    
    print(f"Your prime is {Prime}")
    print(f"Your publickey is {publickey}")
    print(f"Your privatekey is {privatekey}. KEEP THIS TO YOURSELF")
    print(f"Send (Prime: {Prime}, Public key:{publickey}) to Bob")

    return Prime, privatekey, publickey

def genKey_DH(bits: int, privatekey: int, Prime: int, generator: int):
    if Prime == None and generator == None:
        p_safe, q = generate_safe_prime(bits)
        g = find_generator_safe_prime(p_safe, q)
        publickey = fast_exp(g,privatekey,p_safe)
    elif Prime != None and generator != None:
        p_safe = Prime
        g = generator
        publickey = fast_exp(g,privatekey,p_safe)

    print(f"Your prime is {p_safe}")
    print(f"Your publickey is {publickey}")
    print(f"Your privatekey is {privatekey}. KEEP THIS TO YOURSELF")
    print(f"Send (Prime:{p_safe}, Public Key:{publickey}, generator:{g}) to Bob")


    return p_safe, privatekey, publickey

def genKey(cipherType: str, bits: int, privatekey: int, Prime: int, generator: int):
    """
    random RSA keys or DH/El-gamal keys
    """
    if cipherType == "RSA":
        return genKey_RSA(bits,privatekey)
    elif cipherType == "DH":
        return genKey_DH(bits,privatekey,Prime,generator)


def timing(func):
    """
    A decorator that measures the execution time of a function and returns (original result, execution time in seconds).
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time

        return result, execution_time

    return wrapper
