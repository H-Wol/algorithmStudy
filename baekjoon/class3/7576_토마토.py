import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().rstrip().split(" "))
moveable = [[1, 0], [0, 1], [-1, 0], [0, -1]]

farm = list()
visited = list()
queue = deque([])

for n in range(N):
    line = list(map(int, input().rstrip().split(" ")))
    xLine = list()
    for m in range(M):
        if line[m] == 0:
            xLine.append(0)
        elif line[m] == 1:
            xLine.append(1)
            queue.append([n, m])
        else:
            xLine.append(1)
    visited.append(xLine)
    farm.append(line)


def isMoveable(y, x, map, visited):
    if (M > x >= 0 and N > y >= 0 and map[y][x] == 0 and visited[y][x] == 0):
        return True
    return False


def BFS(queue, map, visited):
    while (queue):
        pos = queue.popleft()
        for i in moveable:
            currentY = pos[0] + i[0]
            currentX = pos[1] + i[1]
            if (isMoveable(currentY, currentX, map, visited)):
                map[currentY][currentX] = map[pos[0]][pos[1]] + 1
                visited[currentY][currentX] = 1
                queue.append([currentY, currentX])
    return map


farm = BFS(queue, farm, visited)
failedFlag = False
maxDay = 0
for y in farm:
    if 0 in y:
        print(-1)
        exit()
    maxDay = max(maxDay, max(y))

print(maxDay-1)
