from FastExpo import *
from euclid_functions import *
def El_gamal(mode: str, plaintext: int, ciphertext:int, publickey: int, privatekey: int, Prime: int):
    if mode=="e":
        # Alice will comput (x*((b^lr) mod p)) mod p. Computing Ciphertext
        FastExpo_result=fast_exp(publickey,privatekey,Prime)
        ciphertext = (plaintext * FastExpo_result) % Prime
        #print(f"plaintext * FastExpo_result{FastExpo_result}:{plaintext * FastExpo_result}")
        return print(f"Ciphertext is {ciphertext}")
    elif mode == "d":
        # Bob will compute [(b^r mod p)^l mod p]^-1 * (x*((b^lr) mod p)) mod p
        # Find ((b^r)mod p)^l inverse first
        FastExpo_result=fast_exp(publickey,privatekey,Prime)
        inverse=modinv(FastExpo_result, Prime)
        #print(f"inverse:{inverse}")
        #print(f"FastExpo_result{FastExpo_result}")
        plaintext=(inverse * ciphertext) % Prime
        return print(f"Plaintext is {plaintext}")   