import sys
from math import log2
input = sys.stdin.readline

N, M, K = map(int, input().split(" "))


max_battle = int(log2(N))
max_won = 0

for battle in range(1, max_battle+1):
    winnable = 2 ** battle
    if K < winnable:
        if M == 0:
            break
        M -= 1
    max_won += 1


print(max_won)
