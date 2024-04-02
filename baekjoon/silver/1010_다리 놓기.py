from sys import stdin
import math

input = stdin.readline
T = int(input())

for _ in range(T):

    N, M = map(int, input().split())

    k = min(N, M)

    result = math.comb(M, k)

    print(result)
