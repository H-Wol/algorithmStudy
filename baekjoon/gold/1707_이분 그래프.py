from sys import stdin
from collections import deque

input = stdin.readline
k = int(input())


def is_bipartite_graph(v, adj_list):
    colors = [0] * (v + 1)

    for i in range(1, v + 1):
        if colors[i] == 0:
            queue = deque()
            queue.append(i)
            colors[i] = 1

            while queue:
                cur = queue.popleft()

                for adj in adj_list[cur]:
                    if colors[adj] == 0:
                        colors[adj] = -colors[cur]
                        queue.append(adj)
                    elif colors[adj] == colors[cur]:
                        return False

    return True


for _ in range(k):
    v, e = map(int, input().split())
    adj_list = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    if is_bipartite_graph(v, adj_list):
        print("YES")
    else:
        print("NO")
