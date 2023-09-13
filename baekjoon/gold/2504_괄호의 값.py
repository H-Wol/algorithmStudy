from sys import stdin

input = stdin.readline


n = int(input())
solutions = list(map(int, input().split()))


def solve(arr):
    n = len(arr)
    left, right = 0, n - 1
    min_diff = float("inf")
    result = (0, 0)

    while left < right:
        current_sum = arr[left] + arr[right]
        current_diff = abs(current_sum)

        if current_diff < min_diff:
            min_diff = current_diff
            result = (arr[left], arr[right])

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return result


result = solve(solutions)
print(result[0], result[1])
