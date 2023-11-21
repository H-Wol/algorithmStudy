from sys import stdin

input = stdin.readline


t = int(input())


for _ in range(t):
    n = int(input())
    dp = [[0] * 10 for _ in range(n + 1)]

    for i in range(10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(10):
            dp[i][j] = sum(dp[i - 1][:j + 1])

    result = sum(dp[n])
    print(result)
