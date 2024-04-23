from sys import stdin

input = stdin.readline


t = int(input().strip())
results = []


def koong(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    return dp[n]


for _ in range(t):
    n = int(input().strip())
    result = koong(n)
    results.append(result)

for res in results:
    print(res)
