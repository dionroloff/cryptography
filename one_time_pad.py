import random

# generate random key string and return in as binary
def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range(n)])

# return xor'd key stream and message
def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])

message = input("Type a message to be encrypted: ").encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)
print("Key stream: ", key_stream)
print("Cipher: ", cipher)
print(xor_bytes(key_stream, cipher))