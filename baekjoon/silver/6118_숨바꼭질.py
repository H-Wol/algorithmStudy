from sys import stdin
from collections import deque

input = stdin.readline


def bfs(start, maps):
    visited = [False] * (len(maps) + 1)
    distance = [0] * (len(maps) + 1)

    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        for neighbor in maps[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    max_distance = max(distance)
    max_index = distance.index(max_distance)

    return max_index, max_distance, distance.count(max_distance)


N, M = map(int, input().split())
maps = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

result = bfs(1, maps)
print(result[0], result[1], result[2])
