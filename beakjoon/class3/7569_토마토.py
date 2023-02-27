import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().rstrip().split(" "))
moveable = [[1, 0, 0], [-1, 0, 0], [0, -1, 0],
            [0, 1, 0], [0, 0, 1], [0, 0, -1]]

farm = list()
visited = list()
queue = deque([])

for h in range(H):
    yLine = list()
    yFarm = list()
    for n in range(N):
        line = list(map(int, input().rstrip().split(" ")))
        xLine = list()
        for m in range(M):
            if line[m] == 0:
                xLine.append(0)
            elif line[m] == 1:
                xLine.append(1)
                queue.append([h, n, m])
            else:
                xLine.append(1)
        yLine.append(xLine)
        yFarm.append(line)
    visited.append(yLine)
    farm.append(yFarm)


def isMoveable(z, y, x, map, visited):
    if (M > x >= 0 and N > y >= 0 and H > z >= 0 and map[z][y][x] == 0 and visited[z][y][x] == 0):
        return True
    return False


def BFS(queue, map, visited):
    while (queue):
        pos = queue.popleft()
        for i in moveable:
            currentZ = pos[0] + i[0]
            currentY = pos[1] + i[1]
            currentX = pos[2] + i[2]
            if (isMoveable(currentZ, currentY, currentX, map, visited)):
                map[currentZ][currentY][currentX] = map[pos[0]
                                                        ][pos[1]][pos[2]] + 1
                visited[currentZ][currentY][currentX] = 1
                queue.append([currentZ, currentY, currentX])
    return map


farm = BFS(queue, farm, visited)
failedFlag = False
maxDay = 0
for yFarm in farm:
    for l in yFarm:
        if 0 in l:
            print(-1)
            exit()
        maxDay = max(maxDay, max(l))

print(maxDay-1)
