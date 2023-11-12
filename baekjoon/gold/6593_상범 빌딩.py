from collections import deque
from sys import stdin
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

input = stdin.readline


def is_valid(z, y, x, visited, map):
    if 0 <= z < L and 0 <= y < R and 0 <= x < C and not visited[z][y][x] and map[z][y][x] != '#':
        return True
    return False


def bfs(building, visited, start, end):
    time = 0
    queue = deque([start])

    visited[start[0]][start[1]][start[2]] = True

    while queue:

        loop_cnt = len(queue)
        for _ in range(loop_cnt):
            z, y, x = queue.popleft()

            if (z, y, x) == end:
                return time

            for i in range(6):
                nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]

                if is_valid(nz, ny, nx, visited, building):
                    visited[nz][ny][nx] = True
                    queue.append((nz, ny, nx))
        time += 1

    return -1


while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    building = []
    start = end = None

    for i in range(L):
        floor = [list(map(str, input().rstrip())) for _ in range(R)]
        input()
        building.append(floor)
        for j in range(R):
            for k in range(C):
                if floor[j][k] == 'S':
                    start = (i, j, k)
                elif floor[j][k] == 'E':
                    end = (i, j, k)

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    result = bfs(building, visited, start, end)

    if result == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")
