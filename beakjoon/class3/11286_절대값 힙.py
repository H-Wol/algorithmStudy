import sys
import heapq
input = sys.stdin.readline

T = int(input())

heap = []
for _ in range(T):
    k = int(input())
    if k:
        heapq.heappush(heap, (abs(int(k)), int(k)))
    else:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)