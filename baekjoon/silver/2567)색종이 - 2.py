from sys import stdin
from collections import deque

input = stdin.readline


N = int(input())


board = [[0] * 101 for _ in range(101)]


for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1


perimeter = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < 101 and 0 <= ny < 101 and board[nx][ny] == 0:
                    perimeter += 1

print(perimeter)
