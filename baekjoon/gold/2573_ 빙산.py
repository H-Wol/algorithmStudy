from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
max_height = 0
sea = []
visited = []

for _ in range(N):
    visited.append([False for _ in range(M)])
    sea.append(list(map(int, input().split())))


def melt_ice(y, x, map):
    if map[y][x] == 0:
        return 0
    cur_height = map[y][x]
    for ny, nx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        if map[ny + y][nx + x] == 0:
            cur_height -= 1
        if cur_height == 0:
            return cur_height

    return cur_height


def bfs(y, x, map, visited):
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            ny, nx = cy + dy, cx + dx
            if is_valid(ny, nx, visited, map):
                visited[ny][nx] = True
                queue.append((ny, nx))


def is_valid(y, x, visited, map):
    if 0 < y < N and 0 < x < M and not visited[y][x] and map[y][x]:
        return True
    return False


year = 0
while True:
    is_checked = False
    new_sea = [sea[0]]
    new_max_height = 0
    for y in range(1, N - 1):
        new_line = [0]
        for x in range(1, M - 1):
            if sea[y][x] == 0:
                new_line.append(0)
                continue
            if year and not visited[y][x]:
                if is_checked:
                    print(year)
                    exit()
                bfs(y, x, sea, visited)
                is_checked = True
            new_line.append(melt_ice(y, x, sea))
        cur_max = max(new_line)
        new_max_height = new_max_height if new_max_height > cur_max else cur_max
        new_line.append(0)
        new_sea.append(new_line)
    if new_max_height == 0:
        print(0)
        exit()
    sea = new_sea
    sea.append(sea[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    year += 1
