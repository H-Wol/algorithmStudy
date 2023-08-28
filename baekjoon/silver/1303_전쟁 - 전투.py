from sys import stdin
from collections import deque

input = stdin.readline


def move(y, x):
    return (
        [y - 1, x],
        [y, x - 1],
        [y, x + 1],
        [y + 1, x],
    )


def isMoveAble(y: int, x: int, map: list, visited: list, compare: str):
    if M > y >= 0 and N > x >= 0 and map[y][x] == compare and visited[y][x] == False:
        return True
    return False


def BFS(y, x, map, visited):
    if visited[y][x] == True:
        return 0, map[y][x]
    queue = deque([[y, x]])
    visited[y][x] = True
    power = 1
    standard = map[y][x]
    while queue:
        curY, curX = queue.popleft()
        for ny, nx in move(curY, curX):
            if isMoveAble(ny, nx, map, visited, standard):
                visited[ny][nx] = True
                power += 1
                queue.append([ny, nx])
    return power * power, standard


N, M = map(int, input().rsplit())

field = []
visited = []
for _ in range(M):
    field.append(list(input().rstrip()))
    visited.append([False for _ in range(N)])


powers = {"W": 0, "B": 0}
for y in range(M):
    for x in range(N):
        power, alliance = BFS(y, x, field, visited)
        powers[alliance] += power

print(powers["W"])
print(powers["B"])
