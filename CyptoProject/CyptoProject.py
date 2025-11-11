import argparse
from pydoc import plain
from random import choices
from euclid_functions import *
from FastExpo import *
from ciphers import *
from utilities import *

def main():
    parser = argparse.ArgumentParser(description="Project for Diffie-Hellman Key Exchange Protocaol and RSA")
    # positional arguments (required)
    parser.add_argument("--CipherType", choices=["DH","RSA"], help="You can type in DH for Diffie-Hellman/El gamal, or RSA")
    parser.add_argument("--utilities", choices=["GenPrime", "Modinv", "StrtoInt", "InttoStr", "GenPubKey"], help="You can use utilities to help you to build your cipher.")
    parser.add_argument("--bits", type=int, help="Enter the bits of your prime number")
    parser.add_argument("--num", type=int, help="Enter your number")
    parser.add_argument("--generator", type=int, help="Enter your generator")
    parser.add_argument("--mode", choices=["d","e"], default="d", help="You can type in d for decrpytion mode or encryption mode")
    parser.add_argument("--plaintext", "-p", type=str, help="Enter the string that you want to encrypt")
    parser.add_argument("--ciphertext", "-c", type=int, help="Enter the string that you want to decrypt")
    # Alice will publish (b, b^r% P). Alice will comput "(x*((b^lr) mod p)) mod p" and send it to bob. l is the public key, r is the private key. b is the generator.
    parser.add_argument("--privatekey", type=int, help="Enter your private key")
    parser.add_argument("--publickey", type=int, help="Enter your public key")
    parser.add_argument("--Prime", type=int, help="Enter your Prime number")
    parser.add_argument("--verbose", "-v", action="store_true", help="show each step of the Euclidean algorithm")

    args=parser.parse_args()

    CipherType=args.CipherType
    mode=args.mode
    Prime=args.Prime
    privatekey=args.privatekey
    publickey=args.publickey
    plaintext=args.plaintext
    ciphertext=args.ciphertext
    util=args.utilities
    bits=args.bits
    num=args.num
    generator=args.generator

    if CipherType != None and util == None:
        if CipherType == "DH":
            return El_gamal(mode,plaintext,ciphertext,publickey,privatekey,Prime)
        elif CipherType == "RSA":
            return
    elif CipherType is None and util != None:
        if util == "GenPrime":
            if bits is None:
                parser.error("--bits is required when using GenPrime")
            else:
                return GenPrime(bits)
        elif util == "Modinv":
            if Prime==None or num==None:
                parser.error("--num and --Prime is required when using Modinv")
            else:
                return print(f"Your module inverse is {modinv(num,Prime)}")
        elif util == "StrtoInt":
            if plaintext == None:
                parser.error("--plaintext is required when using StrtoInt")
            else:
                return print(f"Your converted integer for plaintext is: {str_to_int(plaintext)}")
        elif util == "InttoStr":
            if num == None:
                parser.error("--num is required when using InttoStr")
            else:
                return print(f"Your converted plaintext for integer is: {int_to_str(num)}")
        elif util == "GenPubKey":
            if Prime==None or generator==None or privatekey==None:
                parser.error("--Prime and --generator are required when using GenPubKey")
            else:
                return print(f"Your public key is: {GenPubKey(generator,privatekey,Prime)}")
if __name__ == "__main__":
    main()