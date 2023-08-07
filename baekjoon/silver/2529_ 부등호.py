from itertools import permutations
from sys import stdin

input = stdin.readline


k = int(input())
inequality_sign = input().split()

numbers = list(map(str, range(10)))
candidates = list(permutations(numbers, k + 1))

max_candidate = None
min_candidate = None

for candidate in candidates:
    valid = True
    for i in range(k):
        if inequality_sign[i] == "<" and candidate[i] > candidate[i + 1]:
            valid = False
            break
        if inequality_sign[i] == ">" and candidate[i] < candidate[i + 1]:
            valid = False
            break

    if valid:
        max_candidate = candidate
        break

for candidate in reversed(candidates):
    valid = True
    for i in range(k):
        if inequality_sign[i] == "<" and candidate[i] > candidate[i + 1]:
            valid = False
            break
        if inequality_sign[i] == ">" and candidate[i] < candidate[i + 1]:
            valid = False
            break

    if valid:
        min_candidate = candidate
        break

print("".join(min_candidate))
print("".join(max_candidate))
