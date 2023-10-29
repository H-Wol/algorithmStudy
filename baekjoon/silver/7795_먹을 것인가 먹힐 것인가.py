from math import gcd
from itertools import combinations
from sys import stdin

input = stdin.readline
T = int(input())

for _ in range(T):
    num_list = list(map(int, input().split()))
    n = num_list[0]
    num_list = num_list[1:]

    total_gcd_sum = 0

    for combo in combinations(num_list, 2):
        total_gcd_sum += gcd(combo[0], combo[1])
    print(total_gcd_sum)
