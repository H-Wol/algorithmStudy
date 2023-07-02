from sys import stdin

input = stdin.readline


def find_reachable_vertices(graph, start):
    n = len(graph)
    visited = [False] * n
    reachable = [[0] * n for _ in range(n)]

    def dfs(node):
        for neighbor in range(n):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                reachable[start][neighbor] = 1
                dfs(neighbor)

    dfs(start)
    return reachable


n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

for i in range(n):
    result = find_reachable_vertices(adj_matrix, i)
    for j in range(n):
        print(result[i][j], end=" ")
    print()
