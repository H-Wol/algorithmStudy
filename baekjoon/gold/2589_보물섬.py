from sys import stdin
from collections import deque

input = stdin.readline
R, C = map(int, input().split())
treasure_map = [list(input()) for _ in range(R)]

max_distance = 0


def bfs(grid, start):
    R, C = len(grid), len(grid[0])
    visited = [[False] * C for _ in range(R)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    distance = 0

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "L" and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
        distance += 1

    return distance - 1  # 시작 지점을 제외하고 계산


for r in range(R):
    for c in range(C):
        if treasure_map[r][c] == "L":
            max_distance = max(max_distance, bfs(treasure_map, (r, c)))

print(max_distance)
