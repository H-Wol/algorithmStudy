from sys import stdin

input = stdin.readline

K = int(input())

nums = []

for _ in range(K):
    num = int(input())
    if num == 0:
        nums.pop()
        continue
    nums.append(num)


print(sum(nums))
