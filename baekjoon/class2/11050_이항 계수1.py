import sys


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1


N, K = map(int, sys.stdin.readline().split(" "))

print(int(factorial(N) / (factorial(N-K) * factorial(K))))
