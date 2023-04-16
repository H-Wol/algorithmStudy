import sys

a, b, c = map(int, sys.stdin.readline().split(" "))


def pow(C, n, m):
    if n == 1:
        return C % m
    else:
        x = pow(C, n // 2, m)
        if n % 2 == 0:
            return (x * x) % m
        else:
            return (x * x * C) % m


print(pow(a, b, c))
