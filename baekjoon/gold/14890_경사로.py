from sys import stdin

input = stdin.readline
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def can_place_slope(line, L):
    n = len(line)
    used = [False] * n

    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue
        if abs(line[i] - line[i + 1]) > 1:
            return False
        if line[i] > line[i + 1]:
            for j in range(i + 1, i + 1 + L):
                if j >= n or used[j] or line[i + 1] != line[j]:
                    return False
                used[j] = True
        else:
            for j in range(i, i - L, -1):
                if j < 0 or used[j] or line[i] != line[j]:
                    return False
                used[j] = True
    return True


count = 0

for i in range(N):
    if can_place_slope(board[i], L):
        count += 1

for j in range(N):
    if can_place_slope([board[i][j] for i in range(N)], L):
        count += 1


print(count)
