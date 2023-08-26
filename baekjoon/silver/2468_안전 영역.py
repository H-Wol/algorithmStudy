from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

total_heights = []


def move(y, x):
    return (
        [y - 1, x],
        [y, x - 1],
        [y, x + 1],
        [y + 1, x],
    )


def isMoveAble(y: int, x: int, map: list, visited: list, submerged: int):
    if N > y >= 0 and N > x >= 0 and map[y][x] > submerged and visited[y][x] == False:
        return True
    return False


def BFS(y, x, map, visited, submerged):
    if not isMoveAble(y, x, map, visited, submerged):
        return False
    queue = deque([[y, x]])
    has_region = True
    visited[y][x] = True
    while queue:
        curY, curX = queue.popleft()
        for ny, nx in move(curY, curX):
            if isMoveAble(ny, nx, map, visited, submerged):
                visited[ny][nx] = True
                queue.append([ny, nx])
    return has_region


min_height, max_height = 100, 1
for _ in range(N):
    heights = list(map(int, input().rsplit()))
    total_heights.append(heights)
    cur_min, cur_max = min(heights), max(heights)
    min_height = cur_min if min_height > cur_min else min_height
    max_height = cur_max if max_height < cur_max else max_height

answers = 0

for submerged in range(min_height - 1, max_height + 1):
    visited = [[False for _ in range(N)] for _ in range(N)]
    regions = 0
    for y in range(N):
        for x in range(N):
            if BFS(y, x, total_heights, visited, submerged):
                regions += 1
    answers = answers if answers > regions else regions

print(answers)
