
from sys import stdin

input = stdin.readline

S, K = map(int, input().split())
q, r = divmod(S, K)
result = (q + 1) ** r * q ** (K - r)
print(result)
