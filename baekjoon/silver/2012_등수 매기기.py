from sys import stdin

input = stdin.readline

n = int(input())
ranks = [int(input()) for _ in range(n)]
ranks.sort()

disorder = 0
for i in range(1, n + 1):
    disorder += abs(i - ranks[i - 1])

print(disorder)
