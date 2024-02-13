from sys import stdin

input = stdin.readline
N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted((num, i) for i, num in enumerate(nums))
positions = [sorted_nums.index((num, i)) for i, num in enumerate(nums)]

print(*positions)
