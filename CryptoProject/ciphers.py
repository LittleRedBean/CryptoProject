from FastExpo import *
from euclid_functions import *
from utilities import *

def El_gamal(mode: str, plaintext: str, ciphertext:int, publickey: int, privatekey: int, prime: int):
    if mode=="e":
        """
        Alice will comput (x*((b^lr) mod p)) mod p. Computing Ciphertext
        """
        plaintext_int=str_to_int(plaintext)
        fast_exp_result=fast_exp(publickey,privatekey,prime)
        ciphertext = (plaintext_int * fast_exp_result) % prime
        #print(f"plaintext * FastExpo_result{FastExpo_result}:{plaintext * FastExpo_result}")
        return print(f"Ciphertext is {ciphertext}")
    elif mode == "d":
        """
        Bob will compute [(b^r mod p)^l mod p]^-1 * (x*((b^lr) mod p)) mod p
        Find ((b^r)mod p)^l inverse first
        """
        fast_exp_result=fast_exp(publickey,privatekey,prime)
        inverse=modinv(fast_exp_result,prime)
        #print(f"inverse:{inverse}")
        #print(f"FastExpo_result{FastExpo_result}")
        plaintext_int=(inverse * ciphertext) % prime
        plaintext=int_to_str(plaintext_int)
        return print(f"Plaintext is {plaintext}")

def RSA_encrypt(prime: int, publickey: int, plaintext: str):
    plaintext_int=str_to_int(plaintext)
    return print(f"Your ciphertext is {fast_exp(plaintext_int,publickey,prime)}")

def RSA_decrypt(prime: int, privatekey: int, ciphertext: int):
    plaintext_int=fast_exp(ciphertext,privatekey,prime)
    return print(f"Your plaintext is {int_to_str(plaintext_int)}")
     

def RSA(mode: str, plaintext: str, ciphertext:int, publickey: int, privatekey: int, prime: int):
    if mode=="e":
        return RSA_encrypt(prime,publickey,plaintext)
    elif mode=="d":
        return RSA_decrypt(prime,privatekey,ciphertext)
