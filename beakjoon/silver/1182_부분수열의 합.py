from itertools import combinations
from sys import stdin

input = stdin.readline

N, S = map(int, input().split())
groups = list(map(int, input().split()))
count = 0
for i in range(1, N + 1):
    sub = list(map(sum, combinations(groups, i)))
    count += sub.count(S)
print(count)
