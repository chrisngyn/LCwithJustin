"""
F(n) = F(n - 1) + F(n - 2)
0, 1, 1, 2, 3, 5, 8 ...
"""

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
