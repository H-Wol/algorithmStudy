import sys

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split(" ")))
array.sort()
M = int(sys.stdin.readline())


def binarySearch(min, max, target):
    if min > max:
        return 0
    mid = (min + max) // 2
    if array[mid] == target:
        return 1
    if array[mid] < target:
        return binarySearch(mid+1, max, target)
    else:
        return binarySearch(min, mid-1, target)


targets = list(map(int, sys.stdin.readline().split(" ")))

for target in targets:
    print(binarySearch(0, N-1, target))
