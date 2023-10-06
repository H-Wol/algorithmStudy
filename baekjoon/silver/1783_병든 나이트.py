from sys import stdin

input = stdin.readline


def max_knight_moves(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return min(4, (m + 1) // 2)
    elif m < 7:
        return min(4, m)
    else:
        return m - 2


n, m = map(int, input().split())
result = max_knight_moves(n, m)
print(result)
