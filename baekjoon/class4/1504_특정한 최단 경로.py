from sys import stdin
import heapq


input = stdin.readline

N, E = map(int, input().split())

nodes = [[] for _ in range(N)]


for _ in range(E):
    start, end, val = map(int, input().split())
    nodes[start - 1].append((end - 1, val))
    nodes[end - 1].append((start - 1, val))

u, v = map(int, input().split())


distance1 = [float("inf") for _ in range(N)]
distance2 = [float("inf") for _ in range(N)]
distance3 = [float("inf") for _ in range(N)]


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


d1 = dijkstra(1, nodes, distance1)
d2 = dijkstra(u, nodes, distance2)
d3 = dijkstra(v, nodes, distance3)

val = min(d1[u - 1] + d2[v - 1] + d3[N - 1], d1[v - 1] + d3[u - 1] + d2[N - 1])
if val == float("inf"):
    print(-1)
else:
    print(val)
