from sys import stdin
import heapq


input = stdin.readline

N = int(input())
M = int(input())

nodes = [[] for _ in range(N)]

for _ in range(M):
    start, end, val = map(int, input().split())
    nodes[start - 1].append((end - 1, val))

start, end = map(int, input().split())


distance = [float("inf") for _ in range(N)]
distance[start - 1] = 0
heap = []

heapq.heappush(heap, (distance[start - 1], start - 1))
while heap:
    d, now = heapq.heappop(heap)
    if distance[now] < d:
        continue
    for next, val in nodes[now]:
        if distance[next] > d + val:
            distance[next] = d + val
            heapq.heappush(heap, (distance[next], next))
print(distance[end - 1])
