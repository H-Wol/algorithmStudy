from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)

dp = [float("inf")] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == float("inf"):
    print(-1)
else:
    print(dp[k])
