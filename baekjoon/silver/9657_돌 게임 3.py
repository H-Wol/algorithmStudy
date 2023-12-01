from sys import stdin


input = stdin.readline
n = int(input())

dp = [False] * (n + 1)
if n < 4:
    if n == 2:
        print(False)
    else:
        print(True)
    exit()
dp[1] = dp[3] = dp[4] = True

for i in range(5, n + 1):
    dp[i] = not (dp[i - 1] and dp[i - 3] and dp[i - 4])

print("SK" if dp[n] else "CY")
