from sys import stdin
import sys

sys.setrecursionlimit(10**9)
input = stdin.readline


def DFS(v, cnt):
    cnt += 1
    visited[v] = cnt
    for i in node[v]:
        if visited[i] == 0:
            DFS(i, cnt)


N, M, V = map(int, input().split())

node = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
visited_seq = 0
for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(N + 1):
    node[j].sort()
DFS(V, 0)
for i in range(1, N + 1):
    print(visited[i])
