from sys import stdin

input = stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

len_str1 = len(str1)
len_str2 = len(str2)

dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
max_length = 0

for i in range(1, len_str1 + 1):
    for j in range(1, len_str2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_length = max(max_length, dp[i][j])

print(max_length)
