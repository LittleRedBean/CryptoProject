# 🔐 CryptoProject

A Python-based cryptography tool implementing **Diffie–Hellman key exchange** and **RSA encryption/decryption**.  
This project was developed as part of the *CS789 Cryptography* course at Boston University.

## 🧠 Features
- Diffie–Hellman (DH) key exchange simulation
- RSA encryption and decryption support

## ⚙️ Requirements
- Python 3.9 or later
- Visual Studio / VS Code (optional)
- `argparse` (built-in)

## test cases:
Prime number: 23
generator: 5
message: 2
Alice publish (5, 5^6 mod 23) => (5,8), that is Alice's private key is 6
Bob publish (5, 5^15 mod 23) => (5,19), that is Bob's private key is 15

## Usage

  -h, --help            show this help message and exit
  -CipherType {DH,RSA}  You can type in DH for Diffie-Hellman, or RSA
  -mode {d,e}           You can type in d for decrpytion mode or encryption mode
  --plaintext, -p PLAINTEXT
                        Enter the string that you want to encrypt
  --ciphertext, -c CIPHERTEXT
                        Enter the string that you want to decrypt
  -generator GENERATOR  Enter your generator
  -privatekey PRIVATEKEY
                        Enter your private key
  -publickey PUBLICKEY  Enter your public key
  -Prime PRIME          Enter your Prime number
  --verbose, -v         show each step of the Euclidean algorithm
  
Example: python .\CyptoProject.py -t DH -m e -P 23 -b 5 -r 6 --publickey 19 -p 2