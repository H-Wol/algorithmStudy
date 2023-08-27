from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().rsplit())

paper = []


def move(y, x):
    return (
        [y - 1, x],
        [y, x - 1],
        [y, x + 1],
        [y + 1, x],
    )


def isMoveAble(y: int, x: int, map: list, visited: list) -> bool:
    if N > y >= 0 and M > x >= 0 and map[y][x] == 1 and visited[y][x] == False:
        return True
    return False


def BFS(y, x, map, visited):
    if not isMoveAble(y, x, map, visited):
        return 0
    queue = deque([[y, x]])
    visited[y][x] = True
    size = 1
    while queue:
        curY, curX = queue.popleft()
        for ny, nx in move(curY, curX):
            if isMoveAble(ny, nx, map, visited):
                visited[ny][nx] = True
                size += 1
                queue.append([ny, nx])
    return size


for _ in range(N):
    heights = list(map(int, input().rsplit()))
    paper.append(heights)

answers = 0

visited = [[False for _ in range(M)] for _ in range(N)]
regions = 0
for y in range(N):
    for x in range(M):
        region = BFS(y, x, paper, visited)
        if region > 0:
            regions += 1
            answers = answers if answers > region else region

print(regions)
print(answers)
