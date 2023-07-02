import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split(" "))

nodes = [[]for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    F, T = map(int, input().split(" "))
    nodes[F].append(T)
    nodes[T].append(F)


def BFS(v):
    if visited[v] == 0:
        visited[v] = 1
        queue = deque([v])

        while (queue):
            for i in nodes[queue.popleft()]:
                if (visited[i] == 0):
                    visited[i] = 1
                    queue.append(i)
        return True
    return False


cnt = 0

for i in range(1, N+1):
    if BFS(i):
        cnt += 1

print(cnt)
