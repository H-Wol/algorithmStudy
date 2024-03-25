
N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

median_index = (N - 1) // 2

print(numbers[median_index])
