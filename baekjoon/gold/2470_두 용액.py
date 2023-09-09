from sys import stdin

input = stdin.readline

n = int(input())
data = list(map(int, input().split()))


def two_liquids(n, data):
    data.sort()
    left, right = 0, n - 1
    min_diff = float("inf")
    result = (0, 0)

    while left < right:
        current_sum = data[left] + data[right]
        if abs(current_sum) < abs(min_diff):
            min_diff = current_sum
            result = (data[left], data[right])

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return result


result = two_liquids(n, data)
print(result[0], result[1])
