from sys import stdin

input = stdin.readline
n, k = map(int, input().split())


dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][1] = 1

for i in range(1, k + 1):
    for j in range(n + 1):
        for x in range(j + 1):
            dp[j][i] += dp[x][i - 1]
            dp[j][i] %= 1000000000

print(dp[n][k])
