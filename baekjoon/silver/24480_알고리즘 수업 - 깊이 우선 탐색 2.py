from sys import stdin
import sys

sys.setrecursionlimit(10**5)
input = stdin.readline


def DFS(v):
    global visited_seq
    visited_seq += 1
    visited[v] = visited_seq
    for i in node[v]:
        if visited[i] == 0:
            DFS(i)


N, M, V = map(int, input().split())

node = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
visited_seq = 0
for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(N + 1):
    node[j].sort(reverse=True)
DFS(V)
for i in range(1, N + 1):
    print(visited[i])
