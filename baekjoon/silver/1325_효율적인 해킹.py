from sys import stdin
from collections import deque


n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[b].append(a)

max_count = -1
result = []


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    count = 1

    while queue:
        node = queue.popleft()

        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)
                count += 1

    return count


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    count = bfs(i)

    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

print(" ".join(map(str, result)))
