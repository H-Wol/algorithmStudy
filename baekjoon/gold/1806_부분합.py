from sys import stdin

input = stdin.readline


n, s = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0
min_length = float("inf")
current_sum = 0

while right < n:
    current_sum += numbers[right]
    right += 1

    while current_sum >= s:
        min_length = min(min_length, right - left)
        current_sum -= numbers[left]
        left += 1

if min_length == float("inf"):
    print(0)
else:
    print(min_length)
