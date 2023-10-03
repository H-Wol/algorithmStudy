from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))


i = n - 2
while i >= 0 and arr[i] <= arr[i + 1]:
    i -= 1

if i == -1:
    print(-1)
    exit()

j = n - 1
while arr[i] <= arr[j]:
    j -= 1
arr[i], arr[j] = arr[j], arr[i]

left, right = i + 1, n - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

if arr:
    for num in arr:
        print(num, end=" ")
