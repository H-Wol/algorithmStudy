from sys import stdin

input = stdin.readline

INF = float('inf')

n = int(input())
s = input()
dp = [INF] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if s[j] == 'B' and s[i] == 'O':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        elif s[j] == 'O' and s[i] == 'J':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        elif s[j] == 'J' and s[i] == 'B':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

print(dp[-1] if dp[-1] != INF else -1)
