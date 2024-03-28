
from sys import stdin

input = stdin.readline


N = int(input())

sequence = [float(input()) for _ in range(N)]

max_product = [0] * N

max_product[0] = sequence[0]

for i in range(1, N):

    max_product[i] = max(sequence[i], max_product[i - 1] * sequence[i])

print(format(max(max_product), ".3f"))
