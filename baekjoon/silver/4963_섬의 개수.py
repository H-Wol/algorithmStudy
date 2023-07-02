import sys
from collections import deque

input = sys.stdin.readline


def moveable(y, x):
    return (
        [y - 1, x],
        [y + 1, x],
        [y, x + 1],
        [y, x - 1],
        [y + 1, x + 1],
        [y + 1, x - 1],
        [y - 1, x + 1],
        [y - 1, x - 1],
    )


def isMoveable(M, N, y, x, map, visited):
    if M > x >= 0 and N > y >= 0 and visited[y][x] == False and map[y][x] == 1:
        return True
    return False


def BFS(M, N, y, x, map, visited):
    isIsland = False
    if isMoveable(M, N, y, x, map, visited):
        visited[y][x] = True
        queue = deque([[y, x]])
        isIsland = True
        while queue:
            pos = queue.popleft()
            for currentY, currentX in moveable(*pos):
                if isMoveable(M, N, currentY, currentX, map, visited):
                    visited[currentY][currentX] = True
                    queue.append([currentY, currentX])
    return isIsland


while True:
    M, N = map(int, input().rstrip().split(" "))
    if M == N == 0:
        break
    field = []
    visited = []

    for _ in range(N):
        field.append(list(map(int, input().rstrip().split(" "))))
        visited.append([False for _ in range(M)])

    cnt = 0
    for x in range(M):
        for y in range(N):
            if BFS(M, N, y, x, field, visited):
                cnt += 1

    print(cnt)
