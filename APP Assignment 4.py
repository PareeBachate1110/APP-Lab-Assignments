import time
from functools import lru_cache

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

start = time.time()
print(fib(35))
end = time.time()

print("Without Using lru_cache: Execution time:", end - start, "seconds")

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

start = time.time()
print(fib(35))
end = time.time()

print("With Using lru_cache: Execution time:", end - start, "seconds")
