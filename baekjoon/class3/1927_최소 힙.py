import sys
import heapq
input = sys.stdin.readline


N = int(input())
queue = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if queue == []:
            print(0)
            continue
        print(heapq.heappop(queue))
        continue
    heapq.heappush(queue, num)
