from sys import stdin
import heapq

input = stdin.readline

N = int(input())
heap = []

for num in map(int, input().split()):
    heapq.heappush(heap, num)

for _ in range(1, N):
    row = list(map(int, input().split()))
    for num in row:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

print(heap[0])
