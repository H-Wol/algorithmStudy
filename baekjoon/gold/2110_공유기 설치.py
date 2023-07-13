from sys import stdin


def is_possible(c, distances, target):
    count = 1
    prev = distances[0]

    for i in range(1, len(distances)):
        if distances[i] - prev >= target:
            count += 1
            prev = distances[i]

    return count >= c


def find_max_min_distance(c, distances):
    distances.sort()
    left = 1
    right = distances[-1] - distances[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if is_possible(c, distances, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)


input = stdin.readline
n, c = map(int, input().split())
distances = [int(input()) for _ in range(n)]

find_max_min_distance(c, distances)
