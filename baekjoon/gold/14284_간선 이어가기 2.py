from sys import stdin
import heapq


input = stdin.readline

N, M = map(int, input().split())
nodes = [[] for _ in range(N)]


for _ in range(M):
    start, end, val = map(int, input().split())
    nodes[start - 1].append((end - 1, val))
    nodes[end - 1].append((start - 1, val))

distance = [float("inf") for _ in range(N)]
start, end = map(int, input().split())


def dijkstra(start, nodes, distance):
    heap = []
    distance[start - 1] = 0
    heapq.heappush(heap, (distance[start - 1], start - 1))
    while heap:
        d, now = heapq.heappop(heap)
        d = -d
        if distance[now] < d:
            continue
        for next, val in nodes[now]:
            if distance[next] > d + val:
                distance[next] = d + val
                heapq.heappush(heap, (-distance[next], next))
    return distance


print(dijkstra(start, nodes, distance)[end - 1])
