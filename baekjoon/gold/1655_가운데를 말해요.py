import heapq
from sys import stdin

input = stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]


max_heap = []
min_heap = []

result = []

for num in numbers:
    if not max_heap or -max_heap[0] >= num:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if len(max_heap) > len(min_heap) + 1:
        popped = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, popped)
    elif len(max_heap) < len(min_heap):
        popped = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -popped)

    if len(max_heap) > len(min_heap):
        result.append(-max_heap[0])
    else:
        result.append(min(-max_heap[0], min_heap[0]))

for i in result:
    print(i)
