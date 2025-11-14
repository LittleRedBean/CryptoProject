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



def cracker_RSA():
    return
def cracker():
    return