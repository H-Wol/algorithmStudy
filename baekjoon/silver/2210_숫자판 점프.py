from sys import stdin

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

input = stdin.readline
board = [input().split() for _ in range(5)]
result = set()


def dfs(x, y, number):
    if len(number) == 6:
        result.add(number)
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, number + board[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(result))
