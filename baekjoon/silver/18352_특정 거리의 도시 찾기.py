from sys import stdin
import heapq


input = stdin.readline

V, E, K, start = map(int, input().split())


nodes = [[] for _ in range(V)]

for _ in range(E):
    s, e = map(int, input().split())
    nodes[s - 1].append((e - 1, 1))

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


answer = [idx + 1 for idx, val in enumerate(dijkstra(start, nodes, distance)) if val == K]
if answer == []:
    print(-1)
else:
    for i in answer:
        print(i)
