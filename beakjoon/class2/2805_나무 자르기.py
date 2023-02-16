from sys import stdin
input = stdin.readline

N, M = map(int, input().split(" "))

inputTree = list(map(int, input().split(" ")))


def binarySearch(min, max, target):
    if min > max:
        return 0
    if min == max:
        return min
    mid = (min + max) // 2
    if mid == min:
        return mid
    sum = 0
    for tree in inputTree:
        if tree > mid:
            sum += tree - mid

    if sum == target:
        return mid
    if sum > target:
        return binarySearch(mid, max, target)
    else:
        return binarySearch(min, mid, target)


print(binarySearch(0, max(inputTree), M))
