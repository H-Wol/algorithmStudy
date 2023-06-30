from collections import deque
from sys import stdin

input = stdin.readline
N = int(input())
board = [[0] * N for _ in range(N)]

k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

l = int(input())
directions = {}
for _ in range(l):
    x, c = input().split()
    directions[int(x)] = c

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

nd = {"D": {3: 1, 1: 2, 2: 0, 0: 3}, "L": {3: 0, 0: 2, 2: 1, 1: 3}}


def simulate():
    time = 0
    snake = deque([(0, 0)])
    direction = 3

    while True:
        time += 1
        y, x = snake[0]

        ny = y + dy[direction]
        nx = x + dx[direction]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or (ny, nx) in snake:
            return time

        if board[ny][nx] == 1:
            board[ny][nx] = 0
            snake.appendleft((ny, nx))
        else:
            snake.appendleft((ny, nx))
            snake.pop()

        if time in directions:
            direction = nd[directions[time]][direction]


result = simulate()
print(result)
