from sys import stdin

input = stdin.readline
INF = float("inf")
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]


min_cost = INF

for first_color in range(3):

    dp = [[INF] * 3 for _ in range(N)]

    dp[0][first_color] = cost[0][first_color]

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

    for last_color in range(3):
        if first_color != last_color:
            min_cost = min(min_cost, dp[N - 1][last_color])


print(min_cost)
