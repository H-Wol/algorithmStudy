import sys
from collections import deque


def move(y, x):
    return (
        [y - 1, x],
        [y, x - 1],
        [y, x + 1],
        [y + 1, x],
    )


def isMoveAble(y, x, map, visited):
    if N > y >= 0 and M > x >= 0 and map[y][x] != "X" and visited[y][x] == False:
        return True
    return False


def BFS(y, x, map, visited):
    queue = deque([[y, x]])
    cnt = 0
    visited[y][x] = True
    while queue:
        curY, curX = queue.popleft()
        for ny, nx in move(curY, curX):
            if isMoveAble(ny, nx, map, visited):
                if map[ny][nx] == "P":
                    cnt += 1
                visited[ny][nx] = True
                queue.append([ny, nx])
    if cnt == 0:
        return "TT"
    return cnt


maps = []
start_pos = []
visited = []

input = sys.stdin.readline

N, M = map(int, input().split())


for i in range(N):
    maps.append(line := list(input().rstrip()))
    visited.append([False] * M)
    if "I" in line:
        start_pos = [i, line.index("I")]
print(BFS(start_pos[0], start_pos[1], maps, visited))
