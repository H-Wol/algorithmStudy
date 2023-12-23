from sys import stdin

input = stdin.readline

N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

segments.sort(key=lambda x: (x[0], x[1]))

result = 0
start, end = segments[0]

for i in range(1, N):
    next_start, next_end = segments[i]

    if next_start <= end:
        end = max(end, next_end)
    else:
        result += end - start
        start, end = next_start, next_end

result += end - start

print(result)
