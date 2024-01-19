from sys import stdin

input = stdin.readline

n = int(input().strip())
coins = [1, 2, 5, 7]
dp = [float('inf')] * (n + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, n + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[n])
