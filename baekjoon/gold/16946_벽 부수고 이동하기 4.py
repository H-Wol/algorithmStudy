from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().rsplit())
maps = [list(input().rstrip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

visited_cnts = dict()


def is_valid_to_visit(y: int, x: int, maps, visited) -> bool:
    if 0 <= y < N and 0 <= x < M and maps[y][x] == "0" and not visited[y][x]:
        return True
    return False


def is_not_wall(y: int, x: int, maps) -> bool:
    if 0 <= y < N and 0 <= x < M and maps[y][x] == "0":
        return True
    return False


def bfs(y: int, x: int, maps: list, visited: list, visited_key: int):
    queue = deque([(y, x)])
    visited[y][x] = visited_key
    visited_cnt = 1
    while queue:
        cur_y, cur_x = queue.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_y, next_x = cur_y + dy, cur_x + dx
            if not is_valid_to_visit(next_y, next_x, maps, visited):
                continue
            visited_cnt += 1
            queue.append((next_y, next_x))
            visited[next_y][next_x] = visited_key
    return visited_cnt, visited


visited_key = 1

for y in range(N):
    for x in range(M):
        if not is_valid_to_visit(y, x, maps, visited):
            continue
        cnt, visited = bfs(y, x, maps, visited, visited_key)
        visited_cnts[visited_key] = cnt
        visited_key += 1

new_map = [[] for _ in range(N)]

for y in range(N):
    for x in range(M):
        if maps[y][x] == "1":
            total_visitable_cnt = 0
            visited_key = []
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny, nx = y + dy, x + dx
                if is_not_wall(ny, nx, maps) and visited[ny][nx] not in visited_key:
                    total_visitable_cnt += visited_cnts[visited[ny][nx]]
                    visited_key.append(visited[ny][nx])
            new_map[y].append(str((total_visitable_cnt + 1) % 10))
        else:
            new_map[y].append("0")

for y in range(N):
    print("".join(new_map[y]))
