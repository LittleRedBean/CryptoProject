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

## test cases of DH/El_gamal
### test case1:
- Prime number: 23
- generator: 5
- message: 2
- Alice publish (5, 5^6 mod 23) => (5,8), that is Alice's private key is 6
- Bob publish (5, 5^15 mod 23) => (5,19), that is Bob's private key is 15
### test case2: Passed
- prime number: 12373260429731796467
- generator: 10546807778165541197
- Message/Plaintext: "hello"
#### Alice:
- Public Key: 61585494543714566
- Private Key: 461054
#### Bob:
- Public Key: 12258140044862796638
- Private Key: 532147
- See tested command in Test2.txt file, screenshot is named test2.png

## test cases of RSA
### test case1: Passed
- prime number: 198353806820510587300865597006300982661
- Message/Plaintext: "hello"
#### Alice: 
- Public Key: 33530844196292470614850048744593233647
- Pivate Key: 652315

## test cases of DH/El_gamal cracker
### test case1: Passed
- publick key: 44535
- generator: 3578
- prime: 44867
- private key 371 (cracked)

### test case2: Passed
- publick key: 1312691860
- generator: 1628055958
- prime: 3653627807
- private key 371 (cracked)

## Usage

Example: 
- `python .\CryptoProject.py -CipherType DH -m e -Prime 23 -generator 5 -privatekey 6 -publickey 19 -p 2`
- `python .\CryptoProject.py --utilities GenPubKey --Prime 12373260429731796467 --generator 10546807778165541197 --privatekey 461054`
#### Generating random keys for RSA
- `python .\CryptoProject.py --utilities GenKey --CipherType RSA --bits 64 --privatekey 652315`
#### RSA encryption
- `python .\CryptoProject.py --CipherType RSA --mode e --Prime 198353806820510587300865597006300982661 --plaintext hello --publickey 33530844196292470614850048744593233647`
#### RSA decryption
- `python .\CryptoProject.py --CipherType RSA --mode d --Prime 198353806820510587300865597006300982661 --ciphertext 104980963682124885442006657033602004904 --privatekey 652315`
