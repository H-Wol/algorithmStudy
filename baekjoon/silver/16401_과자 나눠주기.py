from sys import stdin

input = stdin.readline

M, N = map(int, input().split())
lengths = list(map(int, input().split()))

lengths.sort(reverse=True)


def can_share(mid):
    count = 0
    for length in lengths:
        count += length // mid
        if count >= M:
            return True
    return False


def binary_search(left, right):
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if can_share(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


answer = binary_search(1, lengths[0])

print(answer)
