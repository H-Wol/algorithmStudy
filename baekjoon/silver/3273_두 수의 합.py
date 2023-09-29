from sys import stdin

input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

count = 0
left = 0
right = len(arr) - 1

arr.sort()

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        count += 1
        left += 1
        right -= 1
    elif current_sum < target:
        left += 1
    else:
        right -= 1

print(count)
