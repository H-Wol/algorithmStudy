from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))


def dfs(node, depth, distance):
    visited[node] = True
    depth_list[node] = depth
    distance_list[node] = distance

    for next_node, next_distance in graph[node]:
        if not visited[next_node]:
            dfs(next_node, depth + 1, distance + next_distance)


for _ in range(m):
    visited = [False] * (n + 1)
    depth_list = [0] * (n + 1)
    distance_list = [0] * (n + 1)
    start, end = map(int, input().split())

    dfs(start, 0, 0)
    print(distance_list[end])
