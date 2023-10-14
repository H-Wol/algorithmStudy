from itertools import permutations
from sys import stdin

input = stdin.readline


N = int(input())
numbers = list(map(int, input().split()))

max_sum = 0
for perm in permutations(numbers):
    diff_sum = sum(abs(perm[i] - perm[i - 1]) for i in range(1, len(perm)))
    max_sum = max(max_sum, diff_sum)
print(max_sum)
