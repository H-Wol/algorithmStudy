import sys
import heapq

input = sys.stdin.readline

N = int(input())
time = 0
total = 0
times = list(map(int, input().rstrip().split(" ")))

heapq.heapify(times)

while times:
    time += heapq.heappop(times)
    total += time
print(total)
