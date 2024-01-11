from sys import stdin

input = stdin.readline
n, k = map(int, input().split())
numbers = list(map(int, input().split()))
count = [0] * (max(numbers) + 1)
start = 0
max_length = 0

for end in range(n):
    count[numbers[end]] += 1

    while count[numbers[end]] > k:
        count[numbers[start]] -= 1
        start += 1

    max_length = max(max_length, end - start + 1)

print(max_length)
