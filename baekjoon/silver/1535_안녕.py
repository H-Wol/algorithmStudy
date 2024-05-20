from sys import stdin

input = stdin.readline

N = int(input().strip())
L = list(map(int, input().strip().split()))
J = list(map(int, input().strip().split()))

dp = [0] * 100

for i in range(N):
    for j in range(99, L[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(max(dp))
