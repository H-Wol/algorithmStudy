from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a


parent = [i for i in range(n + 1)]
edges.sort(key=lambda x: x[2])

total_cost = 0
for edge in edges:
    a, b, cost = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost


print(total_cost)
