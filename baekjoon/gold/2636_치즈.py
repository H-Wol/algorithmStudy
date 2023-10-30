from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().rsplit())
plate = []
change_plate = []
visited = []
cheese_cnt = 0
for _ in range(N):
    plate.append(list(map(int, input().split())))
    cheese_cnt += plate[-1].count(1)


def bfs(y, x, map, new_map, visited):
    queue = deque([(y, x)])
    visited[y][x] = True
    melt_cnt = 0
    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            ny, nx = cy + dy, cx + dx
            if is_valid(ny, nx, visited):
                visited[ny][nx] = True
                if map[ny][nx] == 1:
                    if new_map[ny][nx] == 1:
                        new_map[ny][nx] = 0
                        melt_cnt += 1
                    continue
                queue.append((ny, nx))
    return melt_cnt, new_map


def is_valid(y, x, visited):
    if 0 <= y < N and 0 <= x < M and not visited[y][x]:
        return True
    return False


change_plate = plate

hour = 0
while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    melted_cheese_cnt, change_plate = bfs(0, 0, plate, change_plate, visited)
    hour += 1
    if cheese_cnt == melted_cheese_cnt:
        print(hour)
        print(cheese_cnt)
        exit()
    cheese_cnt -= melted_cheese_cnt
    plate = change_plate
