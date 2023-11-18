from sys import stdin

input = stdin.readline

R, C, K = map(int, input().split())

board = [input().rstrip() for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


def dfs(x, y, count):
    global result

    if x == 0 and y == C - 1:
        if count == K:
            result += 1
        return

    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and board[nx][ny] == '.':
            dfs(nx, ny, count + 1)

    visited[x][y] = False


dfs(R - 1, 0, 1)
print(result)
