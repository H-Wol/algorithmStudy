from sys import stdin
from collections import deque

input = stdin.readline


def cantor_set(n):
    if n == 0:
        return "-"
    else:
        length = 3 ** (n - 1)
        return cantor_set(n - 1) + " " * length + cantor_set(n - 1)


while True:
    try:
        n = int(input())
        print(cantor_set(n))
    except EOFError:
        break
