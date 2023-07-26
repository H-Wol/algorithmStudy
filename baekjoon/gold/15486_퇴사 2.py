from sys import stdin

input = stdin.readline
n = int(input())

schedule = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    t, p = schedule[i]
    next_index = i + t

    if next_index > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(p + dp[next_index], dp[i + 1])

print(dp[0])
