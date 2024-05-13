from sys import stdin
from collections import deque

input = stdin.readline

N, M, T = map(int, input().rsplit())

castle = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]


def isMoveAble(y, x, map, visited):
    if N > y >= 0 and M > x >= 0 and map[y][x] != 1 and visited[y][x] == False:
        return True
    return False


def BFS(castle, visited, T):
    time = 0
    gram_time = float("inf")
    if castle[0][0] == 2:
        gram_time = N + M - 2
    queue = deque([(0, 0)])
    visited[0][0] = True
    while queue:
        loop_cnt = len(queue)
        if time > T:
            return "Fail" if gram_time > T else gram_time
        time += 1
        for _ in range(loop_cnt):
            x, y = queue.popleft()
            for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ny, nx = y + dy, dx + x
                if (ny, nx) == (N - 1, M - 1):
                    return min(time, gram_time)
                if not isMoveAble(ny, nx, castle, visited):
                    continue
                if castle[ny][nx] == 2:
                    gram_time = (N - ny) + (M - nx) - 2 + time

                visited[ny][nx] = True
                queue.append((nx, ny))
    return "Fail" if gram_time > T else gram_time


print(BFS(castle, visited, T))
