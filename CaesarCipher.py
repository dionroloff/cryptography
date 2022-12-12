import sys

def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWYWZ"
    key = {}
    count = 0
    for c in letters:
        key[c] = letters[(count + n) % len(letters)]
        count += 1
    return key

def encrypt_message(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def get_num():
    num = input("Pick a number to shift the plaintext: ")
    if num[0] == '-':
        print("That is a negative number.")
        sys.exit(1)
    try:
        n = int(num)
        return n
    except:
        print("That is not a number.")
        sys.exit(1)
    
num = get_num() 
key = generate_key(num)
message = input("Please write the message to be encrypted: ").upper()
cipher = encrypt_message(key, message)
print("Ciphertext:\n", cipher)