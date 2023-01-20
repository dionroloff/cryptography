# (g**b mod p)**a = (g**b)**a mod p = g**(ab) mod p
import math
import random

def is_prime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def get_prime(size):
    while True:
        prime = random.randrange(size, 2*size)
        if is_prime(prime):
            return prime

def is_generator(g, prime):
    for i in range(1, prime - 1):
        if (g**1) % prime == 1:
            return False
    return True

def get_generator(prime):
    for g in range(2, prime):
        if is_generator(g, prime):
            return g

p = get_prime(10000)
g = get_generator(p)
print(g, p)