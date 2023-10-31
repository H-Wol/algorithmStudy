from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))


n = len(arr)

dp = [1] * n

prev_index = [-1] * n
max_length = 1
end_index = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev_index[i] = j
            if dp[i] > max_length:
                max_length = dp[i]
                end_index = i

lis = []
while end_index != -1:
    lis.append(arr[end_index])
    end_index = prev_index[end_index]

print(max_length)
print(" ".join(map(str, lis[::-1])))
