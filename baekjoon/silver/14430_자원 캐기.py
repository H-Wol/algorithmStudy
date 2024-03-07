from sys import stdin

input = stdin.readline


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        dp[i][j] = grid[i][j] + max(dp[i-1][j] if i-1 >= 0 else 0,
                                    dp[i][j-1] if j-1 >= 0 else 0)

print(dp[N-1][M-1])
