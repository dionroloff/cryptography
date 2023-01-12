import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key
    
    def random(self):
        self.next = (1103515245 * self.next + 12345) % 2 ** 31
        return self.next
    
    def get_key_byte(self):
        return self.random() % 256

def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def flip_bit(cipher, probability):
    b = []
    for c in cipher:
        if random.randrange(0, probability) == 0:
            # flip one of the 8 bits
            c = c ^ 2 ** random.randrange(0, 8)
        b.append(c)
    return bytes(b)

key = KeyStream(10)
message = "This is a message.".encode()
print(message)
cipher = encrypt(key, message)
print(cipher)

cipher = flip_bit(cipher, 5)

key = KeyStream(10)
message = encrypt(key, cipher)
print(message)