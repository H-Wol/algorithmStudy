from itertools import permutations
from sys import stdin

input = stdin.readline


N, K = map(int, input().split())
weights = list(map(int, input().split()))
count = 0

for route in permutations(weights):
    current_weight = 500

    for w in route:
        current_weight += w - K

        if current_weight < 500:
            break

    else:
        count += 1
print(count)
