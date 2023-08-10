from sys import stdin

input = stdin.readline

n = int(input())
max_dp = [0] * 3
min_dp = [0] * 3

for _ in range(n):
    nums = list(map(int, input().split()))

    max_temp = max_dp.copy()
    min_temp = min_dp.copy()

    max_dp[0] = max(max_temp[0], max_temp[1]) + nums[0]
    max_dp[1] = max(max_temp) + nums[1]
    max_dp[2] = max(max_temp[1], max_temp[2]) + nums[2]

    min_dp[0] = min(min_temp[0], min_temp[1]) + nums[0]
    min_dp[1] = min(min_temp) + nums[1]
    min_dp[2] = min(min_temp[1], min_temp[2]) + nums[2]

print(max(max_dp), min(min_dp))
