from sys import stdin

input = stdin.readline


def binarySearch(min, max, target, arr):
    mid = (min + max) // 2
    if min > max:
        return -1
    if arr[mid] < target <= arr[mid + 1]:
        return mid + 1
    if arr[mid] < target:
        return binarySearch(mid + 1, max, target, arr)
    else:
        return binarySearch(min, mid - 1, target, arr)


N = int(input())

A = [0]

dp = [0] * (N + 5)
dpLength = 1

A += list(map(int, input().split(" ")))

for i in range(1, N + 1):
    idx = binarySearch(0, dpLength - 1, A[i], dp)
    if idx == -1:
        dp[dpLength] = A[i]
        dpLength += 1
    else:
        dp[idx] = A[i]

print(dpLength - 1)
