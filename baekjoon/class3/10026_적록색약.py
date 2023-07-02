import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

moveable = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def isMoveable(y, x, map, color):
    if (N > x >= 0 and N > y >= 0 and map[y][x][1] == False and map[y][x][0] == color):
        return True
    return False


origin = []

for _ in range(N):
    origin.append(input().rstrip())

# [color, visited]
grid = []

for ori in origin:
    tmp = []
    for color in ori:
        tmp.append([color, False])
    grid.append(tmp)


def BFS(y, x, map):
    hasRegion = False
    if (isMoveable(y, x, map, map[y][x][0])):
        hasRegion = True
        queue = deque([[y, x]])
        standardColor = map[y][x][0]
        map[y][x][1] = True
        while (queue):
            pos = queue.popleft()
            for i in moveable:
                currentY = pos[0] + i[0]
                currentX = pos[1] + i[1]
                if (isMoveable(currentY, currentX, map, standardColor)):
                    map[currentY][currentX][1] = True
                    queue.append([currentY, currentX])
    return hasRegion, map


realRegions = 0

for y in range(N):
    for x in range(N):
        hasRegion, grid = BFS(y, x, grid)
        if hasRegion:
            realRegions += 1

grid = []

for ori in origin:
    tmp = []
    for color in ori:
        if color == "R":
            tmp.append(["G", False])
        else:
            tmp.append([color, False])
    grid.append(tmp)

redGreenRegion = 0

for y in range(N):
    for x in range(N):
        hasRegion, grid = BFS(y, x, grid)
        if hasRegion:
            redGreenRegion += 1

print(realRegions, redGreenRegion)
