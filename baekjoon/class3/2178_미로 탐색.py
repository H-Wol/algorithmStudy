import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split(" "))

movable = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def isMoveable(y, x, map, visited):
    if (M > x >= 0 and N > y >= 0 and map[y][x] == '1' and visited[y][x] == 0):
        return True
    return False


map = list()
visited = list()
for _ in range(N):
    map.append(list(input().rstrip()))
    visited.append([0 for _ in range(M)])


def BFS(y, x, map, visited):
    visited[y][x] = 1
    queue = deque([[y, x]])

    while queue:
        curY, curX = queue.popleft()
        for nextY, nextX in movable:
            y = curY + nextY
            x = curX + nextX
            if isMoveable(y, x, map, visited):
                if y == N-1 and x == M-1:
                    return visited[curY][curX] + 1
                visited[y][x] = visited[curY][curX] + 1
                queue.append([y, x])
    return 0


print(BFS(0, 0, map, visited))
