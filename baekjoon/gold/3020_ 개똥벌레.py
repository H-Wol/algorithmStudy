from sys import stdin

input = stdin.readline

n, h = map(int, input().split())
half_n = n // 2
stalagmites, stalactites = [], []

for _ in range(half_n):
    stalagmites.append(int(input()))
    stalactites.append(int(input()))

stalagmites.sort()
stalactites.sort()

coll_counts = [0] * h


def bin_search(array, target):
    start, end = 0, len(array)

    while start < end:
        mid = (start + end) // 2

        if target <= array[mid]:
            end = mid
        else:
            start = mid + 1

    return start


for i in range(h):
    coll_counts[i] = half_n - bin_search(stalagmites, i + 1) + half_n - bin_search(stalactites, h - i)

min_coll = min(coll_counts)
print(min_coll, coll_counts.count(min_coll))
