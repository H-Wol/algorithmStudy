from sys import stdin
from itertools import chain, combinations

input = stdin.readline


N = int(input())
S = list(map(int, input().split()))
subsets = chain.from_iterable(combinations(S, r) for r in range(len(S)+1))

sums = set()

for subset in subsets:
    sums.add(sum(subset))

i = 1
while i in sums:
    i += 1

print(i)
