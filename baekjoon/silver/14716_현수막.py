from sys import stdin
from collections import deque

input = stdin.readline


def bfs(start, visited, banner):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(banner) and 0 <= ny < len(banner[0]) and not visited[nx][ny] and banner[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))


def count_banners(banner):
    visited = [[False] * len(banner[0]) for _ in range(len(banner))]
    count = 0

    for i in range(len(banner)):
        for j in range(len(banner[0])):
            if not visited[i][j] and banner[i][j] == 1:
                bfs((i, j), visited, banner)
                count += 1

    return count


M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]

print(count_banners(banner))
