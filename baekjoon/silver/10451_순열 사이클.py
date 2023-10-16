from sys import stdin
from collections import defaultdict

input = stdin.readline


def dfs(graph, node, visited):
    visited[node] = True
    next_node = graph[node]
    if not visited[next_node]:
        dfs(graph, next_node, visited)


def count_cycles(graph, n):
    visited = [False] * (n + 1)
    cycles = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            cycles += 1

    return cycles


T = int(input())
for _ in range(T):
    n = int(input())
    permutation = list(map(int, input().split()))

    graph = defaultdict(int)
    for i in range(n):
        graph[i + 1] = permutation[i]

    cycles = count_cycles(graph, n)
    print(cycles)
