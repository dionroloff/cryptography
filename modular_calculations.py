# (g**b mod p)**a = (g**b)**a mod p = g**(ab) mod p
import math
import random

def is_prime(n):
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            return False
    return True

def get_prime(size):
    while True:
        prime = random.randrange(size, 2*size)
        if is_prime(prime):
            return prime

print(get_prime(1000))