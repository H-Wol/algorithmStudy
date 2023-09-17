from collections import deque
from sys import stdin

input = stdin.readline


def is_valid(y, x, visited, map):
    return 0 <= y < R and 0 <= x < C and not visited[y][x] and map[y][x] != "#"


R, C = map(int, input().split())
farm = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
total_sheep, total_wolf = 0, 0


def bfs(start_y, start_x):
    sheep_count = 0
    wolf_count = 0

    queue = deque()
    queue.append((start_y, start_x))
    visited[start_y][start_x] = True

    while queue:
        y, x = queue.popleft()
        if farm[y][x] == "o":
            sheep_count += 1
        elif farm[y][x] == "v":
            wolf_count += 1

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if is_valid(ny, nx, visited, farm):
                visited[ny][nx] = True
                queue.append((ny, nx))

    if sheep_count > wolf_count:
        return sheep_count, 0
    else:
        return 0, wolf_count


for i in range(R):
    for j in range(C):
        if not visited[i][j] and farm[i][j] != "#":
            sheep, wolf = bfs(i, j)
            total_sheep += sheep
            total_wolf += wolf

print(total_sheep, total_wolf)
