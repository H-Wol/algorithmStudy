from sys import stdin

input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))


def find_max_length(nums):
    max_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] >= nums[i - 1]:
            current_length += 1
        else:
            current_length = 1

        max_length = max(max_length, current_length)

    return max_length


def find_min_length(nums):
    min_length = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            current_length += 1
        else:
            current_length = 1

        min_length = max(min_length, current_length)

    return min_length


max_length = find_max_length(nums)
min_length = find_min_length(nums)

result = max(max_length, min_length)
print(result)
