from sys import stdin

input = stdin.readline


def count_ways_to_reach_target(n, numbers):
    dp = [[0] * 21 for _ in range(n)]
    dp[0][numbers[0]] = 1

    for i in range(1, n - 1):
        for j in range(21):
            if dp[i - 1][j] > 0:
                if 0 <= j + numbers[i] <= 20:
                    dp[i][j + numbers[i]] += dp[i - 1][j]
                if 0 <= j - numbers[i] <= 20:
                    dp[i][j - numbers[i]] += dp[i - 1][j]

    return dp[n - 2][numbers[-1]]


n = int(input())
numbers = list(map(int, input().split()))

result = count_ways_to_reach_target(n, numbers)
print(result)
