from sys import stdin

input = stdin.readline

N = int(input())
weights = list(map(int, input().split()))

weights.sort()
max_total_weight = 0

if N % 2 == 0:
    for i in range(N // 2):
        max_total_weight = max(
            max_total_weight, weights[i] + weights[N - i - 1])
else:
    for i in range(N // 2):
        max_total_weight = max(
            max_total_weight, weights[i] + weights[N - i - 2])
    max_total_weight = max(max_total_weight, weights[N - 1])

print(max_total_weight)
