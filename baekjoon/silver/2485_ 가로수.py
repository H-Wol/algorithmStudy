from sys import stdin
import math

input = stdin.readline

N = int(input())
positions = [int(input()) for _ in range(N)]

gaps = []
for i in range(1, N):
    gaps.append(positions[i] - positions[i - 1])

gcd = gaps[0]
for gap in gaps[1:]:
    gcd = math.gcd(gcd, gap)

total_removed = sum([(gap // gcd) - 1 for gap in gaps])
print(total_removed)
