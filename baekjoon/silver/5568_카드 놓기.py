from itertools import permutations
from sys import stdin

input = stdin.readline


def solution(numbers, k):
    result = set()
    perm = permutations(numbers, k)
    for p in perm:
        result.add(''.join(p))
    return len(result)


n = int(input().strip())
k = int(input().strip())

numbers = []
for _ in range(n):
    numbers.append(input().strip())

print(solution(numbers, k))
