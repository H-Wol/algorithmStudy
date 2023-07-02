import math
from sys import stdin

input = stdin.readline


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime(i):
            count += 1

    print(count)
