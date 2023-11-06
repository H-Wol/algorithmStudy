from sys import stdin

input = stdin.readline

s1 = input().strip()
s2 = input().strip()

len_s1, len_s2 = len(s1), len(s2)

dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

for i in range(1, len_s1 + 1):
    for j in range(1, len_s2 + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

lcs_length = dp[len_s1][len_s2]
print(lcs_length)

lcs = []
i, j = len_s1, len_s2
while i > 0 and j > 0:
    if s1[i - 1] == s2[j - 1]:
        lcs.append(s1[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print("".join(reversed(lcs)))
