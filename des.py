from pyDes import *

def modify(cipher):
    mod = [0] * len(cipher)
    mod[8] = 1
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

message = "This is a message."
key = "DECRYPTS"
iv = bytes([0] * 8)
# CBC mode makes the message XOR'd with IV before encryption
k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
cipher = k.encrypt(message)

print("Length of plaintext: ", len(message))
print("Length of ciphertext: ", len(cipher))
print("Encrypted: ", cipher[0:8])
print("Encrypted: ", cipher[8:16])
print("Encrypted: ", cipher[16:])

cipher = modify(cipher)
print("Modified cipher: ", cipher)

messge = k.decrypt(cipher)
print("Decrypted: ", message)