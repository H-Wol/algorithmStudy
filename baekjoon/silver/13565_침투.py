from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
map = [input() for _ in range(N)]

visited = [[False] * M for _ in range(N)]


def bfs(start_x, start_y, map, visited):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()

        if x == N - 1:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and map[nx][ny] == "0" and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return False


for i in range(M):
    if map[0][i] == "0" and not visited[0][i]:
        if bfs(0, i, map, visited):
            print("YES")
            exit(0)

print("NO")
