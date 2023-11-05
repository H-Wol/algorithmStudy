from sys import stdin

input = stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())


dp = [[0] * n for _ in range(n)]


for i in range(n):
    dp[i][i] = 1


for i in range(n - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = 1


for k in range(2, n):
    for i in range(n - k):
        j = i + k
        if numbers[i] == numbers[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

for _ in range(m):
    s, e = map(int, input().split())
    s -= 1
    e -= 1

    if dp[s][e] == 1:
        print(1)
    else:
        print(0)
