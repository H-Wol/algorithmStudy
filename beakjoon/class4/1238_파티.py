from sys import stdin
import heapq


input = stdin.readline


N, M, X = map(int, input().split())

nodes = [[] for _ in range(N)]


for _ in range(M):
    start, end, val = map(int, input().split())
    nodes[start - 1].append((end - 1, val))


def dijkstra(start, end, nodes, distance):
    heap = []
    distance[start - 1] = 0
    heapq.heappush(heap, (distance[start - 1], start - 1))
    while heap:
        d, now = heapq.heappop(heap)
        if distance[now] < d:
            continue
        for next, val in nodes[now]:
            if distance[next] > d + val:
                distance[next] = d + val
                heapq.heappush(heap, (distance[next], next))
    return distance[end - 1]


max = 0
for i in range(N):
    sum = dijkstra(i + 1, X, nodes, [float("inf") for _ in range(N)]) + dijkstra(
        X, i + 1, nodes, [float("inf") for _ in range(N)]
    )
    if sum > max:
        max = sum
print(max)
