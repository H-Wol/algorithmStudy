import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split(" "))

coins = 0
worths = []

for _ in range(N):
    worths.append(int(input()))


while K:
    worth = worths.pop()
    if K >= worth:
        coins += K // worth
        K %= worth

print(coins)
