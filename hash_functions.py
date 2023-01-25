import hashlib

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

message = "This is a message.".encode()
sha256 = hashlib.sha256()
h = sha256.digest()
print(h)

mm = modify(message)
print(mm)