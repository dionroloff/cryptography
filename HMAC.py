import hashlib

secret_key = "secret key".encode()
message = "Hello, this is a message.".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(message)
hmac = sha256.digest()

print(message, hmac)