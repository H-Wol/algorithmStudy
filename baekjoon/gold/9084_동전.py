from sys import stdin

input = stdin.readline


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))
    m = int(input().strip())

    dp = [0] * (m + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, m + 1):
            dp[amount] += dp[amount - coin]
    print(dp[m])
