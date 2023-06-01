from sys import stdin

input = stdin.readline

n, m, r = map(int, input().split())

items = list(map(int, input().split()))

nodes = [[float("inf")] * (n) for _ in range(n)]

for idx, node in enumerate(nodes):
    node[idx] = 0

for _ in range(r):
    start, end, val = map(int, input().split())
    nodes[start - 1][end - 1] = val
    nodes[end - 1][start - 1] = val


def floyd(nodes, n):
    for k in range(0, n):
        for a in range(0, n):
            for b in range(0, n):
                nodes[a][b] = min(nodes[a][b], nodes[a][k] + nodes[k][b])
    return nodes


max = 0
for res in floyd(nodes, n):
    cnt = sum([items[idx] for idx, len in enumerate(res) if len <= m])
    if cnt > max:
        max = cnt
print(max)
