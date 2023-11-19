from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
matrix = [input().rstrip() for _ in range(N)]

dp = [[0] * M for _ in range(N)]
max_size = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == '1':
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

            max_size = max(max_size, dp[i][j])

print(max_size**2)
