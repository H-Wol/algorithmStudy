from sys import stdin

input = stdin.readline
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())

    nodes = [[] * (N) for _ in range(N)]
    distance = [int(1e9)] * (N + 1)

    for _ in range(M):
        s, e, t = map(int, input().split())
        nodes[s - 1].append((e - 1, t))
        nodes[e - 1].append((s - 1, t))

    for _ in range(W):
        s, e, t = map(int, input().split())
        nodes[s - 1].append((e - 1, -t))

    def floyd(nodes, n):
        flag = 0
        for i in range(0, n):
            for j in range(0, n):
                for node, dis in nodes[j]:
                    if distance[node] > distance[j] + dis:
                        distance[node] = distance[j] + dis
                        if i == n - 1:
                            flag = 1
        return flag

    if floyd(nodes, N):
        print("YES")
    else:
        print("NO")
