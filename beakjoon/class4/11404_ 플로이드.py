from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())


nodes = [[float("inf")] * (n) for _ in range(n)]

for idx, node in enumerate(nodes):
    node[idx] = 0

for _ in range(m):
    start, end, val = map(int, input().split())
    if nodes[start - 1][end - 1] < val:
        continue
    nodes[start - 1][end - 1] = val


def floyd(nodes, n):
    for k in range(0, n):
        for a in range(0, n):
            for b in range(0, n):
                nodes[a][b] = min(nodes[a][b], nodes[a][k] + nodes[k][b])
    return nodes


for res in floyd(nodes, n):
    print(" ".join(map(str, [i if i != float("inf") else 0 for i in res])))
