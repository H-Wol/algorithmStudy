from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())

fixed_seats = []
for _ in range(m):
    fixed_seats.append(int(input()))

dp = [0] * (n + 1)
dp[0] = dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

total_arrangements = 1
start = 0

for seat in fixed_seats:
    total_arrangements *= dp[seat - start - 1]
    start = seat

total_arrangements *= dp[n - start]
print(total_arrangements)
