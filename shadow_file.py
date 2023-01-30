import hashlib
import base64

iterations = 454545
salt = base64.b64decode("VGhpcyBpcyBhIG1lc3NhZ2UgdG8gYmUgZW5jcnlwdGVkLg==".encode())
password = "password".encode()
value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
print(base64.b64encode(value))