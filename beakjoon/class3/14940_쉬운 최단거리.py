import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())


def move(y, x):
    return (
        [y - 1, x],
        [y, x - 1],
        [y, x + 1],
        [y + 1, x],
    )


def isMoveAble(y, x, map, visited):
    if N > y >= 0 and M > x >= 0 and map[y][x] == 1 and (visited[y][x] == -1 or visited[y][x] == 0):
        return True
    return False


maps = []
start_pos = []
visited = []

for i in range(N):
    maps.append(line := list(map(int, input().split())))
    visited.append([0 if i == 0 else -1 for i in line])
    if 2 in line:
        start_pos = [i, line.index(2)]


def BFS(y, x, map, visited):
    queue = deque([[y, x]])
    visited[y][x] = 0
    while queue:
        curY, curX = queue.popleft()
        for ny, nx in move(curY, curX):
            if isMoveAble(ny, nx, map, visited):
                visited[ny][nx] = visited[curY][curX] + 1
                queue.append([ny, nx])
    return visited


for i in BFS(start_pos[0], start_pos[1], maps, visited):
    print(" ".join(map(str, i)))
