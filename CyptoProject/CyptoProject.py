import argparse
from pydoc import plain
from random import choices
from euclid_functions import *
from FastExpo import *
from ciphers import *

def main():
    parser = argparse.ArgumentParser(description="Project for Diffie-Hellman Key Exchange Protocaol and RSA")
    # positional arguments (required)
    parser.add_argument("-CipherType", choices=["DH","RSA"], default="DH", help="You can type in DH for Diffie-Hellman, or RSA")
    parser.add_argument("-mode", choices=["d","e"], default="d", help="You can type in d for decrpytion mode or encryption mode")
    parser.add_argument("--plaintext", "-p", type=int, help="Enter the string that you want to encrypt")
    parser.add_argument("--ciphertext", "-c", type=int, help="Enter the string that you want to decrypt")
    # Alice will publish (b, b^r% P). Alice will comput "(x*((b^lr) mod p)) mod p" and send it to bob. l is the public key, r is the private key. b is the generator.
    parser.add_argument("-generator", type=int, help="Enter your generator")
    parser.add_argument("-privatekey", type=int, help="Enter your private key")
    parser.add_argument("-publickey", type=int, help="Enter your public key")
    parser.add_argument("-Prime", type=int, help="Enter your Prime number")
    # optional arguments 
    parser.add_argument("--verbose", "-v", action="store_true", help="show each step of the Euclidean algorithm")

    args=parser.parse_args()

    CipherType=args.CipherType
    mode=args.mode
    generator=args.generator
    Prime=int(
    "822981df504ae0f1ec3e170c655da066c59d35925b12d50da01386ceb99e06fe"
    "297011dcbbf79d7d1805a8c64b7c1fb67cd3d54b3187b71a97ff7f758bf2f1e3", 16)
    privatekey=args.privatekey
    publickey=args.publickey
    plaintext=args.plaintext
    ciphertext=args.ciphertext

    if CipherType == "DH":
        return El_gamal(mode,plaintext, ciphertext, publickey,privatekey, Prime)
    elif CipherType == "RSA":
        return
if __name__ == "__main__":
    main()