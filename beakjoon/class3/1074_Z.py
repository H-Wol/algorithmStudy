import sys

input = sys.stdin.readline

N, r, c = map(int, input().split(" "))

size = 2 ** N


def Z(y, x, size):
    if size == 1:
        return 0
    size //= 2
    result = 0
    if y <= r < y+size and x <= c < x+size:
        result = Z(y, x, size)
    elif y <= r < y+size and x+size <= c:
        result = Z(y, x+size, size) + size*size
    elif y+size <= r and x <= c < x+size:
        result = Z(y+size, x, size) + size*size*2
    elif y+size <= r and x+size <= c:
        result = Z(y+size, x+size, size) + size*size*3
    return result


print(Z(0, 0, size))
