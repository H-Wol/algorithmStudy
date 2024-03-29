from sys import stdin

input = stdin.readline

V, E = map(int, input().split())

edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V + 1)]


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


answer = 0
for a, b, cost in edges:
    a = get_parent(a)
    b = get_parent(b)

    if not a == b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        answer += cost
print(answer)
