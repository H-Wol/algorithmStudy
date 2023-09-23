from collections import defaultdict
from sys import stdin

input = stdin.readline


n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().rsplit())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start):
    visited = set()
    queue = []
    visited.add(start)
    queue.append(start)
    cnt = 0

    while queue and cnt < 2:
        next_level = []
        for node in queue:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_level.append(neighbor)
        queue = next_level
        cnt += 1

    return visited - {start}


friends = bfs(graph, 1)
print(len(friends))
