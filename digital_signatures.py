import hashlib

# Public key
n = 123456
message = "This is a message to be hashed."
sha256 = hashlib.sha256()
hash = sha256.digest()
hash = int.from_bytes(hash, "big") % n
print("Hash value: ", hash)