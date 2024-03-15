from sys import stdin

input = stdin.readline


def fibonacci(n):
    fib = [0] * (n + 1)
    if n == 0:
        return 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


n = int(input().strip())
print(fibonacci(n))
