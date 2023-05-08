import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split(" "))


walls = list()
visited = list()
for _ in range(N):
    walls.append(list(map(int, list(input().rstrip()))))
    visited.append([[False, False] for _ in range(M)])

movable = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def BFS(y, x, map, visited):
    visited[y][x][1] = True
    dist = 1
    queue = deque([[y, x, True]])
    if y == N - 1 and x == M - 1:
        return dist

    while queue:
        dist += 1
        tasks = len(queue)
        for _ in range(tasks):
            curY, curX, is_not_broken = queue.popleft()
            for nextY, nextX in movable:
                y = curY + nextY
                x = curX + nextX
                if y == N - 1 and x == M - 1:
                    return dist
                if x < 0 or y < 0 or M <= x or N <= y:
                    continue
                if map[y][x] == 0 and not visited[y][x][is_not_broken]:
                    queue.append([y, x, is_not_broken])
                    visited[y][x][is_not_broken] = True
                elif is_not_broken and map[y][x] and not visited[y][x][0]:
                    queue.append([y, x, 0])
                    visited[y][x][0] = True
    return -1


print(BFS(0, 0, walls, visited))
