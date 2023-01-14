from pyDes import *

message = "0123456701234567"
key = "DECRYPTS"
iv = bytes([0] * 8)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
cipher = k.encrypt(message)

print("Length of plaintext: ", len(message))
print("Length of ciphertext: ", len(cipher))
print("Encrypted: ", cipher[0:8])
print("Encrypted: ", cipher[8:16])
print("Encrypted: ", cipher[16:])
messge = k.decrypt(cipher)
print("Decrypted: ", message)