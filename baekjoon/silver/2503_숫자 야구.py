from sys import stdin

input = stdin.readline
n = int(input())

distances = list(map(int, input().split()))

prices = list(map(int, input().split()))

min_cost = prices[0]
total_cost = 0

for i in range(n - 1):
    min_cost = min(min_cost, prices[i])
    total_cost += min_cost * distances[i]

print(total_cost)
