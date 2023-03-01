import sys
from collections import deque
input = sys.stdin.readline

C = int(input())


N = int(input())
nodes = [[]for _ in range(C+1)]
visited = [0] * (C+1)

for _ in range(N):
    F, T = map(int, input().split(" "))
    nodes[F].append(T)
    nodes[T].append(F)


def BFS(v):
    cnt = 0
    visited[v] = 1
    queue = deque([v])

    while (queue):
        for i in nodes[queue.popleft()]:
            if (visited[i] == 0):
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt


print(BFS(1))
