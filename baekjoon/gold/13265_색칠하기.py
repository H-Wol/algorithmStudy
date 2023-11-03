from sys import stdin
from collections import deque

input = stdin.readline
T = int(input())


def bfs(start: int, nodes: list, visited: list):
    queue = deque([start])
    visited[start] = 1
    while queue:
        cur_node = queue.popleft()
        for next_node in nodes[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = (visited[cur_node] + 1) % 2
                queue.append(next_node)
                continue
            if visited[next_node] == visited[cur_node]:
                return False
    return True


for _ in range(T):
    N, M = map(int, input().split())

    nodes = [[] for _ in range(N + 1)]
    flag = False
    visited = [-1] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    for i in range(N):
        if visited[i] != -1:
            continue
        if not bfs(i, nodes, visited):
            print("impossible")
            flag = True
            break
    if flag:
        continue
    print("possible")
