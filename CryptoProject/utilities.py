
from FastExpo import *
from primes import *
from euclid_functions import *

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
    random RSA keys
    """
    if cipherType == "RSA":
        return genKey_RSA(bits,privatekey)
    elif cipherType == "DH":
        return genKey_DH(bits,privatekey,Prime,generator)