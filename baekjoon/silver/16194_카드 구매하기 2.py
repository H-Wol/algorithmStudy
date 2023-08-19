from sys import stdin

input = stdin.readline

n = int(input())
card_prices = [0] + list(map(int, input().split()))

dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + card_prices[j])

print(dp[n])
