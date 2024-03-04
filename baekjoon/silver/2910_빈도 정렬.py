from sys import stdin

input = stdin.readline


def frequency_sort(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    sorted_numbers = sorted(
        numbers, key=lambda x: (-frequency[x], numbers.index(x)))

    return sorted_numbers


N, C = map(int, input().split())
numbers = list(map(int, input().split()))

result = frequency_sort(numbers)

print(*result)
