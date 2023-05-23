from sys import stdin
import heapq


input = stdin.readline

V, E = map(int, input().split())
K = int(input())

nodes = [[] for _ in range(V)]


for _ in range(E):
    start, end, val = map(int, input().split())
    nodes[start - 1].append((end - 1, val))

distance = [float("inf") for _ in range(V)]


def dijkstra(start, nodes, distance):
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
    return distance


for d in dijkstra(K, nodes, distance):
    if d == float("inf"):
        print("INF")
        continue
    print(d)
