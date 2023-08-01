from sys import stdin

input = stdin.readline

n, s, m = map(int, input().split())
volumes = [0] + list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j]:
            if j + volumes[i] <= m:
                dp[i][j + volumes[i]] = True
            if j - volumes[i] >= 0:
                dp[i][j - volumes[i]] = True

for i in range(m, -1, -1):
    if dp[n][i]:
        print(i)
        exit()

print(-1)
