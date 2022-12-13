import random

def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def get_decrypt_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

key = generate_key()
dkey = get_decrypt_key(key)
message = input("Write the message to be encrypted: ").upper()
cipher = encrypt(key, message)
plaintext = encrypt(dkey, cipher)
print("Cipher\n", cipher)
print("Plaintext\n", plaintext)