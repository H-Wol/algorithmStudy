from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))


n = len(arr)
dp = [0] * n

for i in range(n):
    dp[i] = arr[i]

    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
