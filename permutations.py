import cProfile

def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1) * n

def counter(n):
    count = 0
    for i in range(n):
        count += 1
    return count