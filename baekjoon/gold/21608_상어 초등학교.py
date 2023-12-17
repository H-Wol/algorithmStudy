from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
left, right = 0, 1
min_difference = float('inf')

while right < n:
    difference = arr[right] - arr[left]

    if difference < m:
        right += 1
    elif difference == m:
        print(m)
        exit()
    else:
        min_difference = min(min_difference, difference)
        left += 1

print(min_difference)
