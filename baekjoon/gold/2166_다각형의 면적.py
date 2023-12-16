from sys import stdin

input = stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
area = 0

for i in range(n - 1):
    area += (points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1])

area += (points[-1][0] * points[0][1] - points[0][0] * points[-1][1])

result = abs(area) / 2

print(f"{result:.1f}")
