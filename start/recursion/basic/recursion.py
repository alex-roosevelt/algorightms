from functools import lru_cache

# O(n)
def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)


# With memoization - O(n), without - O(2 in n)
@lru_cache(maxsize=None)
def fibonacchi(num):
    if num in (1, 2):
        return 1
    return fibonacchi(num - 1) + fibonacchi(num - 2)

print(fibonacchi(70))