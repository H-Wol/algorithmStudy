from sys import stdin
import heapq

input = stdin.readline

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]

end_times = []

schedule.sort(key=lambda x: x[0])

for start, end in schedule:
    if end_times and end_times[0] <= start:
        heapq.heappop(end_times)

    heapq.heappush(end_times, end)


print(len(end_times))
