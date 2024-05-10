from sys import stdin

input = stdin.readline


def calculate_A(N, P, Q, dp):
    if N == 0:
        return 1
    if N in dp:
        return dp[N]
    dp[N] = calculate_A(N // P, P, Q, dp) + calculate_A(N // Q, P, Q, dp)
    return dp[N]


N, P, Q = map(int, input().split())
dp = {}
result = calculate_A(N, P, Q, dp)
print(result)
