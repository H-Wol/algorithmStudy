from sys import stdin
import heapq


input = stdin.readline

N = int(input())
M = int(input())

nodes = [[] for _ in range(N)]


for _ in range(M):
    start, end, val = map(int, input().split())
    nodes[start - 1].append((end - 1, val))

distance = [float("inf") for _ in range(N)]
distance2 = [0 for _ in range(N)]
start, end = map(int, input().split())


def dijkstra(start, nodes, distance, distance2):
    heap = []
    distance[start - 1] = 0
    distance2[start - 1] = 0
    heapq.heappush(heap, (distance[start - 1], start - 1))
    while heap:
        d, now = heapq.heappop(heap)
        d = -d
        if distance[now] < d:
            continue
        for next, val in nodes[now]:
            if distance[next] > d + val:
                distance[next] = d + val
                distance2[next] = now + 1
                heapq.heappush(heap, (-distance[next], next))
    return distance, distance2


d1, d2 = dijkstra(start, nodes, distance, distance2)
answer = [end]
now = end

while True:
    answer.append(d2[now - 1])
    now = answer[-1]
    if now == start:
        break

print(d1[end - 1])
print(len(answer))
print(" ".join(map(str, answer[::-1])))
