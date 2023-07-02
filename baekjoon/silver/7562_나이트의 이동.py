from sys import stdin
from collections import deque

input = stdin.readline

T = int(input())


def moveable(y, x):
    return (
        [y + 2, x - 1],
        [y + 1, x - 2],
        [y - 1, x - 2],
        [y - 2, x - 1],
        [y + 2, x + 1],
        [y + 1, x + 2],
        [y - 1, x + 2],
        [y - 2, x + 1],
    )


def isMoveable(y, x, map, L):
    if L > x >= 0 and L > y >= 0 and map[y][x] == 0:
        return True
    return False


def BFS(y, x, targetY, targetX, map, L):
    returnList = []
    if isMoveable(y, x, map, L):
        queue = deque([[y, x]])
        map[y][x] = 1
        while queue:
            posY, posX = queue.popleft()
            for currentY, currentX in moveable(posY, posX):
                if currentY == targetY and currentX == targetX:
                    returnList.append(map[posY][posX])
                    continue
                if isMoveable(currentY, currentX, map, L):
                    map[currentY][currentX] = map[posY][posX] + 1
                    queue.append([currentY, currentX])
    return min(returnList)


for _ in range(T):
    L = int(input())
    board = [[0] * L for _ in range(L)]
    startY, startX = map(int, input().split())
    targetY, targetX = map(int, input().split())
    if startY == targetY and startX == targetX:
        print(0)
        continue
    print(BFS(startY, startX, targetY, targetX, board, L))
