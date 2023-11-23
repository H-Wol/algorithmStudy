from sys import stdin

input = stdin.readline

n = int(input())
blocks = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * n
dp[0] = 0

for i in range(n):
    for j in range(1, blocks[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[n - 1] == INF:
    print(-1)
else:
    print(dp[n - 1])
