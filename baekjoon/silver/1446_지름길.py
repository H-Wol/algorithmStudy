import heapq
from sys import stdin

input = stdin.readline
INF = float("inf")

N, D = map(int, input().split())
shortcuts = []

for _ in range(N):
    start, end, length = map(int, input().split())
    shortcuts.append((start, end, length))


def dijkstra(N, D, shortcuts):
    dist = [INF] * (D + 1)
    dist[0] = 0

    pq = []
    heapq.heappush(pq, (0, 0))

    while pq:
        current_dist, current_pos = heapq.heappop(pq)

        if current_dist > dist[current_pos]:
            continue

        for start, end, length in shortcuts:
            if start == current_pos:
                new_dist = current_dist + length
                if end <= D and new_dist < dist[end]:
                    dist[end] = new_dist
                    heapq.heappush(pq, (new_dist, end))

        next_pos = current_pos + 1
        if next_pos <= D and current_dist + 1 < dist[next_pos]:
            dist[next_pos] = current_dist + 1
            heapq.heappush(pq, (current_dist + 1, next_pos))

    return dist[D]


min_distance = dijkstra(N, D, shortcuts)
print(min_distance)
