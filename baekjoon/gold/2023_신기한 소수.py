import math
from sys import stdin

input = stdin.readline

n = int(input())


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def dfs(current, n):
    if len(str(current)) == n:
        print(current)
        return
    for i in range(10):
        next_num = current * 10 + i
        if is_prime(next_num):
            dfs(next_num, n)


for prime in [2, 3, 5, 7]:
    dfs(prime, n)
