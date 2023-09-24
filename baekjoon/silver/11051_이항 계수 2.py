from sys import stdin

input = stdin.readline


MOD = 10007

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(min(i, k) + 1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
print(dp[n][k])
