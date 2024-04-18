from sys import stdin

input = stdin.readline

n = int(input())
prices = [int(input()) for _ in range(n)]
prices.sort(reverse=True)

total_cost = 0
n = len(prices)

for i in range(n):
    if (i + 1) % 3 != 0:
        total_cost += prices[i]
print(total_cost)
