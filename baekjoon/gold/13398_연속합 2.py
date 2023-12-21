from sys import stdin

input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp_forward = [0] * N
dp_backward = [0] * N

max_sum = dp_forward[0] = numbers[0]
for i in range(1, N):
    dp_forward[i] = max(dp_forward[i - 1] + numbers[i], numbers[i])
    max_sum = max(max_sum, dp_forward[i])

dp_backward[N - 1] = numbers[N - 1]
for i in range(N - 2, -1, -1):
    dp_backward[i] = max(dp_backward[i + 1] + numbers[i], numbers[i])

max_result = max_sum
for i in range(1, N - 1):
    max_result = max(max_result, dp_forward[i - 1] + dp_backward[i + 1])

print(max_result)
