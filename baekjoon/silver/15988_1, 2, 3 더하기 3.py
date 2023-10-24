from sys import stdin

input = stdin.readline

T = int(input())
dp = [0] * 1000001
dp[0], dp[1], dp[2] = 1, 2, 4
cur = 3
for _ in range(T):
    N = int(input())

    MOD = 1000000009
    if N < 4:
        print(dp[N - 1])
        continue
    for i in range(cur, N):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
    print(dp[N - 1])
    cur = N
