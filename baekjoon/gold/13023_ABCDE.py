from sys import stdin

input = stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, visited, v, depth):
    visited[v] = True
    if depth == 4:
        return True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if dfs(graph, visited, neighbor, depth + 1):
                return True

    visited[v] = False
    return False


def find_ABCDE(graph):
    n = len(graph)
    for i in range(n):
        visited = [False] * n
        if dfs(graph, visited, i, 0):
            return 1
    return 0


result = find_ABCDE(graph)
print(result)
