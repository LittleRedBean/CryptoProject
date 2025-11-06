import argparse
from pydoc import plain
from random import choices
from euclid_functions import *
from FastExpo import *

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
    Prime=args.Prime
    privatekey=args.privatekey
    publickey=args.publickey
    

    if CipherType == "DH":
        if mode=="e" and args.plaintext is None:
            parser.error("Encryption mode requires --plaintext.")
        else:
            # Alice will comput (x*((b^lr) mod p)) mod p. Computing Ciphertext
            plaintext=args.plaintext
            FastExpo_result=fast_exp(publickey,privatekey,Prime)
            ciphertext = (plaintext * FastExpo_result) % Prime
            print(f"plaintext * FastExpo_result{FastExpo_result}:{plaintext * FastExpo_result}")
            return print(f"Ciphertext is {ciphertext}")
        if mode == "d" and args.ciphertext is None:
            parser.error("Encryption mode requires --ciphertext.")
        else:
            # Bob will compute [(b^r mod p)^l mod p]^-1 * (x*((b^lr) mod p)) mod p
            # Find ((b^r)mod p)^l inverse first
            FastExpo_result=fast_exp(publickey,privatekey,Prime)
            inverse=modinv(FastExpo_result, Prime)
            print(f"inverse:{inverse}")
            print(f"FastExpo_result{FastExpo_result}")
            ciphertext=args.ciphertext
            plaintext=(inverse * ciphertext) % Prime
            return print(f"Plaintext is tests{plaintext}")
    elif CipherType == "RSA":
        return
if __name__ == "__main__":
    main()