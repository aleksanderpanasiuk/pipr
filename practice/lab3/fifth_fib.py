def fibonacci(n):
    if 0 == n:
        return 0
    if 1 == n or 2 == n:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))
