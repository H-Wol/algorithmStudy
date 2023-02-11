import sys
sys.setrecursionlimit(10 ** 9)


# dfs 탐색
def DFS(x, y):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = y + b
            DFS(a, y + b)


n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y, l = map(int, sys.stdin.readline().split())
    graph[x].append([y, l])
    graph[y].append([x, l])

visited = [-1] * (n + 1)
visited[1] = 0
DFS(1, 0)

start = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[start] = 0
DFS(start, 0)

print(max(visited))
