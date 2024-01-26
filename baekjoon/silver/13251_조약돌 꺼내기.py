from sys import stdin
from math import comb

input = stdin.readline
M = int(input())
marbles = list(map(int, input().split()))
K = int(input())
total_combinations = comb(sum(marbles), K)
favorable_combinations = 0

for marble in marbles:
    if marble >= K:
        favorable_combinations += comb(marble, K)

print(favorable_combinations / total_combinations)
