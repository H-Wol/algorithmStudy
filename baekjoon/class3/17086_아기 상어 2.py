from sys import stdin
from collections import deque

input = stdin.readline


def isMoveAble(y, x, map):
    if 0 <= y < N and 0 <= x < M and map[y][x] == 0:
        return True
    return False


def BFS(N, M, spaces):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    queue = deque()
    for y in range(N):
        for x in range(M):
            if spaces[y][x] == 1:
                queue.append((y, x))

    max_distance = 0
    distance = 0
    while queue:
        loop_cnt = len(queue)
        distance += 1
        for _ in range(loop_cnt):
            y, x = queue.popleft()

            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if isMoveAble(ny, nx, spaces):
                    spaces[ny][nx] = 1
                    max_distance = max(max_distance, distance)
                    queue.append((ny, nx))

    return max_distance


N, M = map(int, input().split())
spaces = [list(map(int, input().split())) for _ in range(N)]

result = BFS(N, M, spaces)
print(result)
