from sys import stdin

input = stdin.readline
n = int(input())

lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort(key=lambda x: x[0])

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

result = n - max(dp)
print(result)
