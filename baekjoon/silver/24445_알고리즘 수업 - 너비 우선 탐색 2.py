from sys import stdin
from collections import deque

input = stdin.readline

N, M, R = map(int, input().rsplit())

node = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)


for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(N + 1):
    node[j].sort(reverse=True)


def BFS(start, node, visited):
    visited_seq = 1
    visited[start] = visited_seq
    queue = deque([start])

    while queue:
        for i in node[queue.popleft()]:
            if visited[i] == 0:
                visited_seq += 1
                visited[i] = visited_seq
                queue.append(i)
    return visited


visited = BFS(R, node, visited)

for i in range(1, N + 1):
    print(visited[i])
