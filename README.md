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

## test cases
### test case1:
- Prime number: 23
- generator: 5
- message: 2
- Alice publish (5, 5^6 mod 23) => (5,8), that is Alice's private key is 6
- Bob publish (5, 5^15 mod 23) => (5,19), that is Bob's private key is 15

## Usage

Example: `python .\CyptoProject.py -CipherType DH -m e -Prime 23 -generator 5 -privatekey 6 -publickey 19 -p 2`