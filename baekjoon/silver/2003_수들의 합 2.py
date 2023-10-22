from sys import stdin

input = stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
current_sum = 0
count = 0

while right < N:
    current_sum += arr[right]

    while current_sum > M:
        current_sum -= arr[left]
        left += 1

    if current_sum == M:
        count += 1

    right += 1

print(count)
