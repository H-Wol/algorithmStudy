from sys import stdin
from collections import deque

input = stdin.readline

N, K = map(int, input().rsplit())

test_tube = []
queues = [deque([]) for _ in range(K + 1)]

for y in range(N):
    test_tube.append(list(map(int, input().rsplit())))
    for x, i in enumerate(test_tube[-1]):
        if i != 0:
            queues[i].append((y, x))

S, X, Y = map(int, input().rsplit())


def isMoveAble(y, x, map):
    if N > y >= 0 and N > x >= 0 and map[y][x] == 0:
        return True
    return False


def BFS(queues, map):
    for _ in range(S):
        for queue in queues:
            for _ in range(len(queue)):
                y, x = queue.popleft()
                if (y, x) == (X - 1, Y - 1):
                    return map[y][x]
                for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ny, nx = y + dy, x + dx
                    if not isMoveAble(ny, nx, map):
                        continue
                    if (ny, nx) == (X - 1, Y - 1):
                        return map[y][x]
                    map[ny][nx] = map[y][x]
                    queue.append((ny, nx))
    return 0


if S == 0:
    print(test_tube[X - 1][Y - 1])
else:
    print(BFS(queues=queues, map=test_tube))
