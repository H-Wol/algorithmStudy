from sys import stdin


input = stdin.readline
h, w = map(int, input().split())
heights = list(map(int, input().split()))

n = len(heights)
left_max = [0] * n
right_max = [0] * n
water = 0

left_max[0] = heights[0]
for i in range(1, n):
    left_max[i] = max(left_max[i - 1], heights[i])

right_max[n - 1] = heights[n - 1]
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], heights[i])

for i in range(n):
    water += min(left_max[i], right_max[i]) - heights[i]

print(water)
