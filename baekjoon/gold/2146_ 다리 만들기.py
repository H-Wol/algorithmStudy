from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
maps = [list(map(int, input().rsplit())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def check_island_bfs(y, x, maps, visited, island_num):
    queue = deque([(y, x)])
    maps[y][x] = island_num
    visited[y][x] = True
    islands = [(y, x)]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and maps[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                maps[ny][nx] = island_num
                queue.append((ny, nx))
                islands.append((ny, nx))
    return maps, visited, islands


def check_bridge_len_bfs(queue, maps, visited, island_num):
    bridge_len = 0
    while queue:
        loop_cnt = len(queue)
        for _ in range(loop_cnt):
            y, x = queue.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if maps[ny][nx] == 0:
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                        continue
                    if maps[ny][nx] != island_num:
                        return bridge_len
        bridge_len += 1
    return 200


island_num = 1
total_island = []
for y in range(N):
    for x in range(N):
        if maps[y][x] == 1 and not visited[y][x]:
            maps, visited, islands = check_island_bfs(
                y, x, maps, visited, island_num)
            total_island.append(islands)
            island_num += 1

min_bridge_len = 200
for idx, island in enumerate(total_island):
    visited = [[False] * N for _ in range(N)]
    for landY, landX in island:
        visited[landY][landX] = True
    cur_len = check_bridge_len_bfs(deque(island), maps, visited, idx+1)
    min_bridge_len = min_bridge_len if min_bridge_len < cur_len else cur_len
print(min_bridge_len)
