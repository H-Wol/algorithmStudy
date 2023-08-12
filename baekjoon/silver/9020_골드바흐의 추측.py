from sys import stdin

input = stdin.readline


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


def solve(n):
    for i in range(n // 2, 1, -1):
        if is_prime(i) and is_prime(n - i):
            return i, n - i


t = int(input())

for _ in range(t):
    n = int(input())
    a, b = solve(n)
    print(a, b)
