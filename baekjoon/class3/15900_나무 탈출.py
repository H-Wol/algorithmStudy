from collections import deque
from sys import stdin

input = stdin.readline


def bfs(start):
    queue = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True

    total_depth = 0

    while queue:
        node, depth = queue.popleft()

        is_leaf = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                is_leaf = False
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))

        if is_leaf:
            total_depth += depth

    return total_depth


N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs(1)
if result % 2 == 0:
    print("No")
else:
    print("Yes")
