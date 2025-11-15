import math
from FastExpo import *
from euclid_functions import *
from utilities import *

def cracker_DH(b,a,p):
    """
    Solve b^x = a (mod p), using Baby-step Gian-step Algorithm
    """
    # find a(b^-1)^im=b^j

    m = int(math.ceil(math.sqrt(p)))

    baby_steps = []
    # b^j
    for j in range(0,m):
        tmp = fast_exp(b,j,p)
        baby_steps.append(tmp)

    inv=modinv(b,p)
    # (b^-1)^m
    binvm = fast_exp(inv,m,p)

    # a(b^-1)^im
    for i in range(0,m):
        target = (a * fast_exp(binvm,i,p)) % p
        _,j=find_first_match(baby_steps,target)
        # print(f"value test, j {j}")
        if j != None:
            break

    if j is None:
        return print("can't find a solution for find a(b^-1)^im=b^j, cracking failed")
    else:
        return print(f"Your i*m + j is: {i}*{m} + {j} = {i*m + j}")


def cracker_RSA(Prime: int, publickey: int, ciphertext: int):
    """
    Crack small RSA modulus:
    - factor Prime = n into p, q
    - compute phi
    - recover private key d
    - decrypt ciphertext
    """
    # 1) factor n (Prime)
    import math
    n = Prime
    p = None
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            p = i
            break
    if p is None:
        return print("Failed to factor n; cracking aborted.")
    q = n // p

    phi = (p - 1) * (q - 1)
    d = modinv(publickey, phi)

    plaintext_int = fast_exp(ciphertext, d, n)
    plaintext = int_to_str(plaintext_int)

    print(f"Cracked RSA!")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"Recovered private key d = {d}")
    print(f"Recovered plaintext = {plaintext}")

 

    return
def cracker():
    return