from sys import stdin

input = stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x != y:
        parent[y] = x


n, m = map(int, input().split())


parent = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(parent, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")
